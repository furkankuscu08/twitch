"""Run the local game server. No credentials are needed for typed mode."""

import os
from dataclasses import fields

import uvicorn
from dotenv import load_dotenv

from minefield.core.config import Config
from minefield.server.app import ROOT, create_app


def config_from_env(environ):
    values = {}
    for item in fields(Config):
        if item.name in environ:
            values[item.name] = item.type(environ[item.name])
    return Config(**values)


def main():
    load_dotenv(ROOT / ".env")
    config = config_from_env(os.environ)
    uvicorn.run(
        create_app(config=config, debug=os.getenv("MINEFIELD_DEBUG") == "1"),
        host="127.0.0.1",
        port=config.GAME_PORT,
    )


if __name__ == "__main__":
    main()
