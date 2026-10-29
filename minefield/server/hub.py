"""Bounded queues isolate slow WebSocket clients from synchronous broadcast."""

import asyncio
from dataclasses import dataclass, field

from starlette.websockets import WebSocketDisconnect


@dataclass(eq=False)
class Client:
    socket: object
    channel: str
    queue: asyncio.Queue
    writer: asyncio.Task | None = field(default=None, repr=False)


class Hub:
    def __init__(self, queue_size):
        self.queue_size = queue_size
        self.clients = set()

    def add(self, socket, channel):
        client = Client(socket, channel, asyncio.Queue(self.queue_size))
        self.clients.add(client)
        client.writer = asyncio.create_task(self._write(client))
        return client

    async def _write(self, client):
        try:
            while True:
                await client.socket.send_json(await client.queue.get())
        except (asyncio.CancelledError, OSError, RuntimeError, WebSocketDisconnect):
            pass
        finally:
            self.clients.discard(client)
            try:
                await asyncio.wait_for(client.socket.close(code=1013), timeout=1)
            except (TimeoutError, OSError, RuntimeError, WebSocketDisconnect):
                pass

    def send(self, client, message):
        if client not in self.clients:
            return
        try:
            client.queue.put_nowait(message)
        except asyncio.QueueFull:
            self.clients.discard(client)
            client.writer.cancel()

    def broadcast(self, message, channel=None):
        for client in tuple(self.clients):
            if channel is None or client.channel == channel:
                self.send(client, message)

    async def remove(self, client):
        self.clients.discard(client)
        client.writer.cancel()
        await asyncio.gather(client.writer, return_exceptions=True)

    async def close(self):
        await asyncio.gather(*(self.remove(client) for client in tuple(self.clients)))
