"""Run the local game server. No credentials are needed for typed mode."""

import logging
import os
from contextlib import asynccontextmanager
from dataclasses import fields

import httpx
import uvicorn
from dotenv import load_dotenv

from minefield.core.config import Config
from minefield.server.app import ROOT, create_app
from minefield.twitch_api.auth import TOKEN_PATH, TwitchAuth
from minefield.twitch_api.chat import Twitch
from minefield.twitch_api.helix import Helix


def config_from_env(environ):
    values = {}
    for item in fields(Config):
        if item.name in environ:
            values[item.name] = item.type(environ[item.name])
    return Config(**values)


def main():
    load_dotenv(ROOT / ".env")
    logging.basicConfig(level=logging.INFO)
    config = config_from_env(os.environ)
    client_id = os.getenv("TWITCH_CLIENT_ID", "").strip()
    broadcaster = os.getenv("TWITCH_BROADCASTER_LOGIN", "").strip()
    logins = {
        account: os.getenv(f"TWITCH_{account.upper()}_LOGIN", "").strip()
        for account in ("bot", "test")
    }

    @asynccontextmanager
    async def twitch_factory(runtime):
        async with httpx.AsyncClient(timeout=config.TWITCH_IO_TIMEOUT_S) as client:
            auth = TwitchAuth(client, client_id, logins)
            yield Twitch(runtime, Helix(auth, config, broadcaster))

    enabled = client_id and broadcaster and logins["bot"] and TOKEN_PATH.exists()
    uvicorn.run(
        create_app(
            config=config,
            debug=os.getenv("MINEFIELD_DEBUG") == "1",
            twitch_factory=twitch_factory if enabled else None,
        ),
        host="127.0.0.1",
        port=config.GAME_PORT,
    )


if __name__ == "__main__":
    main()
