# Minefield: technical spec

> Chat plants secret words. Say one on stream, it explodes.

Viewers secretly pick a word from a deck and plant it as a "mine". The streamer talks as usual. Streaming speech recognition (Deepgram) listens to the streamer's mic; when the streamer says a live mine word, the overlay explodes and names the viewer who planted it.

This file is the source of truth for the build. Work packages (WP1–WP14, without WP6 and WP12) and their acceptance criteria are in §7. The project plan (schedule, decisions; Turkish) is in `docs/plan/minefield.md`.

---

## 1. Components

```
[Windows]  mic ──► mic page (Chrome tab, http://localhost:8100/mic)
                      │  16 kHz mono int16 PCM over WebSocket
                      ▼
[WSL]      STT engine (minefield.stt) ──80 ms chunks──► Deepgram streaming STT (EU endpoint)
                      │                ◄──interim results with word timings──┘
                      │  hypotheses (HTTP POST)
                      ▼
[WSL]      game server (minefield.server, FastAPI, 127.0.0.1:8100)
              ├── matcher + game state (minefield.core)
              ├── /overlay  (OBS browser source, WebSocket)
              ├── /dock     (OBS custom dock, WebSocket + POST)
              ├── /mic      (mic page, opened in Chrome on Windows)
              └── Twitch    (EventSub WebSocket chat, Helix: chat message)
           plant app (same process, 127.0.0.1:8101) ◄── cloudflared quick tunnel (in WSL) ◄── viewers' phones
```

Ports default to `GAME_PORT=8100` and `PLANT_PORT=8101`; both can be overridden by environment variables. Local URLs and the tunnel target use the configured ports.

- **mic page** (`web/mic`; Windows Chrome, because WSL2 has no reliable mic access):
  - Served by the game server, opened in a normal Chrome tab on Windows (`localhost` counts as a secure context, so `getUserMedia` works). Not an OBS dock: OBS docks do not grant mic access reliably.
  - Device picker (remembered in `localStorage`), level meter, connection state.
  - `getUserMedia` with `echoCancellation`, `noiseSuppression` and `autoGainControl` off. An AudioWorklet resamples to 16 kHz mono int16 and sends 20 ms frames.
  - Reconnects automatically when the engine restarts.
- **STT engine**: a separate process, so a stalled network call never blocks the server.
  - It reads audio from the mic page or from a WAV file (`--wav`, sent at real-time pace; optional for development).
  - It streams the audio to Deepgram and turns Deepgram's messages into hypotheses (§5). Backends: `flux` (default) and `nova3`, same API key.
  - There is no local model, no GPU work and no VAD of our own.
- **game server**: holds game state in memory. Only Twitch tokens and explicitly requested private engine/event logs are persisted under `data/`.
  - The engine sends a heartbeat every 2 s. If none arrives for `ENGINE_TIMEOUT_S`, or the heartbeat says Deepgram is disconnected, the dock shows a red light.
  - The server never falls back silently to typed mode.
- **plant app**: the only thing exposed to the internet. It serves the plant page and its API, and nothing else. It binds to 127.0.0.1 because cloudflared runs in WSL too.

Fallbacks (decision D3 in the plan): if one Deepgram model performs badly, switch the backend (`--backend nova3`) or the model name; the API key stays the same. If Deepgram is unreachable, the streamer uses typed mode from the dock. There is no local STT fallback.

---

## 2. Repository layout

```
AGENTS.md  SPEC.md  README.md  pyproject.toml
minefield/
  core/        pure logic, no I/O: normalize, deck, game state, matcher
  stt/         engine: audio input (mic page WS, WAV), Deepgram client, backends (flux, nova3), hypothesis mapping, CLI
  server/      FastAPI app, WebSocket hub, dock/overlay/mic routes, plant app
  twitch_api/  auth (device code flow), EventSub client, Helix calls
scripts/run_all.sh   server + engine + cloudflared in one command
scripts/shoot.py     dev only: headless screenshots (Playwright) of overlay, dock, plant and mic pages into data/shots/
web/overlay/  web/dock/  web/mic/  web/plant/  web/assets/   plain HTML/CSS/JS, no build step
deck/en.json
tests/         tests/fixtures/deepgram/: recorded Deepgram messages (JSONL) for unit tests
data/          gitignored: tokens, raw Deepgram logs, hypothesis logs
```

Do not create a top-level `twitch/` package; that path is an unrelated local folder.

---

## 3. Game rules

### Round
- The streamer starts a round from the dock. Mines can be planted only during a round.
- Ending the round stops detection and planting, closes pending matcher candidates, reveals the duds and the stats, then clears the round's game state. Twitch tokens and connection health are not round state.
- The overlay keeps the received reveal on screen until the next round starts. This is browser display state only; the server does not retain the ended round for snapshots. An idle snapshot must not erase a reveal already displayed by that overlay, but a fresh page cannot recover it after the server has cleared it.
- Round start broadcasts a snapshot showing the new running round; the overlay clears its retained reveal on that snapshot.

### Planting (decision D4)
1. A viewer types `!mine`. The bot replies: `@{user} pick your mine: {plant_url}`. The overlay also shows a short plant URL and a QR code in a corner while a round is running.
2. The plant page shows a **hand of 6 random cards drawn from the whole deck**. Hands never exclude live words; excluding them would let anyone find the live mines by requesting many hands.
3. The viewer taps a card. The page shows the full command `!mine K7QF` with a **Copy** button.
   - The code has 4 characters (alphabet without 0/O/1/I) and is valid for `CODE_TTL_S` (300 s).
   - The code does not reveal the word.
   - Codes are anonymous bearer codes: the first successful redemption binds the word to that chatter. No viewer login is required. Consume a code only after a successful bind; rejected attempts do not consume it. Codes and hands belong to the current round and are invalidated at round end, even if their TTL has not elapsed. Allocate codes uniquely among pending codes.
4. The viewer types `!mine K7QF`. The server binds the word to the chatter and replies: `@{user} mine planted 💣 arming…`.
   - Parsing is lenient: case-insensitive, extra spaces allowed (`!Mine  k7qf`).

Planting rejects with a short reply:
- the user already has a live mine;
- `MAX_MINES` (4) mines are already live;
- the code is unknown or expired;
- the word is already live ("taken, pick another"). This is checked at bind time.

Both apps and Twitch commands share one asyncio process/event loop. Bind-time validation, code consumption and mine creation run in one synchronous function with no `await` between them; no planting locks are needed. Concurrent requests must not bypass the live-mine, owner or word limits. Rejection replies never include the selected word.

**Live mine:** status `arming`, `armed` or `sparking`. `MAX_MINES` and "one live mine per user" count only live mines. An exploded mine is no longer live, so its owner may plant again right away.

### Lifecycle
`arming` (`ARM_DELAY_S` = 30 s) → `armed` → `sparking` → back to `armed` (fizzle), or `exploded`. An exploded mine may later be marked `false_alarm`.

At round end, every mine that never exploded becomes a `dud`.

### Detection
See §5. Only `armed` mines can trigger. Eligibility uses the spoken occurrence's start time, not the time its hypothesis arrives: it must be at or after both the current round's start and the mine's `arms_at`. Ignore hypotheses while no round is running and occurrences from before the current round; delayed speech from an earlier round cannot trigger a new round's mines.

### Boom
1. Show the overlay explosion and a banner: `{OWNER}'S MINE: {WORD}`, `planted {n} min ago`, and the **receipt** (below).
2. Post `💥 @{owner}'s mine {WORD} went off!` immediately.

**Receipt:** the streamer's own words that set the mine off, e.g. *"…honestly I could go for some **pineapple**"*.
- The last `RECEIPT_WORDS` (8) words of the triggering hypothesis, ending with the boom word (or its multi-word variant), which is highlighted. Words after it are not shown.
- In typed mode, the same window is taken from the typed text.
- **Masking:** every other word in the window that matches any deck word or variant (after normalization, §5) is replaced by `•••`, whether or not it is a live mine. A fizzled mine's word must never leak through a receipt.
- Built in `core` (pure) and unit-tested.

**False alarm** corrects speech-recognition errors; it is not a way for the streamer to escape.
- Who: `!defuse` from a mod or the broadcaster, or the dock's "False alarm" button.
- When: within `FALSE_ALARM_WINDOW_S` (10 s) of the boom.
- Target: the latest boom in the active round that is still within that window and has not already been corrected. Both `!defuse` and the dock button use this rule; no mine ID selector is needed. With no eligible boom, there is no state change.
- Effect: the mine becomes `false_alarm` and does not count in the stats. The overlay shows a "FALSE ALARM" stamp, and the bot posts `🧯 False alarm, @{owner} gets a free re-plant`.

### Round end
- The overlay reveals the duds (`{owner}'s mine {WORD} never went off`) and the number of booms.
- The bot posts **one recap message**: `Round over: {n} booms. 💥 @a (pineapple), @b (volcano). Survived: @c's "banana".`
  - False alarms are not listed. With no booms: `Round over: no booms.` followed by the survivors.
  - At most `CHAT_MAX_CHARS` (500, the Send Chat Message limit); if longer, drop list entries from the end and add `…`.
  - The text is built in `core` (pure) and unit-tested.

**Secrecy invariant:** while a round is running, the words of mines that have not exploded must never reach the overlay, the dock, logs at INFO level, chat or a Twitch API call. A boom makes only that mine's word public; a later false-alarm correction does not make it secret again. At round end, dud words may be disclosed in `reveal` and the single chat recap, as required above. These are the only game-output disclosure exceptions. Receipts mask every other deck word, even one already public. The plant page may show its viewer their own hand; private server-side hand/code mappings and game state may hold those words. Live game recognition hypotheses are private engine/server inputs and must not be broadcast as a public transcript. Do not log live mine words through request bodies, state dumps or exception messages.

---

## 4. Messages and endpoints

### Mic page → engine
WebSocket `ws://localhost:8765/audio` (served by the engine; the page itself is served by the game server at `/mic`).
- First message (JSON): `{"type":"hello","sample_rate":16000,"client_start_wall":<unix float>}`.
- Then binary frames of int16 PCM.
- **Clock:** the engine timestamps audio with **its own clock**: the time `hello` arrived plus samples received ÷ 16000. `client_start_wall` is for logs only, because the Windows and WSL clocks can drift apart (for example after sleep).
- Only one mic client at a time; a new connection replaces the old one.

### Engine → server
`POST /stt/hypothesis`:
```json
{"utt_id": "u42", "seq": 3, "final": false,
 "words": [{"text": "pineapple", "start": 1.20, "end": 1.71, "prob": 0.93}],
 "utt_start_wall": 1730000000.12, "emitted_wall": 1730000003.40,
 "lag_ms": 310}
```
- `start`/`end` are seconds from `utt_start_wall`.
- `utt_id` is globally unique across Deepgram reconnects and engine process restarts. Include a fresh per-process identifier in the session prefix; a counter that resets on process restart is insufficient.
- `seq` strictly increases within an utterance. The engine delivers hypotheses in order. Duplicate or out-of-order hypotheses (`seq` no greater than the last accepted value) are ignored and cannot count toward confirmation. A finalized or aborted utterance cannot be reopened by a late request.
- `final: true` is sent once, when the utterance ends.
- `lag_ms`: `emitted_wall − (stream_start_wall + audio_window_end)`, i.e. network plus Deepgram processing time (§5).
- Engine and server run on the same WSL clock.
- `POST /stt/status` (heartbeat every 2 s): `{"ok": true, "backend": "flux", "deepgram": "connected", "mic": "connected", "lag_ms_p95": 420, "reconnects": 0}`.
- `POST /stt/abort {"utt_id": "u42"}`: discard the named open utterance and fizzle its pending candidates without confirming them. This control message is not a hypothesis and does not increment confirmation counts. Repeated aborts are harmless. The engine sends it when a Deepgram connection drops or an audio source is replaced. If the engine cannot send it, the server performs the same cleanup on a disconnected heartbeat or engine timeout. A replacement utterance also closes any candidates left open by the preceding utterance from that engine. The pure matcher receives an explicit cleanup call; it never reads the clock or network itself.

### Server → overlay/dock
WebSocket `/ws/overlay` and `/ws/dock`. JSON messages with a `type` field:

| type | payload | overlay | dock |
| --- | --- | --- | --- |
| `snapshot` | `round`, `plant_url`, `mines:[{id, owner, status, arms_in_s}]` | ✓ | ✓ |
| `mine_planted` | `id, owner, arms_in_s` | ✓ | ✓ |
| `mine_armed` | `id` | ✓ | ✓ |
| `spark` | `id` | ✓ | ✓ |
| `fizzle` | `id` | ✓ | ✓ |
| `boom` | `id, owner, word, planted_ago_s, latency_ms, source, at, receipt` | ✓ | ✓ |
| `false_alarm` | `id, owner` | ✓ | ✓ |
| `reveal` | `duds:[{owner, word}], stats` | ✓ | ✓ |
| `status` | `mic, engine, deepgram, eventsub, tunnel_url` | — | ✓ |

`word` appears only in `boom` and `reveal`; snapshots never contain words. `arms_in_s` is the seconds remaining until arming, clamped to zero. A reloaded overlay restores chips with their status without replaying banners or sounds. Snapshots retain live mines and recent inactive mines through the false-alarm window. Older inactive records are discarded; uncorrected booms are compacted into a total and a recap prefix bounded by `CHAT_MAX_CHARS`. `at` is the boom's server-clock Unix time; the server remains authoritative for the false-alarm deadline.

`source` is `stt` or `typed`. `receipt` is a list of `{"text": str, "hit": bool}` (masked as in §3; exactly one item has `hit: true`; a multi-word variant is one item). The dock receives a current `status` message when it connects as well as subsequent health updates.

Each overlay/dock WebSocket client has a queue of at most `WS_CLIENT_QUEUE_SIZE` (100) messages. If the queue fills, drop that client without blocking broadcast to others. The browser reconnects automatically and receives a fresh snapshot. Reject malformed messages at the input boundary without crashing the server or advancing game state.

The overlay may show `latency_ms` as a small debug badge, enabled by `?latency=1`; it is used in the demo video.

### Dock → server
`POST /dock/round/start`, `/dock/round/end`, `/dock/false-alarm` (enabled for `FALSE_ALARM_WINDOW_S` after a `boom`), `/dock/typed {"text": "..."}`.

Debug only, behind `MINEFIELD_DEBUG=1`: `/dock/debug/plant {"owner","word"}`.

### Plant app (default port 8101)
- `GET /`: the page.
- `GET /api/hand` → `{"hand_id","cards":[6 words]}`.
- `POST /api/pick {"hand_id","word"}` → `{"code","command","expires_at"}`. `word` must be in that hand.

No rate limiting (demo scope). If it is ever added, read the client IP from `CF-Connecting-IP`: through the tunnel every request arrives from cloudflared on localhost. No other routes on this app.

The demo accepts that repeated bind attempts and "taken" replies can reveal which words are live; anonymous bearer codes and the existing replies remain in scope. Do not add viewer authentication or anti-probing infrastructure. Pending hands expire after `CODE_TTL_S`, as do codes. Remove expired entries before allocating new ones, and cap the combined number of pending hands and codes at `MAX_PENDING_PLANTS` (1,000); reject new allocations with a short capacity error until room is available. This storage cap is not per-client rate limiting. Clear both collections at round end.

---

## 5. Speech pipeline

### Engine (`minefield.stt`)
Verify every URL, parameter and message field below against https://developers.deepgram.com before coding, and note the verified details in code comments. Talk to Deepgram over plain `websockets` (no Deepgram SDK; its API changed a lot between major versions).

- **Connection:** API key from `DEEPGRAM_API_KEY` (`.env`), header `Authorization: Token <key>`. Region from `DEEPGRAM_REGION`: `eu` → `api.eu.deepgram.com` (default), `us` → `api.deepgram.com`.
- **Audio:** the engine joins 20 ms frames into 80 ms binary messages (2,560 bytes of 16 kHz int16), the chunk size Deepgram recommends. `--wav` sends the same chunks at real-time pace. On shutdown send `{"type":"CloseStream"}`.
- **No biasing:** no `keyterm`, no keywords, no prompt. A false boom names a viewer, so it is worse than a miss.
- **Backend `flux` (default):** `wss://<host>/v2/listen?model=flux-general-en&encoding=linear16&sample_rate=16000&mip_opt_out=true`. Keep Deepgram's default end-of-turn settings; do not use `eager_eot_threshold`.
  - A Flux turn is one utterance: `utt_id = f"{engine_id}-s{session}-t{turn_index}"`, where `engine_id` is fresh on every process start. Nova-3 uses the same process/session uniqueness requirement.
  - Each `Update` with a non-empty `words` list → a hypothesis with `final: false`. Updates without words are **not** sent (they would count as the "next" hypothesis and cause a fizzle).
  - `EndOfTurn` → the same words with `final: true`.
  - Word fields: `word` → `text`, `confidence` → `prob`, `start`/`end` converted to seconds from `utt_start_wall`.
- **Backend `nova3`:** `wss://<host>/v1/listen?model=nova-3&language=en&encoding=linear16&sample_rate=16000&interim_results=true&punctuate=false&smart_format=false&endpointing=300&utterance_end_ms=1000&vad_events=true&mip_opt_out=true`.
  - Hypothesis = the utterance's `is_final` words so far + the words of the latest interim result.
  - The utterance ends on `speech_final: true` or `UtteranceEnd`; send that last hypothesis with `final: true`.
- **Clock:** `stream_start_wall` is the engine-clock time of the first sample sent on the current Deepgram connection. Deepgram's times are offsets in the audio sent on that connection. Check on the first raw log whether word times are relative to the stream or to the turn, and convert accordingly. `utt_start_wall = stream_start_wall + turn start`.
- **Audio continuity:** after an audio-source interruption or a gap that breaks PCM continuity (disconnect, replacement, pause/resume or dropped audio), abort the open utterance and reset the Deepgram session before forwarding resumed audio. Reanchor its clock to the first resumed sample on the engine's clock. The initial `hello` clock anchor is valid only for uninterrupted mic audio; do not carry it across a gap, insert silence to fill the gap or replay a buffered backlog. Ordinary recorded silence remains PCM audio, not a gap.
- **Reconnect:** on a dropped connection, reconnect with exponential backoff (0.5 s → 8 s), `session += 1`. The open utterance is discarded via `/stt/abort` (§4), not a synthetic `final` that could cause a boom. Audio that arrives while disconnected is dropped. If the mic page sends nothing, send Deepgram's `KeepAlive` message so the connection stays open, subject to verification for the selected backend as required above.
- **Logs:** `scripts/run_all.sh --save-hyps FILE --save-events FILE` enables hypothesis logging and a separate overlay-event recorder with wall-clock timestamps, round boundaries and connection-gap markers under `data/events/`. Event files are private, never printed as transcripts, and cannot recover events missed during a disconnect. `--save-raw FILE` writes every Deepgram message with its receive time (JSONL). `--save-hyps FILE` writes every emitted hypothesis (JSONL). After rehearsal, inspect the saved hypotheses to diagnose missed words and false booms and tune config. Small anonymized raw logs go to `tests/fixtures/deepgram/` so the mapping is unit-tested without the network.

### Matcher (`minefield.core`, pure)
Input: the ordered, deduplicated hypothesis stream above plus the armed mines, explicit times and utterance cleanup calls. Output: `spark`, `fizzle` and `boom` events. A pending candidate remains eligible for confirmation while its mine is `sparking`; the armed-only rule prevents opening candidates for an `arming`, exploded or otherwise inactive mine.

1. **Normalize** each word: lowercase, NFKC, strip punctuation, then map through the deck's variants (e.g. `pineapples`, `pine apple` → `pineapple`). Multi-word variants are matched on adjacent words. Their confidence is the minimum constituent `prob`; their start/end span the first through last constituent. Reject deck entries whose normalized canonical forms or variants produce identical or overlapping matches for different canonical words; do not resolve ambiguous matches through precedence.
2. **Occurrences:** within an utterance, the n-th occurrence of a mine word is one occurrence. Identity is (word, n), not the timestamp; word timestamps at the end of a growing transcript can shift between hypotheses. An occurrence is *present* in a hypothesis only if its `prob ≥ MIN_WORD_PROB`; n counts every occurrence regardless of prob.
3. **Spark:** an occurrence of an armed mine's word is present for the first time in hypothesis `k` → open a candidate and emit `spark`.
4. **Boom:** the occurrence is present in `CONFIRM_N` (2) consecutive **received** hypotheses, counting hypothesis `k` → `boom`. Hypotheses the engine did not send (e.g. empty Flux updates) do not count.
   - Secondary sanity check: `|start − candidate.start| ≤ AGREE_TOL_S` (0.5).
   - If this check fails, fizzle the old candidate and treat the occurrence as newly observed in the current hypothesis under the normal spark/final-only rules. Do not retain the old confirmation count.
5. **Fizzle:** a received hypothesis before confirmation does not contain it → `fizzle`; close the candidate.
6. **Final-only words:** an occurrence that appears for the first time in a `final` hypothesis (very short utterance) → boom only if it meets both `MIN_WORD_PROB` and `FINAL_SOLO_MIN_PROB` (0.7). Below `MIN_WORD_PROB` it is absent; otherwise, if below the final-only threshold, emit spark followed by fizzle.
7. A mine booms at most once per utterance.
8. **Latency:** `now_wall − (utt_start_wall + word.end)`. Include it in the `boom` event and in logs.

After processing a final hypothesis, fizzle any candidates that remain unconfirmed and close the utterance. An abort or round end also clears pending candidates without counting as a confirmation hypothesis. Cleanup cannot undo an already emitted boom.

Flux sends an update about every 0.25 s, so `CONFIRM_N = 2` confirms about 0.25 s after a word first appears. If the rehearsal logs show too many false confirmations, raise it to 3.

**Typed mode:** `/dock/typed` text is treated as `CONFIRM_N` identical hypotheses of a synthetic utterance, with confidence 1 and occurrence times equal to submission time. That means an immediate boom for eligible mines, marked `source: "typed"`.

All runtime tunable numbers and their defaults live in one config module (`minefield/core/config.py`) and can be overridden by env vars. Entrypoints outside `core` read the environment and inject a validated config into pure logic. Core modules must not read environment variables, call a clock, or keep mutable process-global game state; callers supply config, time and state explicitly.

---

## 6. Twitch

Verify every endpoint, scope and payload against https://dev.twitch.tv/docs before implementing. Note the verified details in code comments.

- **App:** Public client; **device code flow** (no redirect URI is used, though the console form may require one; `http://localhost:3000` is fine).
  - Tokens are stored in `data/tokens.json` and refreshed on 401.
  - Public-client refresh tokens are single-use and expire after 30 days: always store the new refresh token returned by a refresh.
  - Serialize refreshes per account so simultaneous 401 responses cannot reuse a refresh token. Store the replacement token pair atomically; never log either token.
  - Scopes:
    - Bot (a mod in the channel): `user:read:chat`, `user:write:chat`.
    - Test account and two optional blind-plant viewers: `user:write:chat`. The original test account remains required for WP9-WP11's live checks; all three can plant for the recording.
    - The broadcaster needs no token: there are no markers or clips (decision D15), and the bot reads and sends chat with its own user access token. Checked on 29 Oct: `channel.chat.message` with a user access token "requires `user:read:chat` scope from the chatting user"; Send Chat Message requires "a user access token that includes the `user:write:chat` scope"; `channel:bot` from the broadcaster is needed only with an app access token. Messages are limited to 500 characters.
- **EventSub WebSocket:** `channel.chat.message` v1, condition `{broadcaster_user_id, user_id: bot}`.
  - Subscribe within 10 s of `session_welcome`.
  - On `session_reconnect`: connect to the given `reconnect_url` and close the old socket only after the new welcome. Subscriptions carry over, so do **not** resubscribe.
  - On keepalive timeout or a dropped connection: open a fresh connection and resubscribe. Subscriptions of a lost session are disabled, and missed events are not replayed.
- **Commands:** parsed case-insensitively; messages from the bot itself are ignored.
  - `!mine`, `!mine CODE`;
  - `!defuse` (badges: broadcaster or moderator).
- **Send Chat Message:** `POST /helix/chat/messages` as the bot. Each outgoing chat message gets one attempt with a total `CHAT_SEND_TIMEOUT_S` (5 s) timeout, including any authentication recovery; never retry that message after a failure or timeout. Log `is_sent` / `drop_reason` when returned. Token refresh still recovers authentication for subsequent messages.
- **Blind-plant recording fallback:** `scripts/blind_plant.py` makes one attempt per configured test account in an existing round. Each independently waits a random delay within `BLIND_PLANT_WINDOW_S` (60 s), fetches a hand from the plant API, picks a random card and sends `!mine CODE` through Send Chat Message using that viewer's token. One shared dock WebSocket confirms all accounts by owner within `BLIND_PLANT_CONFIRM_TIMEOUT_S` (10 s) after sending. Existing planting limits apply; failures skip only that account, with no retries or automatic replants. Words stay in memory and never enter output or files; output contains only owners and success/failure, except credential warnings include the exact per-account refresh command. The helper only reads tokens; refresh all three test tokens before each rehearsal and recording. Device-code activation is done by the human in their own incognito browser, never the agent's broadcaster browser.
- **Not used:** stream markers and clips (cut in D15: they only work on a live stream and added little to the demo). The streamer's native Clip button still works.
- Chat sends and EventSub recovery run outside game-state mutations with finite I/O timeouts. Pending external work must not grow without bound or let a stalled service block the game. Chat send failures are logged without private words or credentials and never block the game; sends are best effort with the one-attempt policy above. WebSocket client overflow disconnects only that client, as specified in §4.

---

## 7. Work packages and acceptance

Each WP is done when its acceptance criteria pass and `uv run pytest` and `uv run ruff check` are clean.

| WP | Scope | Acceptance |
| --- | --- | --- |
| WP1 | `core`: config, normalize, deck loader, game state machine, matcher | Unit tests cover: spark→boom with `CONFIRM_N` 2 and 3; spark→fizzle; cleanup of unconfirmed candidates on final, abort and round end; a word below `MIN_WORD_PROB` is not present; occurrence identity with shifted timestamps and candidate restart outside tolerance; final-solo requiring both confidence floors; multi-word minimum confidence and rejection of ambiguous variants; eligibility by speech time after arming and round start; live-mine definition; max mines; one live mine per user; latest eligible false alarm accepted only within the window, excluded from stats; receipt window, highlight and masking of other deck words (including a fizzled live mine's word); round recap text, false alarms excluded, truncated to `CHAT_MAX_CHARS`; hand drawn from the whole deck and taken word rejected at bind; secrecy (no unrevealed mine word in public output; snapshots never contain words) |
| WP2 | `server`: app, WS hub, dock routes, typed mode, debug plant, engine heartbeat timeout | With `MINEFIELD_DEBUG=1`: plant via the debug route, wait for arming, type a sentence → `boom` reaches a test WS client. Tests also cover duplicate/out-of-order hypotheses not confirming a boom; abort/disconnect/timeout cleanup; synchronous no-await planting without locks; reconnect snapshots restoring chips/status and remaining arming seconds without words or banner replay; a full 100-message client queue disconnecting only that client; malformed input leaving the server running |
| WP3 | `web/overlay`: chips, arming ring, spark, fizzle, boom (shake + banner with receipt + sfx), static "FALSE ALARM" stamp, reveal, plant URL + QR, latency badge; `scripts/shoot.py` | 1920×1080 transparent; renders every §4 message; keeps a received reveal displayed until the next round starts even after the server clears its state; the demo page `/overlay?demo=1` replays a scripted sequence and `&step=N` freezes it at step N; sfx are synthesized with WebAudio (no audio files); `scripts/shoot.py overlay` saves one PNG per step and the boom banner is readable in it |
| WP4 | `web/dock`: round controls, status lights, mine list without words, "False alarm" button (enabled for 10 s after a boom), typed box | Works as an OBS custom browser dock at 400 px width; `scripts/shoot.py dock` renders it at 400 px without overflow |
| WP5 | `web/mic` page + `stt` engine: Deepgram client, `flux` and `nova3` backends, reconnect, heartbeat, CLI (`--mic` / `--wav` / `--backend` / `--save-raw` / `--save-hyps`) | Unit tests map recorded Flux and Nova-3 messages (`tests/fixtures/deepgram/`) to the expected hypotheses, including empty updates, a dropped connection with explicit abort, session/clock reset after interrupted audio, and utterance IDs unique across engine restarts; speaking into the mic page produces hypotheses about every 0.25 s with `flux`; the mic page reconnects after an engine restart; the engine reconnects after the Deepgram socket is killed; the heartbeat shows backend, connection state and lag |
| WP7 | `deck/en.json`: ~120 concrete, funny, everyday-but-not-too-common nouns with variants | Static checks only: no brands, offensive words, homophone pairs or ambiguous normalized variants; use `wordfreq` as a dev dependency and reject canonical words or variants in its top 1,000 English words, with the package version pinned by the uv lockfile. Frequency filtering runs during deck validation, never on the runtime hot path. Later, prune misheard words from the rehearsal log |
| WP8 | `twitch_api.auth`: device code flow CLI per account, token store, refresh | `python -m minefield.twitch_api.auth --account bot` stores a working token |
| WP9 | EventSub client + commands + chat send | Unit tests with a fake client; a `live` test sends `!mine` and `!mine CODE` as the test account through Send Chat Message, and the server's state changes and the bot's replies report `is_sent`; reconnect works |
| WP10 | boom message, false-alarm message, round recap message | With a fake Twitch client: a boom posts the boom message, a false alarm within 10 s corrects the latest eligible boom and posts the false-alarm message, round end posts one recap message; a failed or timed-out send gets no retry, is logged, and the game continues. Each chat send has a 5 s total timeout. A `live` test does the same on the real channel (no live stream needed) |
| WP11 | `web/plant` + plant app + code binding + tunnel helper | Unit tests cover anonymous bearer codes consumed only on successful bind, hand/code TTL and round-end invalidation, and rejection at the combined pending-storage cap. `scripts/shoot.py plant` renders the page at 390 px phone width; a `live` test drives hand → pick → `!mine CODE` as the test account through the tunnel URL; then the human repeats it once from a phone (T4) |
| WP13 | Polish and rehearsal fixes | Two uninterrupted rounds (typed mode + debug plant, or with a friend) |
| WP14 | Ops: `scripts/run_all.sh` (server + engine + cloudflared; fails clearly if `DEEPGRAM_API_KEY` is missing), English README (setup, Deepgram key, Twitch app registration, how to open the mic page, no-key demo path: typed mode + debug plant (`MINEFIELD_DEBUG=1`) + `/overlay?demo=1`), demo-day checklist | A fresh clone on the same machine starts with one script plus the mic page in Chrome; the no-key demo path works without the STT engine |

Order and milestones:
- **M0:** WP7, WP8;
- **M1:** WP1–WP4 (WP3 basic);
- **M2:** WP5;
- **M3:** WP9, WP10;
- **M4:** WP11 (WP12, the chat simulator, was removed);
- **M5:** WP3 full, WP13, WP14.

---

## 8. Config defaults

| Name | Default |
| --- | --- |
| `GAME_PORT` | 8100 |
| `PLANT_PORT` | 8101 |
| `STT_BACKEND` | `flux` |
| `DEEPGRAM_REGION` | `eu` |
| `CONFIRM_N` | 2 |
| `MIN_WORD_PROB` | 0.6 |
| `AGREE_TOL_S` | 0.5 |
| `FINAL_SOLO_MIN_PROB` | 0.7 |
| `ARM_DELAY_S` | 30 |
| `MAX_MINES` | 4 |
| `HAND_SIZE` | 6 |
| `CODE_TTL_S` | 300 |
| `FALSE_ALARM_WINDOW_S` | 10 |
| `RECEIPT_WORDS` | 8 |
| `CHAT_MAX_CHARS` | 500 |
| `ENGINE_TIMEOUT_S` | 5 |
| `CHAT_SEND_TIMEOUT_S` | 5 |
| `WS_CLIENT_QUEUE_SIZE` | 100 |
| `MAX_PENDING_PLANTS` | 1000 (hands and codes combined) |
