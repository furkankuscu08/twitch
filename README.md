# Minefield

Viewers plant secret words. When the streamer says one, the overlay explodes and names its owner. Game state stays in memory; ending a round reveals the surviving mines. [SPEC.md](SPEC.md) defines the rules and messages.

## Setup

Run the Python services in WSL/Linux. Open the microphone page in **Chrome on Windows**, where microphone access works reliably. You need Bash 4.3+, Python 3.12, [uv](https://docs.astral.sh/uv/getting-started/installation/), and [cloudflared](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/) on `PATH` for normal play. No GPU, local speech model, Node.js or frontend build is required.

```bash
uv sync --locked
```

Create a local `.env` in the checkout. Fill in values privately; never commit it, credentials, or anything under `data/`.

```dotenv
DEEPGRAM_API_KEY=
DEEPGRAM_REGION=eu
STT_BACKEND=flux
TWITCH_CLIENT_ID=
TWITCH_BROADCASTER_LOGIN=
TWITCH_BOT_LOGIN=
TWITCH_TEST_LOGIN=
TWITCH_TEST2_LOGIN=
TWITCH_TEST3_LOGIN=
```

Create an API key in the [Deepgram console](https://console.deepgram.com/) using its [key setup guide](https://developers.deepgram.com/guides/fundamentals/make-your-first-api-request). The default backend is Flux, with Nova-3 as a backup using the same key. Speech goes to the EU endpoint by default. Deck words are never sent as recognition hints.

### Twitch authorization

Register the app in the broadcaster's [Twitch developer console](https://dev.twitch.tv/console/apps), following [app registration](https://dev.twitch.tv/docs/authentication/register-app/). Set its client type to **Public** and put its Client ID in `TWITCH_CLIENT_ID`. If registration requires an OAuth redirect URL, `http://localhost:3000` is sufficient; device-code login does not use that callback. Minefield needs no client secret.

Set `TWITCH_BROADCASTER_LOGIN` to the channel owner, `TWITCH_BOT_LOGIN` to the bot account, and `TWITCH_TEST_LOGIN` to a separate test viewer. Make the account configured by `TWITCH_BOT_LOGIN` a moderator in the channel. Authorize the bot first, then the test viewer:

```bash
uv run python -m minefield.twitch_api.auth --account bot
uv run python -m minefield.twitch_api.auth --account test
```

For each command, open the printed activation URL, verify that the browser is signed into the account named by the matching `.env` variable, and approve the code. The CLI validates the identity and saves rotating token pairs in `data/tokens.json`. The bot requests `user:read:chat` and `user:write:chat`; the test viewer requests only `user:write:chat`. No broadcaster token is required. The test viewer is optional during play and required for automated live checks.

The [Public client device-code flow](https://dev.twitch.tv/docs/authentication/getting-tokens-oauth/#device-code-grant-flow) was verified on 30 October 2026. Never paste tokens into chat, screenshots or bug reports.

For blind planting, set `TWITCH_TEST2_LOGIN` and `TWITCH_TEST3_LOGIN` to the two extra viewers and authorize them with `--account test2` and `--account test3`. Use your own incognito Chrome window for viewer activation, checking the account before approving each code; do not use a browser signed in as the broadcaster. All three viewers request only `user:write:chat` and have separate entries in the same token file.

Before each rehearsal and recording, with the server stopped, refresh all three viewer tokens:

```bash
for account in test test2 test3; do
  uv run python -m minefield.twitch_api.auth --account "$account" --refresh
done
```

A failed refresh prints the exact device-login command needed to authorize that account again.

### Blind-plant recording fallback

After refreshing the three viewer tokens, start the normal server and a round. Then run:

```bash
uv run python -m scripts.blind_plant
```

The helper attempts one mine per viewer over an independently random 0–60 second delay, using the local plant API and real viewer chat messages. A single dock WebSocket confirms each owner. Output shows only owners and success/failure; a credential warning includes that account's exact refresh command. The helper never reveals choices, writes words or automatically replants. A failed account does not block the others. Existing one-live-mine-per-viewer and four-live-mine limits still apply.

`BLIND_PLANT_WINDOW_S` overrides the delay window; `BLIND_PLANT_CONFIRM_TIMEOUT_S` overrides the 10-second confirmation timeout. Local URLs respect `GAME_PORT` and `PLANT_PORT`. Leave the round running during recording; ending it reveals survivors as usual.

## Start a game

```bash
./scripts/run_all.sh
```

The script installs locked dependencies, checks configuration, starts the game/plant listeners and the microphone engine, and asks the server to manage its quick tunnel using `--tunnel`. There is only one cloudflared process. A missing Deepgram key fails clearly before services start. Twitch connects when its configuration and saved bot token exist.

Open these URLs using the configured game port:

| Page | Default URL | Use |
| --- | --- | --- |
| Mic | `http://localhost:8100/mic` | Chrome on Windows: allow mic access, select the device and start capture |
| Dock | `http://localhost:8100/dock` | OBS custom browser dock, about 400 px wide |
| Overlay | `http://localhost:8100/overlay` | OBS browser source, 1920×1080 with transparent background |
| Local plant | `http://localhost:8101/` | Local inspection only; viewers use the public tunnel URL |

In OBS, enable **Control audio via OBS** for the overlay source and route/monitor it as needed. The synthesized boom targets a peak near −1 dBFS; balance the source against speech in the OBS mixer. If a normal browser blocks sound, interact with the page to allow audio. Add `?latency=1` to the overlay URL for the small debug latency badge.

Wait for the dock's connection lights, start a round and share the current plant URL/QR. A viewer sends `!mine`, opens the link, picks a card and sends the displayed `!mine CODE` in Twitch chat. Mines arm after 30 seconds. A moderator can use `!defuse`, or the streamer can use the dock's False alarm button, within 10 seconds of a mistaken boom.

The public [quick tunnel](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/) exposes only the plant app. Its URL changes after a tunnel restart; the overlay QR and `!mine` reply update automatically. Stop the script with **Ctrl+C** to shut down the engine, both listeners and the tunnel. A service exiting also stops the other service. Restarting loses the current round.

Override ports in `.env` or exported environment variables; exported values take precedence:

```bash
GAME_PORT=8200 PLANT_PORT=8201 STT_MIC_PORT=8265 ./scripts/run_all.sh
```

## No-key demo

This works from a fresh clone with no `.env`, Twitch tokens, Deepgram key or cloudflared:

```bash
./scripts/run_all.sh --demo
```

Demo mode sets `MINEFIELD_DEBUG=1`, disables Twitch, and starts only the game and local plant listeners. Open the dock and the live overlay, then plant a known word locally:

```bash
curl -fsS -X POST http://localhost:8100/dock/round/start
curl -fsS -X POST http://localhost:8100/dock/debug/plant \
  -H 'Content-Type: application/json' \
  -d '{"owner":"demo-viewer","word":"pineapple"}'
```

Wait 30 seconds for arming, then enter `I could go for some pineapple` in the dock's typed box. The live overlay booms. End the round from the dock to see its reveal. With different ports, replace `8100` in the commands.

For the scripted visual demo, open `http://localhost:8100/overlay?demo=1`. It needs no game state, WebSocket, API key or engine; `&step=N` freezes a numbered step silently. The live overlay and scripted demo are separate browser views. Demo mode's red engine status is expected because no speech engine runs.

## Checks and rehearsal

```bash
uv run pytest                         # offline tests; no browser or credentials
uv run ruff check .
uv run ruff format --check .
uv run playwright install chromium    # once; no --with-deps
uv run pytest -m browser              # explicit Chromium checks
uv run pytest -m live --tb=short       # real Twitch/Deepgram; bot + test tokens and key
uv run python scripts/shoot.py overlay # every scripted step, no running server needed
```

Screenshots go to ignored `data/shots/`. The same screenshot command accepts `dock`, `plant` or `mic` when the server is running; it honors `GAME_PORT` and `PLANT_PORT`.

For rehearsal or recording, enable both private logs with a new timestamp:

```bash
stamp=$(date -u +%Y%m%dT%H%M%SZ)
./scripts/run_all.sh --save-hyps "data/rehearsal-${stamp}-hyps.jsonl" \
  --save-events "data/events/rehearsal-${stamp}-events.jsonl"
```

Use a `recording-` prefix for recording sessions. Hypotheses contain `emitted_wall`; event JSONL contains `received_wall`, `received_utc` and the original event, including the boom’s `at`. Round boundaries are observed transitions; connection-gap markers mean events may be missing. Event files must be new. For raw provider responses, run the engine separately with its `--save-raw` flag. These private logs can contain speech; do not share them publicly. Review the saved hypotheses after rehearsal to diagnose misses/false booms, tune configuration and prune misheard deck words.

If Flux performs badly, stop the launcher and restart with `STT_BACKEND=nova3`. If Deepgram is unreachable, use the dock's typed mode deliberately; there is no automatic fallback. See the [demo-day checklist](docs/demo-day.md) for the final run.
