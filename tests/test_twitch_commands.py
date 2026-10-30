import asyncio
from contextlib import asynccontextmanager
from dataclasses import replace
from types import SimpleNamespace

import httpx
from fastapi.testclient import TestClient

from minefield.core.config import Config
from minefield.server.app import create_app
from minefield.twitch_api.chat import Twitch


class FakeHelix:
    bot_id = "20"
    broadcaster_id = "10"

    def __init__(self):
        self.sent = []
        self.started = asyncio.Event()
        self.release = asyncio.Event()
        self.validated = 0
        self.auth = SimpleNamespace(validate=self.validate)

    async def validate(self, account):
        self.validated += 1

    async def initialize(self):
        pass

    async def send_message(self, message):
        self.sent.append(message)
        self.started.set()
        await self.release.wait()
        return {"is_sent": True}


def event(text, user="30", login="viewer", badges=()):
    return {
        "chatter_user_id": user,
        "chatter_user_login": login,
        "message": {"text": text},
        "badges": [{"set_id": badge} for badge in badges],
    }


def make(**changes):
    app = create_app(
        config=replace(Config(), ARM_DELAY_S=0, **changes),
        clock=lambda: 100,
        debug=True,
    )
    runtime = app.state.runtime
    helix = FakeHelix()
    twitch = Twitch(runtime, helix)
    runtime.twitch = twitch
    return app, runtime, twitch, helix


def drain(twitch):
    return [twitch.queue.get_nowait() for _ in range(twitch.queue.qsize())]


def test_commands_parse_redemption_rejections_and_snapshot_secrecy():
    app, runtime, twitch, _ = make()
    with TestClient(app) as client:
        twitch.handle_chat(event("!mine"))
        assert "No active round" in drain(twitch)[0]
        client.post("/dock/round/start")
        runtime.status["tunnel_url"] = "https://plant.example"
        twitch.handle_chat(event("  !MiNe   "))
        assert drain(twitch) == ["@viewer pick your mine: https://plant.example"]
        code = runtime.plants.issue("pineapple", 100)
        twitch.handle_chat(event(" !mInE  " + code.lower()))
        assert drain(twitch) == ["@viewer mine planted 💣 arming…"]
        assert next(iter(runtime.game.mines.values())).owner == "viewer"
        twitch.handle_chat(event("!mine " + code))
        assert "Unknown or expired" in drain(twitch)[0]
        assert "pineapple" not in str(runtime.snapshot())
        for text in ("!mine a b", "!mines", "hello", "!defuse extra"):
            twitch.handle_chat(event(text))
        twitch.handle_chat(event("!mine", user="20"))
        assert not drain(twitch)
        another = runtime.plants.issue("banana", 100)
        client.post("/dock/round/end")
        assert drain(twitch)[0].startswith("Round over:")
        assert not runtime.plants.codes
        client.post("/dock/round/start")
        twitch.handle_chat(event("!mine " + another))
        assert "Unknown or expired" in drain(twitch)[0]


def test_defuse_permissions_and_latest_eligible_boom():
    app, runtime, twitch, _ = make()
    with TestClient(app) as client:
        client.post("/dock/round/start")
        for owner, word in [("a", "pineapple"), ("b", "volcano")]:
            client.post("/dock/debug/plant", json={"owner": owner, "word": word})
        client.portal.call(runtime.tick)
        client.post("/dock/typed", json={"text": "pineapple volcano"})
        assert len(drain(twitch)) == 2
        twitch.handle_chat(event("!defuse"))
        assert all(mine.status == "exploded" for mine in runtime.game.mines.values())
        assert "moderators" in drain(twitch)[0]
        twitch.handle_chat(event("!DEFUSE", badges=["moderator"]))
        assert [mine.status for mine in runtime.game.mines.values()] == [
            "exploded",
            "false_alarm",
        ]
        twitch.handle_chat(event("!defuse", badges=["broadcaster"]))
        assert all(mine.status == "false_alarm" for mine in runtime.game.mines.values())


def test_tunnel_url_updates_snapshots_and_mine_replies():
    app, runtime, twitch, _ = make()
    with (
        TestClient(app) as client,
        client.websocket_connect("/ws/overlay") as overlay,
        client.websocket_connect("/ws/dock") as dock,
    ):
        overlay.receive_json()
        dock.receive_json()
        dock.receive_json()
        client.post("/dock/round/start")
        overlay.receive_json()
        dock.receive_json()
        for url in (
            "https://first.trycloudflare.com",
            None,
            "https://second.trycloudflare.com",
        ):
            client.portal.call(runtime.set_tunnel_url, url)
            assert dock.receive_json()["tunnel_url"] == url
            snapshot = overlay.receive_json()
            assert snapshot["plant_url"] == url
            assert dock.receive_json() == snapshot
            twitch.handle_chat(event("!mine"))
            reply = drain(twitch)[0]
            assert (url in reply) if url else ("unavailable" in reply)


def test_slow_chat_queue_is_bounded_and_does_not_block_game():
    async def scenario():
        _, runtime, twitch, helix = make(TWITCH_CHAT_QUEUE_SIZE=2)
        worker = asyncio.create_task(twitch.send_loop())
        try:
            twitch.enqueue("first")
            await asyncio.wait_for(helix.started.wait(), 1)
            for _ in range(10):
                twitch.enqueue("next")
            assert twitch.queue.qsize() == 2
            runtime.game.start(100)
            runtime.emit(runtime.game.plant("viewer", "pineapple", 100))
            assert len(runtime.game.mines) == 1
            helix.release.set()
            await asyncio.wait_for(twitch.queue.join(), 1)
        finally:
            worker.cancel()
            await asyncio.gather(worker, return_exceptions=True)
        assert len(helix.sent) == 3

    asyncio.run(scenario())


def test_server_lifespan_starts_and_stops_twitch_without_waiting_for_network():
    lifecycle = []

    @asynccontextmanager
    async def factory(runtime):
        class Service:
            async def run(self):
                lifecycle.append("started")
                try:
                    await asyncio.Future()
                finally:
                    lifecycle.append("cancelled")

        yield Service()
        lifecycle.append("closed")

    with TestClient(create_app(twitch_factory=factory)) as client:
        assert client.post("/dock/round/start").is_success
    assert lifecycle == ["started", "cancelled", "closed"]


def test_startup_retry_and_hourly_validation_are_background_work():
    async def scenario():
        _, _, twitch, helix = make(TWITCH_VALIDATE_S=0.01, TWITCH_RECONNECT_MIN_S=0.001)
        attempts = []
        closed = asyncio.Event()

        async def initialize():
            attempts.append(True)
            if len(attempts) == 1:
                raise httpx.ConnectError("private text must not be logged")

        async def validate(account):
            helix.validated += 1
            raise httpx.ConnectError("offline")

        async def listen():
            await asyncio.Future()

        async def close(socket):
            closed.set()

        helix.initialize = initialize
        helix.auth.validate = validate
        twitch.eventsub.run = listen
        twitch.eventsub.close = close
        task = asyncio.create_task(twitch.run())
        try:
            await asyncio.wait_for(closed.wait(), 1)
            assert len(attempts) == 2 and helix.validated >= 1
            twitch.enqueue("hello")
            helix.release.set()
            await asyncio.wait_for(twitch.queue.join(), 1)
            assert helix.sent == ["hello"]
        finally:
            task.cancel()
            await asyncio.gather(task, return_exceptions=True)

    asyncio.run(scenario())
