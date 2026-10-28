# AGENTS.md

Minefield: a Twitch game for the Codex x TwitchCon Hackathon. Viewers plant secret words; when the streamer says one on stream, the overlay explodes and names the viewer who planted it.

**Read `SPEC.md` first.** It is the source of truth for architecture, messages, game rules and the work packages (WP1–WP14). When asked to "do WPn", implement exactly that package and meet its acceptance criteria. If the spec is wrong or unclear, say so and propose a spec change; don't silently diverge.

## Stack
- Python 3.12, managed with `uv`; the package is `minefield/`.
- FastAPI + uvicorn for the server; `httpx` for Helix and Deepgram's REST API; `websockets` for EventSub, Deepgram streaming and the mic page.
- STT: Deepgram streaming over plain `websockets` (no Deepgram SDK). Default model Flux (`flux-general-en`), backup Nova-3; EU endpoint. No local model, no GPU.
- Web: plain HTML/CSS/JS in `web/`. No framework, no bundler, no build step; these pages run as OBS browser sources.
- Sound effects are synthesized at runtime with the WebAudio API; there are no audio files.
- Dev only: Playwright (Chromium) for headless screenshots of the web pages (`scripts/shoot.py`).

## Commands
```
uv sync                                   # install
uv run pytest                             # tests
uv run ruff check . && uv run ruff format .
uv run python -m minefield.server         # game server (127.0.0.1:8000, mic page at /mic) + plant app (:8001)
uv run python -m minefield.stt --mic      # STT engine, live (open http://localhost:8000/mic in Chrome on Windows)
uv run python -m minefield.stt --wav FILE # STT engine on a recording
uv run python -m minefield.harness ...    # accuracy report (see SPEC §7)
uv run python scripts/shoot.py PAGE       # screenshots of overlay/dock/plant/mic into data/shots/
uv run pytest -m live                     # live checks against Twitch and Deepgram (needs .env and data/tokens.json)
```

## Rules
- **Secrecy:** the words of live mines never go to the overlay, the dock, chat, or INFO logs. See SPEC §3.
- **No persistence:** game state lives in memory only. The only runtime state file is `data/tokens.json`; logs and recordings you ask for (`--save-raw`, `--save-hyps`) also go under `data/`. Never commit `data/`, tokens, `.env` or API keys.
- **No STT biasing:** never send mine or deck words to Deepgram (`keyterm`, keywords, prompts). A false boom names a viewer.
- `minefield/core` stays pure (no I/O, no network, no GPU) and fully unit-tested. Put all tunable numbers in `minefield/core/config.py`.
- Twitch and Deepgram: verify endpoints, scopes, parameters and payloads against https://dev.twitch.tv/docs and https://developers.deepgram.com before coding them. Twitch failures (chat send, EventSub) are logged and must never crash or block the game.
- All code, comments, UI text, commit messages and docs you write are in English.
- Assets (images, fonts) must be your own or CC0; record the source in `web/assets/CREDITS.md`. No third-party trademarks. Sounds are synthesized (see Stack), so they need no credits.
- Don't modify `docs/brainstorm/`, `docs/competition/`, or the local `twitch/` folder.

## Twitch accounts
| Role | Login | Token scopes (SPEC §6) |
| --- | --- | --- |
| Broadcaster (owns the channel and the developer app) | `izleyici0808` | none: no markers or clips (D15) |
| Bot (moderator in the broadcaster's channel; sends chat, reads commands) | `minefield_bot` | `user:read:chat`, `user:write:chat` |
| Test viewer (for testing commands alone) | `minefield_test` | `user:write:chat` |

The logins and the app's Client ID are configured in `.env` (`TWITCH_CLIENT_ID`, `TWITCH_BROADCASTER_LOGIN`, `TWITCH_BOT_LOGIN`, `TWITCH_TEST_LOGIN`); resolve user IDs at runtime via Get Users. Do not hard-code them.

## Dependencies and tests
- No ML or GPU dependencies (no torch, no faster-whisper, no onnxruntime).
- `DEEPGRAM_API_KEY` and `DEEPGRAM_REGION` come from `.env`; never log the key.
- Tests that need a microphone, the network or an API key are marked `@pytest.mark.live` and are skipped by default.
- Fake Twitch in unit tests (`respx` or a fake client). Test the Deepgram mapping with recorded messages from `tests/fixtures/deepgram/`. Never call the real APIs from the default test run.
- If you cannot reach dev.twitch.tv, developers.deepgram.com or a package index, say so instead of guessing an API shape.
- Playwright is a dev dependency only. Install the browser with `uv run playwright install chromium`, without `--with-deps`: there is no sudo, and the system libraries Chromium needs are already present (checked on 28 Oct). If Chromium still fails to start, fall back to the Windows Chrome at `/mnt/c/Program Files/Google/Chrome/Application/chrome.exe --headless --screenshot`.

## Workflow
- Tests first: for each WP, write failing tests from its acceptance criteria in SPEC §8, run them, then implement.
- **Verify it yourself before asking the human.** The human's time is the bottleneck; only ask for what you cannot do.
  - Web pages: after a change, run `scripts/shoot.py`, look at the screenshots, and fix what is off before reporting.
  - Twitch and Deepgram: once `data/tokens.json` and `.env` exist, run `uv run pytest -m live` yourself. Live Twitch tests send commands as the test account and check the bot's replies. No live stream is needed.
  - Harness: run `harness run` and `harness replay` yourself on the recordings in `data/recordings/`.
  - Only the human can: complete device-code logins, speak into the mic, use the phone, configure OBS, and judge how it feels. Ask for those explicitly, as a short checklist.
- **Chains:** when asked for several WPs (e.g. "do M1: WP1, WP2, WP4"), do them in order, run tests and lint and commit after each, and stop at the first failure you cannot fix. End with one report covering all of them.
- Small commits, prefixed with the WP id (e.g. `WP5: streaming hypotheses`).
- Before finishing a WP, run tests and lint, and report: what changed, how it was verified, and anything left open.

## Review guidelines
When reviewing a diff or a PR, flag as P0/P1:
- any path where the word of a non-exploded mine can reach the overlay, the dock, chat, INFO logs or a Twitch API call (SPEC §3 secrecy invariant);
- I/O, network or global state in `minefield/core`;
- API keys or tokens in code, logs or committed files;
- mine or deck words sent to Deepgram (no biasing);
- a Twitch or Deepgram failure that can crash the server or block the game loop;
- divergence from SPEC.md without a spec change.
