"""WP2 acceptance with fake time and local ASGI/WebSocket clients."""

import inspect
import json
from dataclasses import replace

import pytest
from fastapi.testclient import TestClient

from minefield.core.config import Config
from minefield.core.deck import Deck
from minefield.server.app import create_app


@pytest.fixture
def setup():
    clock = [100.0]
    deck = Deck(
        [{"word": "pineapple", "variants": []}, {"word": "volcano", "variants": []}]
    )
    app = create_app(
        config=replace(Config(), ARM_DELAY_S=2),
        deck=deck,
        clock=lambda: clock[0],
        debug=True,
    )
    with TestClient(app) as client:
        yield client, app.state.runtime, clock


def plant(client, owner="alice", word="pineapple"):
    return client.post("/dock/debug/plant", json={"owner": owner, "word": word})


def hyp(seq=1, *, final=False, utt_id="u1", utt_start_wall=103, text="pineapple"):
    return {
        "utt_id": utt_id,
        "seq": seq,
        "final": final,
        "words": [{"text": text, "start": 0, "end": 0.1, "prob": 0.95}],
        "utt_start_wall": utt_start_wall,
        "emitted_wall": 104,
        "lag_ms": 10,
    }


def test_debug_plant_arm_typed_boom(setup):
    client, runtime, clock = setup
    with client.websocket_connect("/ws/overlay") as ws:
        assert ws.receive_json()["round"] == {"running": False}
        client.post("/dock/round/start")
        assert ws.receive_json()["round"] == {"running": True}
        assert plant(client).status_code == 200
        assert ws.receive_json()["type"] == "mine_planted"
        clock[0] = 103
        client.post("/dock/typed", json={"text": "I want pineapple today"})
        assert ws.receive_json()["type"] == "mine_armed"
        assert ws.receive_json()["type"] == "spark"
        event = ws.receive_json()
        assert event["type"] == "boom" and event["source"] == "typed"
        assert event["receipt"][-1] == {"text": "pineapple", "hit": True}
        assert runtime.game.mines["1"].status == "exploded"


def test_typed_boom_receipt_masks_punctuation_joined_private_word(setup):
    client, runtime, clock = setup
    client.post("/dock/round/start")
    plant(client)
    plant(client, "bob", "volcano")
    clock[0] = 103
    with client.websocket_connect("/ws/overlay") as ws:
        ws.receive_json()
        response = client.post(
            "/dock/typed", json={"text": "volcano/pineapple pineapple"}
        )
        assert response.status_code == 200
        event = ws.receive_json()
        while event["type"] != "boom":
            event = ws.receive_json()
        assert event["receipt"] == [
            {"text": "•••", "hit": False},
            {"text": "pineapple", "hit": True},
        ]
        assert runtime.game.mines["2"].status == "armed"


def test_duplicate_out_of_order_final_and_late_hypotheses(setup):
    client, runtime, clock = setup
    client.post("/dock/round/start")
    plant(client)
    clock[0] = 104
    for seq in [3, 3, 2, 1]:
        assert client.post("/stt/hypothesis", json=hyp(seq)).status_code == 200
    assert runtime.game.mines["1"].status == "sparking"
    client.post("/stt/abort", json={"utt_id": "u1"})
    client.post("/stt/hypothesis", json=hyp(4, final=True))
    assert runtime.game.mines["1"].status == "armed"
    client.post(
        "/stt/hypothesis", json=hyp(1, final=True, utt_id="u2", utt_start_wall=104)
    )
    assert runtime.game.mines["1"].status == "exploded"


@pytest.mark.parametrize("cleanup", ["abort", "disconnected", "timeout", "replacement"])
def test_pending_cleanup(setup, cleanup):
    client, runtime, clock = setup
    client.post("/dock/round/start")
    plant(client)
    clock[0] = 104
    client.post("/stt/hypothesis", json=hyp())
    assert runtime.game.mines["1"].status == "sparking"
    if cleanup == "abort":
        client.post("/stt/abort", json={"utt_id": "u1"})
    elif cleanup == "replacement":
        client.post(
            "/stt/hypothesis", json=hyp(utt_id="u2", utt_start_wall=104, text="hello")
        )
    else:
        status = {
            "ok": cleanup == "timeout",
            "backend": "flux",
            "deepgram": "connected" if cleanup == "timeout" else "disconnected",
            "mic": "connected",
            "lag_ms_p95": 200,
            "reconnects": 0,
        }
        client.post("/stt/status", json=status)
        if cleanup == "timeout":
            clock[0] = 110
            client.portal.call(runtime.tick)
    assert runtime.game.mines["1"].status == "armed"
    assert runtime.matcher.candidates == {}


def test_snapshot_reconnect_contains_only_chips_and_remaining_seconds(setup):
    client, runtime, clock = setup
    client.post("/dock/round/start")
    plant(client)
    clock[0] = 101
    with client.websocket_connect("/ws/overlay") as ws:
        snapshot = ws.receive_json()
        assert snapshot["mines"] == [
            {"id": "1", "owner": "alice", "status": "arming", "arms_in_s": 1}
        ]
        assert "word" not in json.dumps(snapshot)
    clock[0] = 103
    client.post("/dock/typed", json={"text": "pineapple"})
    with client.websocket_connect("/ws/overlay") as ws:
        snapshot = ws.receive_json()
        assert snapshot["mines"][0]["status"] == "exploded"
        assert "pineapple" not in json.dumps(snapshot)
        assert "booms" not in snapshot
    client.post("/dock/round/end")
    with client.websocket_connect("/ws/overlay") as ws:
        assert ws.receive_json()["mines"] == []


def test_dock_gets_status_on_connect_and_health_changes(setup):
    client, _, _ = setup
    with client.websocket_connect("/ws/dock") as ws:
        assert ws.receive_json()["type"] == "snapshot"
        assert ws.receive_json()["engine"] == "disconnected"
        client.post(
            "/stt/status",
            json={
                "ok": True,
                "backend": "flux",
                "deepgram": "connected",
                "mic": "connected",
                "lag_ms_p95": 100,
                "reconnects": 0,
            },
        )
        assert ws.receive_json()["engine"] == "connected"


def test_invalid_inputs_do_not_mutate_or_echo_private_words(setup):
    client, runtime, _ = setup
    client.post("/dock/round/start")
    before = runtime.game.snapshot(100)
    for path, payload in [
        ("/stt/hypothesis", {"words": [{"text": "pineapple"}]}),
        ("/stt/hypothesis", hyp() | {"seq": "pineapple"}),
        (
            "/stt/hypothesis",
            hyp()
            | {"words": [{"text": "pineapple", "start": 2, "end": 1, "prob": 0.9}]},
        ),
        ("/dock/debug/plant", {"owner": 42, "word": "pineapple"}),
        ("/dock/typed", {"text": ["pineapple"]}),
        ("/stt/status", {"backend": "pineapple"}),
    ]:
        response = client.post(path, json=payload)
        assert response.status_code == 422
        assert "pineapple" not in response.text
        assert runtime.game.snapshot(100) == before
    assert client.get("/does-not-exist").status_code == 404


def test_debug_disabled_by_default():
    with TestClient(create_app()) as client:
        assert plant(client).status_code in {404, 405}


def test_planting_is_synchronous_and_limits_hold(setup):
    client, runtime, _ = setup
    assert not inspect.iscoroutinefunction(runtime.game.plant)
    client.post("/dock/round/start")
    assert plant(client).status_code == 200
    assert plant(client, "bob").status_code == 409
    assert plant(client, "alice", "volcano").status_code == 409
    assert len(runtime.game.mines) == 1


def test_equal_time_replacement_and_late_messages_cannot_confirm(setup):
    client, runtime, clock = setup
    client.post("/dock/round/start")
    plant(client)
    clock[0] = 104
    client.post("/stt/hypothesis", json=hyp())
    client.post("/stt/hypothesis", json=hyp(utt_id="same-time"))
    client.post("/stt/hypothesis", json=hyp(2))
    assert runtime.game.mines["1"].status == "armed"


def test_concurrent_plant_routes_run_on_event_loop_without_racing():
    import asyncio

    import httpx

    async def scenario():
        app = create_app(debug=True)
        loop = asyncio.get_running_loop()
        original = app.state.runtime.game.plant
        calls = []

        def checked_plant(*args):
            calls.append(asyncio.get_running_loop())
            return original(*args)

        app.state.runtime.game.plant = checked_plant
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app), base_url="http://test"
        ) as client:
            await client.post("/dock/round/start")
            responses = await asyncio.gather(
                *[
                    client.post(
                        "/dock/debug/plant", json={"owner": "same", "word": "pineapple"}
                    )
                    for _ in range(10)
                ]
            )
        assert [response.status_code for response in responses].count(200) == 1
        assert len(app.state.runtime.game.mines) == 1
        assert calls and all(item is loop for item in calls)

    asyncio.run(scenario())


def test_binary_socket_message_is_ignored_without_disconnecting(setup):
    client, _, _ = setup
    with client.websocket_connect("/ws/overlay") as ws:
        ws.receive_json()
        ws.send_bytes(b"malformed client input")
        client.post("/dock/round/start")
        assert ws.receive_json()["round"]["running"]


def test_static_redirect_preserves_demo_query(setup):
    client, _, _ = setup
    response = client.get("/overlay?demo=1&step=3", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"].endswith("/overlay/?demo=1&step=3")


def test_environment_defaults_and_overrides():
    from minefield.server.__main__ import config_from_env

    assert config_from_env({}).GAME_PORT == 8100
    config = config_from_env(
        {"GAME_PORT": "8200", "PLANT_PORT": "8201", "CONFIRM_N": "3"}
    )
    assert (config.GAME_PORT, config.PLANT_PORT, config.CONFIRM_N) == (8200, 8201, 3)
    with pytest.raises(ValueError):
        config_from_env({"GAME_PORT": "0"})


def test_rejected_round_start_preserves_pending_candidate(setup):
    client, runtime, clock = setup
    client.post("/dock/round/start")
    plant(client)
    clock[0] = 104
    client.post("/stt/hypothesis", json=hyp())
    assert runtime.game.mines["1"].status == "sparking"
    assert client.post("/dock/round/start").status_code == 409
    assert runtime.game.mines["1"].status == "sparking"
    client.post("/stt/hypothesis", json=hyp(2))
    assert runtime.game.mines["1"].status == "exploded"
