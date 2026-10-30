#!/usr/bin/env bash
# One local supervisor; the server alone owns cloudflared through --tunnel.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.."

mode=live
if [[ ${1:-} == --demo && $# == 1 ]]; then
    mode=demo
elif (( $# )); then
    printf 'Usage: scripts/run_all.sh [--demo]\n' >&2
    exit 2
fi
command -v uv >/dev/null || { printf 'Install uv before starting Minefield.\n' >&2; exit 1; }
uv sync --locked
export MINEFIELD_RUN_MODE="$mode"
ports=$(.venv/bin/python - <<'PY'
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from minefield.server.__main__ import config_from_env

load_dotenv(Path.cwd() / ".env")
try:
    config = config_from_env(os.environ)
except (ValueError, TypeError):
    sys.exit("Invalid Minefield configuration; check .env and port overrides.")
if os.environ["MINEFIELD_RUN_MODE"] != "demo" and not os.getenv("DEEPGRAM_API_KEY", "").strip():
    sys.exit("DEEPGRAM_API_KEY is missing; add it to .env or use scripts/run_all.sh --demo.")
print(config.GAME_PORT, config.PLANT_PORT, config.STT_MIC_PORT)
PY
)
read -r game_port plant_port mic_port <<< "$ports"
if [[ $mode == live ]]; then
    command -v cloudflared >/dev/null || { printf 'Install cloudflared for the plant tunnel.\n' >&2; exit 1; }
fi

pids=()
cleanup() {
    trap - EXIT INT TERM
    if (( ${#pids[@]} )); then
        kill "${pids[@]}" 2>/dev/null || true
        wait "${pids[@]}" 2>/dev/null || true
    fi
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

printf 'Dock: http://localhost:%s/dock\nOverlay: http://localhost:%s/overlay\n' "$game_port" "$game_port"
printf 'Local plant page: http://localhost:%s/\n' "$plant_port"
if [[ $mode == demo ]]; then
    export MINEFIELD_DEBUG=1 TWITCH_CLIENT_ID=''
    printf 'No-key demo: http://localhost:%s/overlay?demo=1\nUse the dock typed box and debug planting; no engine or tunnel is started.\n' "$game_port"
    .venv/bin/python -m minefield.server &
    pids+=("$!")
else
    printf 'Mic: http://localhost:%s/mic (engine WebSocket port %s)\n' "$game_port" "$mic_port"
    .venv/bin/python -m minefield.server --tunnel &
    pids+=("$!")
    .venv/bin/python -m minefield.stt --mic &
    pids+=("$!")
fi
printf 'Press Ctrl+C to stop Minefield and its tunnel.\n'
status=0
wait -n "${pids[@]}" || status=$?
printf 'Minefield process exited; stopping remaining processes.\n' >&2
exit "$status"
