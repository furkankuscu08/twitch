# AGENTS.md

Minefield: a Twitch game for the Codex x TwitchCon Hackathon. Viewers plant secret words; when the streamer says one on stream, the overlay explodes and names the viewer who planted it.

**Read `SPEC.md` first.** It is the source of truth for architecture, messages, game rules and the work packages (WP1–WP15, without WP6 and WP12). When asked to "do WPn", implement exactly that package and meet its acceptance criteria. If the spec is wrong or unclear, say so and propose a spec change; don't silently diverge. `docs/plan/` contains Turkish planning notes, not implementation requirements; do not modify it for spec work.

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
uv run python -m minefield.server         # game server (127.0.0.1:8100, mic page at /mic) + plant app (:8101)
uv run python -m minefield.stt --mic      # STT engine, live (open http://localhost:8100/mic in Chrome on Windows)
uv run python -m minefield.stt --wav FILE # STT engine on a recording
uv run python scripts/shoot.py PAGE       # screenshots of overlay/dock/plant/mic into data/shots/
uv run pytest -m live                     # live checks against Twitch and Deepgram (needs .env and data/tokens.json)
```

Default ports are `GAME_PORT=8100` and `PLANT_PORT=8101`, overridable by environment variables. Use the configured ports in local URLs and the tunnel target.

## Rules
- **Demo scope:** this is a 4-day hackathon demo. Prefer the simplest design that is also robust and efficient. Robust means a dropped connection, a bad message or a slow client never crashes the server or blocks the game, and it recovers on its own through reconnects and snapshots. Efficient means no needless work on the hot path (audio → hypothesis → matcher → overlay) and nothing that grows without bound. Beyond that, add no abstractions, config options or edge-case handling the spec does not ask for. If something needs more complexity, say so first instead of building it. This also applies to `SPEC.md`: add text only when requested or needed to resolve a real contradiction.
- **Secrecy:** unrevealed mine words never go to the overlay, the dock, chat, Twitch API calls or INFO logs during a round. Only a boom discloses its word during play; round-end `reveal` and the recap disclose duds. Snapshots never contain words. Receipts mask all other deck words. See SPEC §3-4.
- **No persistence:** game state lives in memory only. The only runtime state file is `data/tokens.json`; requested engine logs (`--save-raw`, `--save-hyps`) also go under `data/`, and requested private event logs go under `data/events/`. Never commit `data/`, tokens, `.env` or API keys.
- **No STT biasing:** never send mine or deck words to Deepgram (`keyterm`, keywords, prompts). A false boom names a viewer.
- `minefield/core` stays pure (no I/O, no network, no GPU, no clock reads or mutable process-global game state) and fully unit-tested. Put all tunable numbers and defaults in `minefield/core/config.py`; entrypoints outside `core` read env overrides and inject validated config and explicit times. Overlay-only presentation constants, including `BANNER_FULL_S`, live in `web/overlay`.
- Twitch and Deepgram: verify endpoints, scopes, parameters and payloads against https://dev.twitch.tv/docs and https://developers.deepgram.com before coding them. Dated claims in SPEC are verification inputs, not proof of current API behavior. Record the official source URL and verification date in implementation comments. Twitch failures (chat send, EventSub) are logged without private words or credentials and must never crash or block the game.
- All code, comments, UI text, commit messages and docs you write are in English.
- Assets (images, fonts) must be your own or CC0; record the source in `web/assets/CREDITS.md`. No third-party trademarks. Sounds are synthesized (see Stack), so they need no credits.
- Don't modify `docs/brainstorm/`, `docs/competition/`, or the local `twitch/` folder.

## Twitch accounts
| Role | Login | Token scopes (SPEC §6) |
| --- | --- | --- |
| Broadcaster (owns the channel and the developer app) | `izleyici0808` | none: no markers or clips (D15) |
| Bot (moderator in the broadcaster's channel; sends chat, reads commands) | `minefield_bot` | `user:read:chat`, `user:write:chat` |
| Test viewer (for testing commands alone) | `minefield_test` | `user:write:chat` |
| Blind-plant viewers | `pixelmoth01`, `mossy_otter` | `user:write:chat` |

The logins and the app's Client ID are configured in `.env` (`TWITCH_CLIENT_ID`, `TWITCH_BROADCASTER_LOGIN`, `TWITCH_BOT_LOGIN`, `TWITCH_TEST_LOGIN`, `TWITCH_TEST2_LOGIN`, `TWITCH_TEST3_LOGIN`); resolve user IDs at runtime via Get Users. Do not hard-code them. The blind-plant viewers use auth aliases `test2` and `test3` respectively.

The test viewer is optional for normal play and required for WP9-WP11's automated live acceptance checks. The blind-plant viewers, together with the test viewer, plant mines for the recording when no friends join: the words are picked at random and never shown to the streamer.

Before each rehearsal and recording, refresh all three viewer tokens with `uv run python -m minefield.twitch_api.auth --account ACCOUNT --refresh` (`test`, `test2`, `test3`), before starting the server. Give device codes to the human for activation in their own incognito Chrome; never open activation in the agent's broadcaster browser. Blind planting is one-shot; never show its selected words in tool output or messages.

## Dependencies and tests
- No ML or GPU dependencies (no torch, no faster-whisper, no onnxruntime).
- `wordfreq` is a dev dependency only: deck validation rejects words in its top 1,000 English words. Keep frequency checks off the game and audio hot paths.
- `DEEPGRAM_API_KEY` and `DEEPGRAM_REGION` come from `.env`; never log the key.
- Tests that need a microphone, the network or an API key are marked `@pytest.mark.live` and are skipped by default.
- Playwright tests are marked `@pytest.mark.browser` and skipped by default; run them explicitly with `uv run pytest -m browser`.
- Fake Twitch in unit tests (`respx` or a fake client). Test the Deepgram mapping with recorded messages from `tests/fixtures/deepgram/`. Never call the real APIs from the default test run.
- If you cannot reach dev.twitch.tv, developers.deepgram.com or a package index, say so instead of guessing an API shape.
- Playwright is a dev dependency only. Install the browser with `uv run playwright install chromium`, without `--with-deps`: there is no sudo, and the system libraries Chromium needs are already present (checked on 28 Oct). If Chromium still fails to start, fall back to the Windows Chrome at `/mnt/c/Program Files/Google/Chrome/Application/chrome.exe --headless --screenshot`.

## Workflow
- Tests first: for each WP, write failing tests from its acceptance criteria in SPEC §7, run them, then implement.
- **Verify it yourself before asking the human.** The human's time is the bottleneck; only ask for what you cannot do.
  - Web pages: after a change, run `scripts/shoot.py`, look at the screenshots, and fix what is off before reporting.
  - Twitch and Deepgram: once `data/tokens.json` and `.env` exist, run `uv run pytest -m live` yourself. Live Twitch tests send commands as the test account and check the bot's replies. No live stream is needed.
  - After rehearsal: read saved hypotheses to diagnose missed words and false booms, tune config and prune misheard deck words.
  - Only the human can: complete device-code logins, speak into the mic, use the phone, configure OBS, and judge how it feels. Ask for those explicitly, as a short checklist.
- **Chains:** when asked for several WPs (e.g. "do M1: WP1, WP2, WP4"), do them in order, run tests and lint and commit after each, and stop at the first failure you cannot fix. End with one report covering all of them.
- Small commits, prefixed with the WP id (e.g. `WP5: streaming hypotheses`).
- Before finishing a WP, run tests and lint, and report: what changed, how it was verified, and anything left open.

## Review guidelines
When reviewing a diff or a PR, flag as P0/P1:
- any path where an unrevealed mine word can reach the overlay, the dock, chat, INFO logs or a Twitch API call outside the explicit boom and round-end disclosure rules (SPEC §3; snapshots never contain words);
- I/O, network or global state in `minefield/core`;
- API keys or tokens in code, logs or committed files;
- mine or deck words sent to Deepgram (no biasing);
- a Twitch or Deepgram failure that can crash the server or block the game loop;
- divergence from SPEC.md without a spec change.
