import asyncio
import logging
from dataclasses import replace
from types import SimpleNamespace

import httpx
import pytest
from fastapi.testclient import TestClient

from minefield.core.config import Config
from minefield.server.app import create_app
from minefield.twitch_api.auth import TwitchAuth
from minefield.twitch_api.chat import Twitch
from minefield.twitch_api.helix import BASE, Helix


def queued(twitch):
    return [twitch.queue.get_nowait() for _ in range(twitch.queue.qsize())]


def test_boom_latest_correction_and_single_recap_disclosure():
    now = [100.0]
    app = create_app(
        config=replace(Config(), ARM_DELAY_S=0), clock=lambda: now[0], debug=True
    )
    runtime = app.state.runtime
    twitch = Twitch(runtime, SimpleNamespace(bot_id="20"))
    runtime.twitch = twitch
    with TestClient(app) as client:
        client.post("/dock/round/start")
        for owner, word in [("a", "pineapple"), ("b", "volcano"), ("c", "banana")]:
            client.post("/dock/debug/plant", json={"owner": owner, "word": word})
        client.portal.call(runtime.tick)
        assert queued(twitch) == []
        client.post("/dock/typed", json={"text": "pineapple"})
        assert queued(twitch) == ["💥 @a's mine pineapple went off! @a has 1 pt."]
        now[0] += 1
        client.post("/dock/typed", json={"text": "volcano"})
        assert queued(twitch) == ["💥 @b's mine volcano went off! @b has 1 pt."]
        client.post("/dock/false-alarm")
        assert queued(twitch) == ["🧯 False alarm, @b gets a free re-plant"]
        assert [mine.status for mine in runtime.game.mines.values()] == [
            "exploded",
            "false_alarm",
            "armed",
        ]
        now[0] += 11
        client.post("/dock/false-alarm")
        assert queued(twitch) == []
        assert "banana" not in str(runtime.snapshot())
        client.post("/dock/round/end")
        (recap,) = queued(twitch)
        assert (
            recap == "Round over: 1 booms. 💥 @a (pineapple). "
            'Survived: @c\'s "banana". Top trappers: @a 1.'
        )
        assert "volcano" not in recap
        assert not runtime.game.mines
        client.post("/dock/round/end")
        assert queued(twitch) == []


def test_moderator_defuse_uses_same_announcement_once():
    app = create_app(
        config=replace(Config(), ARM_DELAY_S=0), clock=lambda: 100, debug=True
    )
    runtime = app.state.runtime
    twitch = Twitch(runtime, SimpleNamespace(bot_id="20"))
    runtime.twitch = twitch
    with TestClient(app) as client:
        client.post("/dock/round/start")
        client.post("/dock/debug/plant", json={"owner": "viewer", "word": "pineapple"})
        client.portal.call(runtime.tick)
        client.post("/dock/typed", json={"text": "pineapple"})
        queued(twitch)
        event = {
            "chatter_user_id": "30",
            "chatter_user_login": "mod",
            "message": {"text": "!defuse"},
            "badges": [{"set_id": "moderator"}],
        }
        twitch.handle_chat(event)
        twitch.handle_chat(event)
        assert queued(twitch) == ["🧯 False alarm, @viewer gets a free re-plant"]


@pytest.mark.parametrize("failure", ["failed", "timeout"])
def test_failed_announcements_never_retry_or_block_game(failure, tmp_path, caplog):
    async def scenario():
        attempted = []
        entered = asyncio.Event()

        async def transport(request):
            attempted.append(request)
            entered.set()
            if failure == "timeout":
                await asyncio.Future()
            return httpx.Response(503, text="private-pineapple access-secret")

        config = replace(Config(), ARM_DELAY_S=0, CHAT_SEND_TIMEOUT_S=0.02)
        async with httpx.AsyncClient(transport=httpx.MockTransport(transport)) as http:
            auth = TwitchAuth(http, "client", {"bot": "bot"}, tmp_path / "tokens.json")
            auth.save(
                "bot",
                {
                    "access_token": "access-secret",
                    "refresh_token": "refresh-secret",
                    "user_id": "20",
                },
            )
            helix = Helix(auth, config, "channel")
            helix.broadcaster_id = "10"
            runtime = create_app(config=config, clock=lambda: 100).state.runtime
            twitch = Twitch(runtime, helix)
            runtime.twitch = twitch
            runtime.game.start(100)
            runtime.game.plant("viewer", "pineapple", 100)
            runtime.game.arm(100)
            worker = asyncio.create_task(twitch.send_loop())
            try:
                hypothesis = {
                    "utt_id": "u",
                    "seq": 0,
                    "final": True,
                    "utt_start_wall": 100,
                    "words": [{"text": "pineapple", "start": 0, "end": 0, "prob": 1}],
                }
                runtime.emit(runtime.matcher.process(hypothesis, 100))
                await asyncio.wait_for(entered.wait(), 1)
                runtime.emit(runtime.game.false_alarm(100))
                events, recap = runtime.game.end(100)
                runtime.emit(events)
                twitch.enqueue(recap)
                assert not runtime.game.running
                await asyncio.wait_for(twitch.queue.join(), 1)
                assert len(attempted) == 3
                assert all(
                    str(request.url) == BASE + "/chat/messages" for request in attempted
                )
            finally:
                worker.cancel()
                await asyncio.gather(worker, return_exceptions=True)

    with caplog.at_level(logging.INFO):
        asyncio.run(scenario())
    assert "failed" in caplog.text
    assert "private-pineapple" not in caplog.text and "access-secret" not in caplog.text


def test_boom_chat_session_points_plural_and_survive_round_end():
    now = [100.0]
    app = create_app(
        config=replace(Config(), ARM_DELAY_S=0), clock=lambda: now[0], debug=True
    )
    runtime = app.state.runtime
    twitch = Twitch(runtime, SimpleNamespace(bot_id="20"))
    runtime.twitch = twitch
    with TestClient(app) as client:
        for points in [1, 2]:
            now[0] += 20
            client.post("/dock/round/start")
            client.post(
                "/dock/debug/plant", json={"owner": "viewer", "word": "pineapple"}
            )
            client.portal.call(runtime.tick)
            client.post("/dock/typed", json={"text": "pineapple"})
            unit = "pt" if points == 1 else "pts"
            assert queued(twitch) == [
                f"💥 @viewer's mine pineapple went off! @viewer has {points} {unit}."
            ]
            client.post("/dock/round/end")
            assert queued(twitch)[0].endswith(f"Top trappers: @viewer {points}.")
