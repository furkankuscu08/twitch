"""WP11 plant boundaries share the game runtime but expose no game controls."""

import inspect
from dataclasses import replace

from fastapi.testclient import TestClient

from minefield.core.config import Config
from minefield.server.app import create_app
from minefield.server.plant import create_plant_app


def test_hand_pick_bind_and_round_end_are_shared_with_game():
    clock = [100.0]
    game = create_app(config=replace(Config(), CODE_TTL_S=5), clock=lambda: clock[0])
    runtime = game.state.runtime
    with TestClient(game) as local, TestClient(create_plant_app(runtime)) as public:
        assert public.get("/api/hand").status_code == 409
        local.post("/dock/round/start")
        hand = public.get("/api/hand")
        assert hand.headers["cache-control"] == "no-store"
        hand = hand.json()
        assert len(set(hand["cards"])) == 6
        selected = public.post(
            "/api/pick", json={"hand_id": hand["hand_id"], "word": hand["cards"][0]}
        )
        assert selected.status_code == 200
        assert selected.headers["cache-control"] == "no-store"
        assert selected.json()["expires_at"] == 105
        runtime.plants.redeem(selected.json()["code"], "viewer", 101)
        assert len(runtime.game.mines) == 1
        assert hand["cards"][0] not in str(runtime.snapshot())
        pending = public.get("/api/hand").json()
        local.post("/dock/round/end")
        assert not runtime.plants.hands and not runtime.plants.codes
        local.post("/dock/round/start")
        assert (
            public.post(
                "/api/pick",
                json={"hand_id": pending["hand_id"], "word": pending["cards"][0]},
            ).status_code
            == 409
        )


def test_public_app_isolation_bad_messages_expiry_and_capacity(caplog):
    clock = [0.0]
    game = create_app(
        config=replace(Config(), MAX_PENDING_PLANTS=1, CODE_TTL_S=5),
        clock=lambda: clock[0],
        debug=True,
    )
    runtime = game.state.runtime
    runtime.game.start(0)
    app = create_plant_app(runtime)
    with TestClient(app) as public:
        for path in [
            "/dock",
            "/mic",
            "/overlay",
            "/stt/status",
            "/docs",
            "/openapi.json",
            "/.env",
            "/data/tokens.json",
        ]:
            assert public.get(path).status_code == 404
        for path in ["/dock/round/start", "/dock/debug/plant", "/stt/hypothesis"]:
            assert public.post(path, json={}).status_code == 404
        assert public.get("/").status_code == 200
        hand = public.get("/api/hand").json()
        assert public.get("/api/hand").status_code == 409
        for payload in [
            {},
            {"hand_id": 12, "word": "PRIVATE_INPUT"},
            {"hand_id": hand["hand_id"], "word": "PRIVATE_INPUT", "extra": 1},
        ]:
            response = public.post("/api/pick", json=payload)
            assert response.status_code == 422
            assert "PRIVATE_INPUT" not in response.text
        response = public.post("/api/pick", content="not-json")
        assert response.status_code == 422
        assert len(runtime.plants.hands) == 1 and not runtime.plants.codes
        clock[0] = 5
        assert (
            public.post(
                "/api/pick", json={"hand_id": hand["hand_id"], "word": hand["cards"][0]}
            ).status_code
            == 409
        )
        assert public.get("/api/hand").status_code == 200
    assert "PRIVATE_INPUT" not in caplog.text
    endpoint = next(route.endpoint for route in app.routes if route.path == "/api/pick")
    assert "await " not in inspect.getsource(endpoint)
