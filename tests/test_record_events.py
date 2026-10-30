"""Private event recording uses fake sockets, clocks and temporary files."""

import asyncio
import io
import json
from contextlib import asynccontextmanager

import pytest

from minefield.core.config import Config
from scripts import record_events


def test_records_wall_times_round_transitions_and_all_overlay_events(capsys):
    sink = io.StringIO()
    events = [
        {"type": "snapshot", "round": {"running": False}, "mines": []},
        {"type": "snapshot", "round": {"running": True}, "mines": []},
        {"type": "snapshot", "round": {"running": True}, "mines": []},
        *(
            {"type": kind, "id": "1"}
            for kind in ["mine_planted", "mine_armed", "spark", "fizzle", "spark"]
        ),
        {"type": "boom", "id": "1", "at": 1699999999.5, "word": "private-hit"},
        {"type": "false_alarm", "id": "1"},
        {"type": "reveal", "duds": [{"word": "private-dud"}], "stats": {}},
        {"type": "snapshot", "round": {"running": False}, "mines": []},
    ]
    recorder = record_events.Recorder(sink, clock=lambda: 1700000000.25)
    for event in events:
        recorder.receive(json.dumps(event))
    rows = [json.loads(line) for line in sink.getvalue().splitlines()]
    assert [
        row["event"]
        for row in rows
        if row["event"]["type"] not in {"round_start", "round_end"}
    ] == events
    assert [row["event"]["type"] for row in rows].count("round_start") == 1
    assert [row["event"]["type"] for row in rows].count("round_end") == 1
    assert all(row["received_wall"] == 1700000000.25 for row in rows)
    assert all(
        row["received_utc"] == "2023-11-14T22:13:20.250000+00:00" for row in rows
    )
    assert (
        next(row["event"]["at"] for row in rows if row["event"]["type"] == "boom")
        == 1699999999.5
    )
    assert capsys.readouterr() == ("", "")


def test_malformed_messages_are_ignored_and_lines_are_flushed():
    class Sink(io.StringIO):
        flushed = 0

        def flush(self):
            self.flushed += 1

    sink = Sink()
    recorder = record_events.Recorder(sink)
    for raw in [
        "private-invalid",
        "null",
        "[]",
        "1",
        "{}",
        '{"type": []}',
        '{"type":"snapshot","round":null}',
        '{"type":"snapshot","round":{"running":"yes"}}',
    ]:
        recorder.receive(raw)
    assert sink.getvalue() == ""
    recorder.receive('{"type":"spark","id":"1"}')
    assert sink.flushed == 1


def test_reconnect_marks_gap_and_does_not_invent_round_transitions(capsys):
    async def scenario():
        sink = io.StringIO()
        attempts = 0
        options = []

        class Socket:
            def __init__(self, running):
                self.running = running

            async def __aiter__(self):
                yield json.dumps(
                    {
                        "type": "snapshot",
                        "round": {"running": self.running},
                        "mines": [],
                    }
                )
                if attempts == 1:
                    raise OSError("private-provider-body")
                raise asyncio.CancelledError

        @asynccontextmanager
        async def connect(url, **kwargs):
            nonlocal attempts
            assert url == "ws://127.0.0.1:18100/ws/overlay"
            options.append(kwargs)
            attempts += 1
            yield Socket(attempts == 2)

        config = Config(GAME_PORT=18100, STT_RECONNECT_MIN_S=0.001)
        with pytest.raises(asyncio.CancelledError):
            await record_events.run(sink, config, connector=connect)
        rows = [json.loads(line)["event"] for line in sink.getvalue().splitlines()]
        assert [row["type"] for row in rows] == [
            "connected",
            "snapshot",
            "disconnected",
            "reconnected",
            "snapshot",
        ]
        assert all(
            option["max_queue"] == config.WS_CLIENT_QUEUE_SIZE for option in options
        )
        assert all(
            option["open_timeout"] > 0 and option["close_timeout"] > 0
            for option in options
        )

    asyncio.run(scenario())
    output = capsys.readouterr()
    assert "private-provider-body" not in output.out + output.err


def test_logs_are_exclusive_and_restricted_to_events_directory(tmp_path, monkeypatch):
    monkeypatch.setattr(record_events, "ROOT", tmp_path)
    target = tmp_path / "data/events/test.jsonl"
    with record_events.open_log(target) as sink:
        sink.write("existing\n")
    with pytest.raises(FileExistsError):
        record_events.open_log(target)
    with pytest.raises(ValueError):
        record_events.open_log(tmp_path / "data/tokens.json")
    with pytest.raises(ValueError):
        record_events.open_log(tmp_path / "outside.jsonl")
    assert target.read_text() == "existing\n"


def test_disk_failure_exits_instead_of_reconnecting():
    class BrokenSink:
        def write(self, value):
            raise OSError("private-disk-error")

    with pytest.raises(ValueError, match="^Cannot write event log$"):
        record_events.Recorder(BrokenSink()).receive('{"type":"spark","id":"1"}')


def test_cli_uses_configured_port_and_closes_log_on_cancellation(tmp_path, monkeypatch):
    monkeypatch.setattr(record_events, "ROOT", tmp_path)
    monkeypatch.setattr(record_events, "load_dotenv", lambda *args: None)
    monkeypatch.setenv("GAME_PORT", "18150")
    target = tmp_path / "data/events/rehearsal.jsonl"
    captured = []

    async def run(sink, config):
        captured.append(sink)
        assert config.GAME_PORT == 18150
        record_events.Recorder(sink).write({"type": "connected"})
        raise KeyboardInterrupt

    monkeypatch.setattr(record_events, "run", run)
    record_events.main(["--output", str(target)])
    assert captured[0].closed
    assert json.loads(target.read_text())["event"] == {"type": "connected"}


def test_cancellation_closes_socket():
    async def scenario():
        entered = asyncio.Event()
        closed = False

        class Socket:
            async def __aiter__(self):
                entered.set()
                await asyncio.Future()
                yield "unreachable"

        @asynccontextmanager
        async def connect(*args, **kwargs):
            nonlocal closed
            try:
                yield Socket()
            finally:
                closed = True

        task = asyncio.create_task(
            record_events.run(io.StringIO(), Config(), connector=connect)
        )
        await asyncio.wait_for(entered.wait(), 1)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        assert closed

    asyncio.run(scenario())
