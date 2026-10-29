"""A stalled socket must never block broadcast or another client."""

import asyncio

from minefield.server.hub import Hub


class Socket:
    def __init__(self, slow=False):
        self.messages = []
        self.slow = slow
        self.closed = False

    async def send_json(self, message):
        if self.slow:
            await asyncio.Event().wait()
        self.messages.append(message)

    async def close(self, code=1000):
        self.closed = True


def test_overflow_disconnects_only_slow_client():
    async def scenario():
        hub = Hub(100)
        slow_socket, fast_socket = Socket(slow=True), Socket()
        slow, fast = hub.add(slow_socket, "overlay"), hub.add(fast_socket, "overlay")
        hub.broadcast({"type": "spark", "id": "1"})
        await asyncio.sleep(0)
        for index in range(101):
            hub.broadcast({"type": "spark", "id": str(index)})
            await asyncio.sleep(0)
        await asyncio.sleep(0)
        assert slow not in hub.clients
        assert slow_socket.closed
        assert fast in hub.clients
        assert len(fast_socket.messages) == 102
        await hub.remove(fast)

    asyncio.run(scenario())


def test_overflow_closes_socket_before_writer_first_runs():
    async def scenario():
        hub = Hub(100)
        socket = Socket()
        client = hub.add(socket, "overlay")
        # Deliberately do not yield: the writer has never entered its try/finally.
        for index in range(101):
            hub.send(client, {"type": "spark", "id": str(index)})
        assert client not in hub.clients
        for _ in range(10):
            await asyncio.sleep(0)
            if socket.closed:
                break
        assert socket.closed
        await hub.remove(client)

    asyncio.run(scenario())
