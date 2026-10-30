"""Real channel acceptance; all chat input is sent via the test account API."""

import asyncio
import socket
from collections import deque
from contextlib import asynccontextmanager
from dataclasses import replace

import httpx
import pytest
import uvicorn

from minefield.core.config import Config
from minefield.server.app import create_app
from minefield.twitch_api.auth import TOKEN_PATH, TwitchAuth, settings
from minefield.twitch_api.chat import Twitch
from minefield.twitch_api.helix import Helix

pytestmark = pytest.mark.live


async def until(predicate):
    async with asyncio.timeout(30):
        while not predicate():
            await asyncio.sleep(0.02)


@asynccontextmanager
async def live_game():
    if not TOKEN_PATH.exists():
        pytest.skip("Authorize bot and test accounts first")
    client_id, logins = settings()
    import os

    broadcaster = os.environ["TWITCH_BROADCASTER_LOGIN"]
    outcomes = deque(maxlen=100)
    observed = deque(maxlen=100)

    class ObservedHelix(Helix):
        async def send_message(self, text, account="bot"):
            result = await super().send_message(text, account)
            outcomes.append((account, text, bool(result and result["is_sent"])))
            return result

    config = replace(Config(), ARM_DELAY_S=0)
    async with httpx.AsyncClient(timeout=config.TWITCH_IO_TIMEOUT_S) as external:
        auth = TwitchAuth(external, client_id, logins)
        if not {"bot", "test"}.issubset(auth.read_tokens()):
            pytest.skip("Authorize bot and test accounts first")
        await auth.validate("test")
        helix = ObservedHelix(auth, config, broadcaster)

        @asynccontextmanager
        async def factory(runtime):
            twitch = Twitch(runtime, helix)
            original = twitch.eventsub.on_chat

            def observe(event):
                observed.append((event["chatter_user_login"], event["message"]["text"]))
                original(event)

            twitch.eventsub.on_chat = observe
            yield twitch

        app = create_app(config=config, debug=True, twitch_factory=factory)
        listener = socket.socket()
        listener.bind(("127.0.0.1", 0))
        port = listener.getsockname()[1]
        server = uvicorn.Server(uvicorn.Config(app, log_level="error"))
        serving = asyncio.create_task(server.serve(sockets=[listener]))
        try:
            await until(lambda: server.started)
            runtime = app.state.runtime
            await until(lambda: runtime.status["eventsub"] == "connected")
            # WP11 will supply the real tunnel URL; no plant endpoint exists yet.
            runtime.status["tunnel_url"] = "https://plant.example"
            async with httpx.AsyncClient(base_url=f"http://127.0.0.1:{port}") as http:
                yield runtime, http, helix, outcomes, observed, logins
        finally:
            server.should_exit = True
            await serving


async def send_viewer(helix, text):
    # Verified 2026-10-30: ordinary users may send one message/second/channel.
    # Pace test inputs only; production chat delivery never retries a message.
    # https://dev.twitch.tv/docs/chat/#rate-limits
    await asyncio.sleep(1.1)
    result = await helix.send_message(text, "test")
    assert bool(result and result["is_sent"]), "Test-account chat was not delivered"


async def bot_reply(outcomes, observed, login, fragment):
    await until(
        lambda: any(
            account == "bot" and fragment in text and sent
            for account, text, sent in outcomes
        )
    )
    await until(
        lambda: any(user == login and fragment in text for user, text in observed)
    )


def test_live_commands_redemption_and_fresh_reconnect():
    async def scenario():
        async with live_game() as (runtime, http, helix, outcomes, observed, logins):
            assert (await http.post("/dock/round/start")).is_success
            await send_viewer(helix, "!mine")
            await bot_reply(
                outcomes,
                observed,
                logins["bot"],
                "pick your mine: https://plant.example",
            )
            code = runtime.plants.issue("pineapple", runtime.clock())
            await send_viewer(helix, "!mine " + code)
            await until(lambda: bool(runtime.game.mines))
            assert next(iter(runtime.game.mines.values())).owner == logins["test"]
            await bot_reply(outcomes, observed, logins["bot"], "mine planted")
            assert "pineapple" not in str(runtime.snapshot())
            original = runtime.twitch.eventsub.socket
            await original.close()
            await until(
                lambda: (
                    runtime.twitch.eventsub.socket is not None
                    and runtime.twitch.eventsub.socket is not original
                    and runtime.status["eventsub"] == "connected"
                )
            )
            another = runtime.plants.issue("volcano", runtime.clock())
            await send_viewer(helix, "!mine " + another)
            await bot_reply(
                outcomes, observed, logins["bot"], "already has a live mine"
            )
            assert another in runtime.plants.codes
            assert len(runtime.game.mines) == 1

    asyncio.run(scenario())


def test_live_boom_false_alarm_and_single_round_recap():
    async def scenario():
        async with live_game() as (runtime, http, helix, outcomes, observed, logins):
            await http.post("/dock/round/start")
            code = runtime.plants.issue("pineapple", runtime.clock())
            await send_viewer(helix, "!mine " + code)
            await until(lambda: bool(runtime.game.mines))
            await runtime.tick()
            await http.post("/dock/typed", json={"text": "I brought a pineapple"})
            await bot_reply(
                outcomes, observed, logins["bot"], "mine pineapple went off!"
            )
            await send_viewer(helix, "!defuse")
            await bot_reply(
                outcomes, observed, logins["bot"], "Only broadcaster or moderators"
            )
            assert next(iter(runtime.game.mines.values())).status == "exploded"
            await http.post("/dock/false-alarm")
            await bot_reply(outcomes, observed, logins["bot"], "False alarm,")
            assert next(iter(runtime.game.mines.values())).status == "false_alarm"
            code = runtime.plants.issue("volcano", runtime.clock())
            await send_viewer(helix, "!mine " + code)
            await until(
                lambda: any(
                    mine.word == "volcano" for mine in runtime.game.mines.values()
                )
            )
            await runtime.tick()
            await http.post("/dock/typed", json={"text": "We saw a volcano"})
            await bot_reply(outcomes, observed, logins["bot"], "mine volcano went off!")
            code = runtime.plants.issue("banana", runtime.clock())
            await send_viewer(helix, "!mine " + code)
            await until(
                lambda: any(
                    mine.word == "banana" for mine in runtime.game.mines.values()
                )
            )
            assert "banana" not in str(runtime.snapshot())
            await http.post("/dock/round/end")
            await bot_reply(outcomes, observed, logins["bot"], "Round over: 1 booms.")
            await http.post("/dock/round/end")
            await runtime.twitch.queue.join()
            recaps = [
                text
                for account, text, sent in outcomes
                if account == "bot" and text.startswith("Round over:") and sent
            ]
            assert len(recaps) == 1 and "volcano" in recaps[0] and "banana" in recaps[0]
            assert "pineapple" not in recaps[0]

    asyncio.run(scenario())


def test_live_idle_connection_survives_two_keepalive_windows():
    async def scenario():
        async with live_game() as (
            runtime,
            _http,
            _helix,
            _outcomes,
            _observed,
            _logins,
        ):
            original = runtime.twitch.eventsub.socket
            # Default Twitch welcome advertises 10 s. Include two full windows
            # plus the small bounded network grace used by the client.
            await asyncio.sleep(22)
            assert runtime.twitch.eventsub.socket is original
            assert runtime.status["eventsub"] == "connected"

    asyncio.run(scenario())
