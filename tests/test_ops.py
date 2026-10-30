"""WP14 launcher checks use only temporary configuration and fake children."""

import json
import os
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def launcher(tmp_path):
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    shutil.copy2(ROOT / "scripts/run_all.sh", scripts / "run_all.sh")
    binary = tmp_path / "bin"
    binary.mkdir()
    uv = binary / "uv"
    uv.write_text('#!/bin/bash\nprintf "%s\n" "$*" > uv-args\n')
    uv.chmod(0o755)
    cloudflared = binary / "cloudflared"
    cloudflared.write_text("#!/bin/bash\ntouch cloudflared-was-started\n")
    cloudflared.chmod(0o755)
    python = tmp_path / ".venv/bin/python"
    python.parent.mkdir(parents=True)
    python.write_text(
        f"#!{sys.executable}\n"
        + r"""import json, os, signal, subprocess, sys, time
from pathlib import Path
if sys.argv[1:] == ['-']:
    raise SystemExit(subprocess.run([sys.executable, '-'], env=os.environ).returncode)
module = sys.argv[2]
role = module.rsplit('.', 1)[-1]
with open('children.jsonl', 'a') as log:
    log.write(json.dumps({'args': sys.argv[1:], 'pid': os.getpid(),
        'pgid': os.getpgrp(),
        'debug': os.environ.get('MINEFIELD_DEBUG'),
        'client_id': os.environ.get('TWITCH_CLIENT_ID')}) + '\n')
Path(role + '.ready').touch()
def stop(*_):
    Path(role + '.stopped').touch()
    raise SystemExit(0)
signal.signal(signal.SIGTERM, stop)
signal.signal(signal.SIGINT, stop)
if role == 'server' and os.environ.get('TEST_TUNNEL_CHILD'):
    subprocess.Popen([__file__, '-m', 'minefield.tunnel'],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    while not Path('tunnel.ready').exists():
        time.sleep(.01)
if os.environ.get('TEST_EXIT_MODULE') == role:
    while not Path(('stt' if role == 'server' else 'server') + '.ready').exists():
        time.sleep(.01)
    os._exit(7)
while True:
    time.sleep(.05)
"""
    )
    python.chmod(0o755)
    environ = {
        key: value
        for key, value in os.environ.items()
        if not key.startswith(("TWITCH_", "DEEPGRAM_", "STT_", "MINEFIELD_"))
        and key not in {"GAME_PORT", "PLANT_PORT"}
    }
    environ.update(PATH=f"{binary}:{os.environ['PATH']}", PYTHONPATH=str(ROOT))

    def run(*args, **overrides):
        return subprocess.Popen(
            ["bash", str(scripts / "run_all.sh"), *args],
            cwd=tmp_path.parent,
            env=environ | overrides,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )

    return tmp_path, run


def wait_for(path):
    deadline = time.monotonic() + 5
    while not path.exists():
        assert time.monotonic() < deadline, f"Timed out waiting for {path.name}"
        time.sleep(0.02)


def children(path):
    return [
        json.loads(line) for line in (path / "children.jsonl").read_text().splitlines()
    ]


def assert_reaped(records):
    for child in records:
        with pytest.raises(ProcessLookupError):
            os.kill(child["pid"], 0)


def test_missing_key_fails_clearly_without_starting_children(launcher):
    path, run = launcher
    process = run()
    output, _ = process.communicate(timeout=10)
    assert process.returncode != 0
    assert "DEEPGRAM_API_KEY" in output
    assert "--demo" in output
    assert not (path / "children.jsonl").exists()


@pytest.mark.parametrize("stop_signal", [signal.SIGINT, signal.SIGTERM])
def test_demo_disables_network_children_and_reaps_server(launcher, stop_signal):
    path, run = launcher
    process = run("--demo", TWITCH_CLIENT_ID="must-not-connect", GAME_PORT="18200")
    try:
        wait_for(path / "server.ready")
        process.send_signal(stop_signal)
        output, _ = process.communicate(timeout=10)
        records = children(path)
        assert len(records) == 1
        assert records[0]["args"] == ["-m", "minefield.server"]
        assert records[0]["debug"] == "1"
        assert records[0]["client_id"] == ""
        assert "http://localhost:18200/dock" in output
        assert "/overlay?demo=1" in output
        assert (path / "server.stopped").exists()
        assert not (path / "cloudflared-was-started").exists()
        assert (path / "uv-args").read_text().strip() == "sync --locked"
        assert_reaped(records)
    finally:
        if process.poll() is None:
            process.terminate()
            process.communicate(timeout=10)


@pytest.mark.parametrize("exiting", ["server", "stt"])
def test_normal_mode_passes_tunnel_once_and_stops_other_child(launcher, exiting):
    path, run = launcher
    (path / ".env").write_text(
        "DEEPGRAM_API_KEY=temporary-test-value\nGAME_PORT=18200\n"
        "PLANT_PORT=18201\nSTT_MIC_PORT=18265\n"
        "UNUSED=$(touch shell-was-run)\n"
    )
    process = run(TEST_EXIT_MODULE=exiting, GAME_PORT="18210")
    output, _ = process.communicate(timeout=10)
    assert process.returncode == 7
    records = children(path)
    assert sorted(record["args"] for record in records) == [
        ["-m", "minefield.server", "--tunnel"],
        ["-m", "minefield.stt", "--mic"],
    ]
    assert "http://localhost:18210/mic" in output
    assert "18201" in output
    assert "18265" in output
    assert "temporary-test-value" not in output
    assert not (path / "shell-was-run").exists()
    assert not (path / "cloudflared-was-started").exists()
    other = "stt" if exiting == "server" else "server"
    assert (path / f"{other}.stopped").exists()
    assert_reaped(records)


@pytest.mark.parametrize("shutdown", ["crash", signal.SIGINT, signal.SIGTERM])
def test_tunnel_child_stops_after_server_crash_or_launcher_signal(launcher, shutdown):
    path, run = launcher
    process = run(
        DEEPGRAM_API_KEY="temporary-test-value",
        TEST_TUNNEL_CHILD="1",
        TEST_EXIT_MODULE="server" if shutdown == "crash" else "",
    )
    records = []
    try:
        wait_for(path / "tunnel.ready")
        wait_for(path / "stt.ready")
        if shutdown != "crash":
            process.send_signal(shutdown)
        process.communicate(timeout=10)
        wait_for(path / "tunnel.stopped")
        records = children(path)
        server = next(r for r in records if r["args"][1] == "minefield.server")
        tunnel = next(r for r in records if r["args"][1] == "minefield.tunnel")
        assert server["pgid"] == server["pid"] == tunnel["pgid"]
        assert (path / "stt.stopped").exists()
        assert process.returncode == (7 if shutdown == "crash" else 128 + shutdown)
    finally:
        if process.poll() is None:
            process.terminate()
            process.communicate(timeout=10)
        for child in records or children(path):
            try:
                os.kill(child["pid"], signal.SIGTERM)
            except ProcessLookupError:
                pass


@pytest.mark.parametrize("shutdown", [signal.SIGINT, "recorder-crash"])
def test_logging_arguments_and_recorder_cleanup(launcher, shutdown):
    path, run = launcher
    process = run(
        "--save-hyps",
        "data/rehearsal hyps.jsonl",
        "--save-events",
        "data/events/rehearsal events.jsonl",
        DEEPGRAM_API_KEY="temporary-test-value",
        TEST_EXIT_MODULE="record_events" if shutdown == "recorder-crash" else "",
    )
    try:
        wait_for(path / "record_events.ready")
        wait_for(path / "stt.ready")
        wait_for(path / "server.ready")
        if shutdown != "recorder-crash":
            process.send_signal(shutdown)
        output, _ = process.communicate(timeout=10)
        records = children(path)
        assert sorted(record["args"] for record in records) == [
            ["-m", "minefield.server", "--tunnel"],
            [
                "-m",
                "minefield.stt",
                "--mic",
                "--save-hyps",
                "data/rehearsal hyps.jsonl",
            ],
            [
                "-m",
                "scripts.record_events",
                "--output",
                "data/events/rehearsal events.jsonl",
            ],
        ]
        assert process.returncode == (7 if shutdown == "recorder-crash" else 130)
        assert "temporary-test-value" not in output
        assert (path / "server.stopped").exists()
        assert (path / "stt.stopped").exists()
        assert_reaped(records)
    finally:
        if process.poll() is None:
            process.terminate()
            process.communicate(timeout=10)
