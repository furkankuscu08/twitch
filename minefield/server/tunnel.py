"""One background Quick Tunnel, enabled only by the server's --tunnel flag."""

import asyncio
import logging
import re

LOG = logging.getLogger(__name__)
URL = re.compile(rb"https://[a-z0-9-]+\.trycloudflare\.com\b")


class Tunnel:
    def __init__(self, runtime, *, spawn=asyncio.create_subprocess_exec):
        self.runtime = runtime
        self.config = runtime.config
        self.spawn = spawn
        self.process = None

    async def stop(self, process):
        if process.returncode is None:
            try:
                process.terminate()
                await asyncio.wait_for(
                    process.wait(), self.config.TUNNEL_SHUTDOWN_TIMEOUT_S
                )
            except (TimeoutError, ProcessLookupError):
                pass
            finally:
                # Cancellation can interrupt the graceful wait. Kill before
                # yielding again, then reap even when that wait was cancelled.
                if process.returncode is None:
                    process.kill()
                await process.wait()

    async def read(self, process):
        url = None
        registered = False
        async with asyncio.timeout(self.config.TUNNEL_STARTUP_TIMEOUT_S):
            while not (url and registered):
                line = await process.stdout.readline()
                if not line:
                    return
                found = URL.search(line)
                if found:
                    url = found[0].decode("ascii")
                registered |= b"Registered tunnel connection" in line
            self.runtime.set_tunnel_url(url)
            LOG.info("Plant tunnel ready: %s", url)
        # Drain continuously; do not retain or echo cloudflared output.
        while await process.stdout.readline():
            pass
        await process.wait()

    async def run(self):
        delay = self.config.TUNNEL_RECONNECT_MIN_S
        while True:
            process = None
            try:
                # Verified 2026-10-30: account-free temporary public hostname;
                # restarting changes the URL. Expose only the plant listener.
                # https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/
                process = await self.spawn(
                    "cloudflared",
                    "tunnel",
                    "--no-autoupdate",
                    "--url",
                    f"http://127.0.0.1:{self.config.PLANT_PORT}",
                    "--output",
                    "json",
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.STDOUT,
                )
                self.process = process
                await self.read(process)
            except (OSError, TimeoutError, ValueError):
                LOG.warning("Plant tunnel unavailable; reconnecting")
            finally:
                self.runtime.set_tunnel_url(None)
                if process is not None:
                    await self.stop(process)
                self.process = None
            await asyncio.sleep(delay)
            delay = min(delay * 2, self.config.TUNNEL_RECONNECT_MAX_S)
