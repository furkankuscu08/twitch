"""Run the local game server. No credentials are needed for typed mode."""

import argparse
import asyncio
import logging
import os
from contextlib import asynccontextmanager, nullcontext
from dataclasses import fields

import httpx
import uvicorn
from dotenv import load_dotenv

from minefield.core.config import Config
from minefield.server.app import ROOT, create_app
from minefield.server.plant import create_plant_app
from minefield.server.tunnel import Tunnel
from minefield.twitch_api.auth import TOKEN_PATH, TwitchAuth
from minefield.twitch_api.chat import Twitch
from minefield.twitch_api.helix import Helix


def config_from_env(environ):
    values = {}
    for item in fields(Config):
        if item.name in environ:
            values[item.name] = item.type(environ[item.name])
    return Config(**values)


async def run_servers(app, config, *, tunnel=False):
    game = uvicorn.Server(uvicorn.Config(app, host="127.0.0.1", port=config.GAME_PORT))
    plant = uvicorn.Server(
        uvicorn.Config(
            create_plant_app(app.state.runtime),
            host="127.0.0.1",
            port=config.PLANT_PORT,
        )
    )
    # Only the game listener owns process signals; either listener stopping
    # shuts down both. They share one event loop and the exact same Runtime.
    plant.capture_signals = nullcontext
    tasks = [asyncio.create_task(server.serve()) for server in (game, plant)]
    tunnel_task = None
    try:
        if tunnel:
            app.state.runtime.tunnel = Tunnel(app.state.runtime)
            tunnel_task = asyncio.create_task(app.state.runtime.tunnel.run())
        done, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            task.result()
    finally:
        if tunnel_task is not None:
            tunnel_task.cancel()
            await asyncio.gather(tunnel_task, return_exceptions=True)
        game.should_exit = plant.should_exit = True
        await asyncio.gather(*tasks, return_exceptions=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tunnel",
        action="store_true",
        help="Expose only the plant app with a temporary Cloudflare URL",
    )
    args = parser.parse_args(argv)
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
    app = create_app(
        config=config,
        debug=os.getenv("MINEFIELD_DEBUG") == "1",
        twitch_factory=twitch_factory if enabled else None,
    )
    asyncio.run(run_servers(app, config, tunnel=args.tunnel))


if __name__ == "__main__":
    main()
