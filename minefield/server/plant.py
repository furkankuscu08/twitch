"""Public plant page and API only; shares the local game's in-memory runtime."""

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse, JSONResponse
from pydantic import Field

from .app import ROOT, Input


class Pick(Input):
    hand_id: str = Field(min_length=1)
    word: str = Field(min_length=1)


def create_plant_app(runtime):
    app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

    @app.exception_handler(RequestValidationError)
    async def invalid(request: Request, exc: RequestValidationError):
        return JSONResponse({"detail": "Invalid request"}, status_code=422)

    @app.exception_handler(ValueError)
    async def rejected(request: Request, exc: ValueError):
        return JSONResponse(
            {"detail": str(exc)},
            status_code=409,
            headers={"Cache-Control": "no-store"},
        )

    @app.get("/")
    async def page():
        return FileResponse(ROOT / "web/plant/index.html")

    @app.get("/api/hand")
    async def hand():
        return JSONResponse(
            runtime.plants.hand(runtime.clock()),
            headers={"Cache-Control": "no-store"},
        )

    @app.post("/api/pick")
    async def pick(body: Pick):
        return JSONResponse(
            runtime.plants.pick(body.hand_id, body.word, runtime.clock()),
            headers={"Cache-Control": "no-store"},
        )

    return app
