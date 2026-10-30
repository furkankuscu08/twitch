"""Fake cloudflared output/processes: no network in the default suite."""

import asyncio
from dataclasses import replace

from minefield.core.config import Config
from minefield.server.app import create_app
from minefield.server.tunnel import Tunnel


class Process:
    def __init__(self, lines=()):
        self.stdout = asyncio.StreamReader()
        for line in lines:
            self.stdout.feed_data(line + b"\n")
        self.returncode = None
        self.exited = asyncio.Event()
        self.terminated = False
        self.killed = False

    def terminate(self):
        self.terminated = True
        self.finish()

    def kill(self):
        self.killed = True
        self.finish()

    def finish(self):
        self.returncode = 0
        self.stdout.feed_eof()
        self.exited.set()

    async def wait(self):
        await self.exited.wait()
        return self.returncode


async def until(predicate):
    async with asyncio.timeout(2):
        while not predicate():
            await asyncio.sleep(0.001)


def test_tunnel_targets_plant_waits_for_registration_and_restarts_with_new_url():
    async def scenario():
        config = replace(Config(), PLANT_PORT=18101, TUNNEL_RECONNECT_MIN_S=0.001)
        runtime = create_app(config=config).state.runtime
        processes, calls = [], []

        async def spawn(*args, **kwargs):
            calls.append((args, kwargs))
            process = Process(
                [f"https://tunnel-{len(calls)}.trycloudflare.com".encode()]
            )
            processes.append(process)
            return process

        service = Tunnel(runtime, spawn=spawn)
        task = asyncio.create_task(service.run())
        try:
            await until(lambda: bool(processes))
            assert runtime.status["tunnel_url"] is None
            assert calls[0][0] == (
                "cloudflared",
                "tunnel",
                "--no-autoupdate",
                "--url",
                "http://127.0.0.1:18101",
                "--output",
                "json",
            )
            processes[0].stdout.feed_data(
                b'{"message":"Registered tunnel connection"}\n'
            )
            await until(
                lambda: (
                    runtime.status["tunnel_url"] == "https://tunnel-1.trycloudflare.com"
                )
            )
            processes[0].finish()
            await until(lambda: len(processes) == 2)
            assert runtime.status["tunnel_url"] is None
            processes[1].stdout.feed_data(b"Registered tunnel connection\n")
            await until(
                lambda: (
                    runtime.status["tunnel_url"] == "https://tunnel-2.trycloudflare.com"
                )
            )
        finally:
            task.cancel()
            await asyncio.gather(task, return_exceptions=True)
        assert processes[-1].terminated and runtime.status["tunnel_url"] is None

    asyncio.run(scenario())


def test_missing_binary_and_stalled_startup_recover_without_blocking_game():
    async def scenario():
        config = replace(
            Config(), TUNNEL_STARTUP_TIMEOUT_S=0.01, TUNNEL_RECONNECT_MIN_S=0.001
        )
        runtime = create_app(config=config).state.runtime
        processes, attempts = [], []

        async def spawn(*args, **kwargs):
            attempts.append(True)
            if len(attempts) == 1:
                raise FileNotFoundError
            process = Process()
            processes.append(process)
            return process

        task = asyncio.create_task(Tunnel(runtime, spawn=spawn).run())
        try:
            await until(lambda: len(processes) >= 2)
            assert processes[0].terminated
            assert runtime.status["tunnel_url"] is None
            runtime.game.start(0)
            assert runtime.plants.hand(1)["cards"]
        finally:
            task.cancel()
            await asyncio.gather(task, return_exceptions=True)
        assert processes[-1].terminated

    asyncio.run(scenario())


def test_shutdown_kills_child_if_termination_stalls():
    async def scenario():
        runtime = create_app(
            config=replace(Config(), TUNNEL_SHUTDOWN_TIMEOUT_S=0.01)
        ).state.runtime
        process = Process()
        process.terminate = lambda: None
        service = Tunnel(runtime)
        await service.stop(process)
        assert process.killed

    asyncio.run(scenario())
