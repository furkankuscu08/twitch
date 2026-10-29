"""FastAPI boundaries, heartbeat maintenance and private engine inputs."""

import asyncio
import json
import time
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, ConfigDict, Field, model_validator

from minefield.core.config import Config
from minefield.core.deck import Deck
from minefield.core.game import Game
from minefield.core.matcher import Matcher

from .hub import Hub

ROOT = Path(__file__).resolve().parents[2]


class Input(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, allow_inf_nan=False)


class Word(Input):
    text: str = Field(min_length=1)
    start: float = Field(ge=0)
    end: float = Field(ge=0)
    prob: float = Field(ge=0, le=1)

    @model_validator(mode="after")
    def ordered(self):
        if self.end < self.start:
            raise ValueError("Invalid word timing")
        return self


class Hypothesis(Input):
    utt_id: str = Field(min_length=1)
    seq: int = Field(ge=0)
    final: bool
    words: list[Word]
    utt_start_wall: float
    emitted_wall: float
    lag_ms: float


class Abort(Input):
    utt_id: str = Field(min_length=1)


class Heartbeat(Input):
    ok: bool
    backend: Literal["flux", "nova3"]
    deepgram: Literal["connected", "disconnected"]
    mic: Literal["connected", "disconnected"]
    lag_ms_p95: float = Field(ge=0)
    reconnects: int = Field(ge=0)


class Typed(Input):
    text: str = Field(min_length=1)


class Plant(Input):
    owner: str = Field(min_length=1)
    word: str = Field(min_length=1)


class Runtime:
    def __init__(self, config, deck, clock, debug):
        self.config = config
        self.game = Game(deck, config)
        self.matcher = Matcher(self.game)
        self.hub = Hub(config.WS_CLIENT_QUEUE_SIZE)
        self.clock = clock
        self.debug = debug
        self.status = {
            "type": "status",
            "mic": "disconnected",
            "engine": "disconnected",
            "deepgram": "disconnected",
            "eventsub": "disconnected",
            "tunnel_url": None,
        }
        self.last_heartbeat = None
        self.typed_sequence = 0

    def emit(self, events):
        for event in events:
            self.hub.broadcast(event)
        return {"ok": True}

    def snapshot(self):
        return self.game.snapshot(self.clock(), self.status["tunnel_url"])

    async def tick(self):
        self.emit(self.game.arm(self.clock()))
        if (
            self.last_heartbeat is not None
            and self.clock() - self.last_heartbeat >= self.config.ENGINE_TIMEOUT_S
        ):
            self.emit(self.matcher.abort())
            self.last_heartbeat = None
            self.status.update(
                engine="disconnected", deepgram="disconnected", mic="disconnected"
            )
            self.hub.broadcast(dict(self.status), "dock")

    async def maintain(self):
        while True:
            await asyncio.sleep(min(0.1, self.config.ENGINE_TIMEOUT_S))
            await self.tick()


def create_app(*, config=None, deck=None, clock=time.time, debug=False):
    config = config or Config()
    if deck is None:
        deck = Deck(json.loads((ROOT / "deck/en.json").read_text()))
    runtime = Runtime(config, deck, clock, debug)

    @asynccontextmanager
    async def lifespan(app):
        maintenance = asyncio.create_task(runtime.maintain())
        try:
            yield
        finally:
            maintenance.cancel()
            await asyncio.gather(maintenance, return_exceptions=True)
            await runtime.hub.close()

    app = FastAPI(lifespan=lifespan, docs_url=None, redoc_url=None, openapi_url=None)
    app.state.runtime = runtime

    @app.exception_handler(RequestValidationError)
    async def invalid_input(request: Request, exc: RequestValidationError):
        # Pydantic's default response includes private input values. Never echo them.
        return JSONResponse({"detail": "Invalid request"}, status_code=422)

    @app.exception_handler(ValueError)
    async def rejected(request: Request, exc: ValueError):
        # Core rejection messages are fixed strings, never the private selected word.
        return JSONResponse({"detail": str(exc)}, status_code=409)

    @app.post("/dock/round/start")
    async def start():
        events = runtime.game.start(clock())
        runtime.matcher.abort()
        events[0]["plant_url"] = runtime.status["tunnel_url"]
        return runtime.emit(events)

    @app.post("/dock/round/end")
    async def end():
        runtime.emit(runtime.matcher.abort())
        events, _recap = runtime.game.end(clock())
        return runtime.emit(events)

    @app.post("/dock/false-alarm")
    async def false_alarm():
        return runtime.emit(runtime.game.false_alarm(clock()))

    @app.post("/dock/typed")
    async def typed(body: Typed):
        now = clock()
        runtime.typed_sequence += 1
        # One explicitly selected typed utterance replaces any pending STT candidate.
        runtime.emit(runtime.matcher.abort())
        hypothesis = {
            "utt_id": f"typed-{runtime.typed_sequence}",
            "seq": 0,
            "final": False,
            "utt_start_wall": now,
            "words": [
                {"text": token, "start": 0, "end": 0, "prob": 1}
                for token in body.text.split()
            ],
        }
        events = []
        for seq in range(config.CONFIRM_N):
            hypothesis["seq"] = seq
            hypothesis["final"] = seq == config.CONFIRM_N - 1
            events += runtime.matcher.process(hypothesis, now, source="typed")
        return runtime.emit(events)

    if debug:

        @app.post("/dock/debug/plant")
        async def plant(body: Plant):
            return runtime.emit(runtime.game.plant(body.owner, body.word, clock()))

    @app.post("/stt/hypothesis")
    async def hypothesis(body: Hypothesis):
        return runtime.emit(runtime.matcher.process(body.model_dump(), clock()))

    @app.post("/stt/abort")
    async def abort(body: Abort):
        return runtime.emit(runtime.matcher.abort(body.utt_id))

    @app.post("/stt/status")
    async def status(body: Heartbeat):
        runtime.last_heartbeat = clock()
        runtime.status.update(
            mic=body.mic,
            deepgram=body.deepgram,
            engine="connected" if body.ok else "disconnected",
        )
        if not body.ok or body.deepgram != "connected":
            runtime.emit(runtime.matcher.abort())
        runtime.hub.broadcast(dict(runtime.status), "dock")
        return {"ok": True}

    async def socket_session(socket, channel):
        await socket.accept()
        client = runtime.hub.add(socket, channel)
        runtime.hub.send(client, runtime.snapshot())
        if channel == "dock":
            runtime.hub.send(client, dict(runtime.status))
        try:
            while True:
                # These sockets only receive server events. Ignore bad client payloads.
                message = await socket.receive()
                if message["type"] == "websocket.disconnect":
                    break
        except (WebSocketDisconnect, RuntimeError):
            pass
        finally:
            await runtime.hub.remove(client)

    @app.websocket("/ws/overlay")
    async def overlay(socket: WebSocket):
        await socket_session(socket, "overlay")

    @app.websocket("/ws/dock")
    async def dock(socket: WebSocket):
        await socket_session(socket, "dock")

    @app.get("/overlay")
    async def overlay_page(request: Request):
        return RedirectResponse(str(request.url.replace(path="/overlay/")))

    @app.get("/dock")
    async def dock_page(request: Request):
        return RedirectResponse(str(request.url.replace(path="/dock/")))

    for name in ("overlay", "dock", "assets"):
        directory = ROOT / "web" / name
        if directory.is_dir():
            app.mount(
                f"/{name}", StaticFiles(directory=directory, html=True), name=name
            )
    return app
