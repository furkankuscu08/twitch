"""Record private overlay events with wall-clock times. Run as a module."""

import argparse
import asyncio
import json
import os
import sys
import time
from datetime import UTC, datetime
from pathlib import Path

from dotenv import load_dotenv
from websockets.asyncio.client import connect
from websockets.exceptions import WebSocketException

from minefield.server.__main__ import config_from_env
from minefield.server.app import ROOT

EVENTS = {
    "snapshot",
    "mine_planted",
    "mine_armed",
    "spark",
    "boom",
    "fizzle",
    "false_alarm",
    "reveal",
}


class Recorder:
    def __init__(self, sink, *, clock=time.time):
        self.sink = sink
        self.clock = clock
        self.running = None

    def write(self, event, now=None):
        now = self.clock() if now is None else now
        row = {
            "received_wall": now,
            "received_utc": datetime.fromtimestamp(now, UTC).isoformat(),
            "event": event,
        }
        try:
            self.sink.write(json.dumps(row) + "\n")
            self.sink.flush()
        except OSError:
            # Disk failures must stop the recorder/launcher, not look like a
            # recoverable socket failure and silently lose the rehearsal log.
            raise ValueError("Cannot write event log") from None

    def receive(self, raw):
        try:
            event = json.loads(raw)
        except (ValueError, TypeError):
            return
        if not isinstance(event, dict) or not isinstance(event.get("type"), str):
            return
        kind = event["type"]
        if kind not in EVENTS:
            return
        if kind == "snapshot":
            state = event.get("round")
            if not isinstance(state, dict) or type(state.get("running")) is not bool:
                return
        now = self.clock()
        if kind == "snapshot":
            running = event["round"]["running"]
            if self.running is not None and running != self.running:
                self.write({"type": "round_start" if running else "round_end"}, now)
            self.running = running
        elif kind == "reveal":
            self.write({"type": "round_end"}, now)
            self.running = False
        self.write(event, now)


async def run(sink, config, *, connector=connect, clock=time.time):
    recorder = Recorder(sink, clock=clock)
    connected_once = False
    delay = config.STT_RECONNECT_MIN_S
    while True:
        try:
            async with connector(
                f"ws://127.0.0.1:{config.GAME_PORT}/ws/overlay",
                max_queue=config.WS_CLIENT_QUEUE_SIZE,
                open_timeout=config.STT_HTTP_TIMEOUT_S,
                close_timeout=config.STT_HTTP_TIMEOUT_S,
            ) as socket:
                recorder.write(
                    {"type": "reconnected" if connected_once else "connected"}
                )
                connected_once = True
                # A reconnect snapshot observes current state, not when the
                # round actually started/ended during the missing interval.
                recorder.running = None
                delay = config.STT_RECONNECT_MIN_S
                async for raw in socket:
                    recorder.receive(raw)
        except (OSError, TimeoutError, WebSocketException):
            pass
        recorder.write({"type": "disconnected"})
        print(
            "Event recorder disconnected; retrying. Log gap marked.",
            file=sys.stderr,
            flush=True,
        )
        await asyncio.sleep(delay)
        delay = min(delay * 2, config.STT_RECONNECT_MAX_S)


def open_log(path):
    target = Path(path).resolve()
    if not target.is_relative_to(ROOT / "data/events"):
        raise ValueError("Event logs must be saved under data/events/")
    target.parent.mkdir(parents=True, exist_ok=True)
    return target.open("x", encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    load_dotenv(ROOT / ".env")
    try:
        config = config_from_env(os.environ)
        with open_log(args.output) as sink:
            print(f"Event log: {args.output}", flush=True)
            asyncio.run(run(sink, config))
    except KeyboardInterrupt:
        pass
    except (OSError, ValueError, TypeError):
        parser.exit(
            1,
            "Event recording failed; check config and a new data/events/ path.\n",
        )


if __name__ == "__main__":
    main()
