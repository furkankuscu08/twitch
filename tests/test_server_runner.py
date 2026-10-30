import asyncio
from dataclasses import replace

import httpx
import pytest

from minefield.core.config import Config
from minefield.server import __main__ as cli
from minefield.server.app import create_app


@pytest.mark.parametrize("tunnel", [False, True])
def test_both_listeners_share_runtime_and_stop_together(monkeypatch, tunnel):
    async def scenario():
        servers = []
        stop = asyncio.Event()
        lifecycle = []

        class Tunnel:
            def __init__(self, runtime):
                lifecycle.append("created")

            async def run(self):
                lifecycle.append("started")
                try:
                    await asyncio.Future()
                finally:
                    lifecycle.append("cancelled")

        class Server:
            def __init__(self, config):
                self.config = config
                self.should_exit = False
                servers.append(self)

            async def serve(self):
                if self.config.port == 18100:
                    await stop.wait()
                else:
                    while not self.should_exit:
                        await asyncio.sleep(0)

        monkeypatch.setattr(cli.uvicorn, "Server", Server)
        monkeypatch.setattr(cli, "Tunnel", Tunnel)
        config = replace(Config(), GAME_PORT=18100, PLANT_PORT=18101)
        app = create_app(config=config)
        serving = asyncio.create_task(cli.run_servers(app, config, tunnel=tunnel))
        try:
            async with asyncio.timeout(2):
                while len(servers) != 2:
                    await asyncio.sleep(0)
            assert [s.config.host for s in servers] == ["127.0.0.1"] * 2
            assert [s.config.port for s in servers] == [18100, 18101]
            app.state.runtime.game.start(0)
            async with httpx.AsyncClient(
                transport=httpx.ASGITransport(app=servers[1].config.app),
                base_url="http://plant",
            ) as client:
                hand = (await client.get("/api/hand")).json()
                assert hand["hand_id"] in app.state.runtime.plants.hands
            stop.set()
            await asyncio.wait_for(serving, 2)
            assert all(s.should_exit for s in servers)
            assert lifecycle == (["created", "started", "cancelled"] if tunnel else [])
        finally:
            stop.set()
            serving.cancel()
            await asyncio.gather(serving, return_exceptions=True)

    asyncio.run(scenario())


@pytest.mark.parametrize("args, enabled", [([], False), (["--tunnel"], True)])
def test_only_cli_flag_enables_tunnel_without_reading_real_env(
    monkeypatch, args, enabled
):
    observed = []
    monkeypatch.setattr(cli, "load_dotenv", lambda *_: None)
    monkeypatch.setenv("TWITCH_CLIENT_ID", "")

    async def run_servers(app, config, *, tunnel):
        observed.append(tunnel)

    monkeypatch.setattr(cli, "run_servers", run_servers)
    cli.main(args)
    assert observed == [enabled]
