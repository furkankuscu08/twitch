# Minefield: technical spec

> Chat plants secret words. Say one on stream, it explodes.

Viewers secretly pick a word from a deck and plant it as a "mine". The streamer talks as usual. Streaming speech recognition (Deepgram) listens to the streamer's mic; when the streamer says a live mine word, the overlay explodes and names the viewer who planted it.

This file is the source of truth for the build. Work packages (WP1–WP14, without WP12) and their acceptance criteria are in §8. The project plan (schedule, decisions; Turkish) is in `docs/plan/minefield.md`.

---

## 1. Components

```
[Windows]  mic ──► mic page (Chrome tab, http://localhost:8000/mic)
                      │  16 kHz mono int16 PCM over WebSocket
                      ▼
[WSL]      STT engine (minefield.stt) ──80 ms chunks──► Deepgram streaming STT (EU endpoint)
                      │                ◄──interim results with word timings──┘
                      │  hypotheses (HTTP POST)
                      ▼
[WSL]      game server (minefield.server, FastAPI, 127.0.0.1:8000)
              ├── matcher + game state (minefield.core)
              ├── /overlay  (OBS browser source, WebSocket)
              ├── /dock     (OBS custom dock, WebSocket + POST)
              ├── /mic      (mic page, opened in Chrome on Windows)
              └── Twitch    (EventSub WebSocket chat, Helix: chat message)
           plant app (same process, 127.0.0.1:8001) ◄── cloudflared quick tunnel (in WSL) ◄── viewers' phones
```

- **mic page** (`web/mic`; Windows Chrome, because WSL2 has no reliable mic access):
  - Served by the game server, opened in a normal Chrome tab on Windows (`localhost` counts as a secure context, so `getUserMedia` works). Not an OBS dock: OBS docks do not grant mic access reliably.
  - Device picker (remembered in `localStorage`), level meter, connection state.
  - `getUserMedia` with `echoCancellation`, `noiseSuppression` and `autoGainControl` off. An AudioWorklet resamples to 16 kHz mono int16 and sends 20 ms frames.
  - Reconnects automatically when the engine restarts.
- **STT engine**: a separate process, so a stalled network call never blocks the server.
  - It reads audio from the mic page or from a WAV file (`--wav`, sent at real-time pace; used for dev and the harness).
  - It streams the audio to Deepgram and turns Deepgram's messages into hypotheses (§5). Backends: `flux` (default) and `nova3`, same API key.
  - There is no local model, no GPU work and no VAD of our own.
- **game server**: holds all state in memory. Nothing is persisted except Twitch tokens.
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
  harness/     accuracy runs, hypothesis replay, label assist, reports
scripts/run_all.sh   server + engine + cloudflared in one command
web/overlay/  web/dock/  web/mic/  web/plant/  web/assets/   plain HTML/CSS/JS, no build step
deck/en.json
tests/         tests/fixtures/deepgram/: recorded Deepgram messages (JSONL) for unit tests
data/          gitignored: tokens, recordings, raw Deepgram logs, hypothesis logs
reports/       harness reports (committed; shown in the video)
```

Do not create a top-level `twitch/` package; that path is an unrelated local folder.

---

## 3. Game rules

### Round
- The streamer starts a round from the dock. Mines can be planted only during a round.
- Ending the round reveals the duds and the stats, then clears all state.

### Planting (decision D4)
1. A viewer types `!mine`. The bot replies: `@{user} pick your mine: {plant_url}`. The overlay also shows a short plant URL and a QR code in a corner while a round is running.
2. The plant page shows a **hand of 6 random cards drawn from the whole deck**. Hands never exclude live words; excluding them would let anyone find the live mines by requesting many hands.
3. The viewer taps a card. The page shows the full command `!mine K7QF` with a **Copy** button.
   - The code has 4 characters (alphabet without 0/O/1/I) and is valid for `CODE_TTL_S` (300 s).
   - The code does not reveal the word.
4. The viewer types `!mine K7QF`. The server binds the word to the chatter and replies: `@{user} mine planted 💣 arming…`.
   - Parsing is lenient: case-insensitive, extra spaces allowed (`!Mine  k7qf`).

Planting rejects with a short reply:
- the user already has a live mine;
- `MAX_MINES` (4) mines are already live;
- the code is unknown or expired;
- the word is already live ("taken, pick another"). This is checked at bind time.

**Live mine:** status `arming`, `armed` or `sparking`. `MAX_MINES` and "one live mine per user" count only live mines. An exploded mine is no longer live, so its owner may plant again right away.

### Lifecycle
`arming` (`ARM_DELAY_S` = 30 s) → `armed` → `sparking` → back to `armed` (fizzle), or `exploded`. An exploded mine may later be marked `false_alarm`.

At round end, every mine that never exploded becomes a `dud`.

### Detection
See §5. Only `armed` mines can trigger.

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
- Effect: the mine becomes `false_alarm` and does not count in the stats. The overlay shows a "FALSE ALARM" stamp, and the bot posts `🧯 False alarm, @{owner} gets a free re-plant`.

### Round end
- The overlay reveals the duds (`{owner}'s mine {WORD} never went off`) and the number of booms.
- The bot posts **one recap message**: `Round over: {n} booms. 💥 @a (pineapple), @b (volcano). Survived: @c's "banana".`
  - False alarms are not listed. With no booms: `Round over: no booms.` followed by the survivors.
  - At most `CHAT_MAX_CHARS` (500, the Send Chat Message limit); if longer, drop list entries from the end and add `…`.
  - The text is built in `core` (pure) and unit-tested.

**Secrecy invariant:** the words of non-exploded mines must never reach the overlay, the dock, logs at INFO level, or chat. Receipts are masked for this reason (see Boom). Only the plant page (to its own viewer, for its own hand) and the game state hold them.

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
- `seq` grows within an utterance.
- `final: true` is sent once, when the utterance ends.
- `lag_ms`: `emitted_wall − (stream_start_wall + audio_window_end)`, i.e. network plus Deepgram processing time (§5).
- Engine and server run on the same WSL clock.
- `POST /stt/status` (heartbeat every 2 s): `{"ok": true, "backend": "flux", "deepgram": "connected", "mic": "connected", "lag_ms_p95": 420, "reconnects": 0}`.

### Server → overlay/dock
WebSocket `/ws/overlay` and `/ws/dock`. JSON messages with a `type` field:

| type | payload | overlay | dock |
| --- | --- | --- | --- |
| `snapshot` | `round`, `plant_url`, `mines:[{id, owner, status, arms_at}]` | ✓ | ✓ |
| `mine_planted` | `id, owner, arms_at` | ✓ | ✓ |
| `mine_armed` | `id` | ✓ | ✓ |
| `spark` | `id` | ✓ | ✓ |
| `fizzle` | `id` | ✓ | ✓ |
| `boom` | `id, owner, word, planted_ago_s, latency_ms, source, at, receipt` | ✓ | ✓ |
| `false_alarm` | `id, owner` | ✓ | ✓ |
| `reveal` | `duds:[{owner, word}], stats` | ✓ | ✓ |
| `status` | `mic, engine, deepgram, eventsub, tunnel_url` | — | ✓ |

`word` appears only in `boom` and `reveal`. `source` is `stt` or `typed`. `receipt` is a list of `{"text": str, "hit": bool}` (masked as in §3; exactly one item has `hit: true`; a multi-word variant is one item).

The overlay may show `latency_ms` as a small debug badge, enabled by `?latency=1`; it is used in the demo video.

### Dock → server
`POST /dock/round/start`, `/dock/round/end`, `/dock/false-alarm` (enabled for `FALSE_ALARM_WINDOW_S` after a `boom`), `/dock/typed {"text": "..."}`.

Debug only, behind `MINEFIELD_DEBUG=1`: `/dock/debug/plant {"owner","word"}`.

### Plant app (port 8001)
- `GET /`: the page.
- `GET /api/hand` → `{"hand_id","cards":[6 words]}`.
- `POST /api/pick {"hand_id","word"}` → `{"code","command","expires_at"}`. `word` must be in that hand.

No rate limiting (demo scope). If it is ever added, read the client IP from `CF-Connecting-IP`: through the tunnel every request arrives from cloudflared on localhost. No other routes on this app.

---

## 5. Speech pipeline

### Engine (`minefield.stt`)
Verify every URL, parameter and message field below against https://developers.deepgram.com before coding, and note the verified details in code comments. Talk to Deepgram over plain `websockets` (no Deepgram SDK; its API changed a lot between major versions).

- **Connection:** API key from `DEEPGRAM_API_KEY` (`.env`), header `Authorization: Token <key>`. Region from `DEEPGRAM_REGION`: `eu` → `api.eu.deepgram.com` (default), `us` → `api.deepgram.com`.
- **Audio:** the engine joins 20 ms frames into 80 ms binary messages (2,560 bytes of 16 kHz int16), the chunk size Deepgram recommends. `--wav` sends the same chunks at real-time pace. On shutdown send `{"type":"CloseStream"}`.
- **No biasing:** no `keyterm`, no keywords, no prompt. A false boom names a viewer, so it is worse than a miss.
- **Backend `flux` (default):** `wss://<host>/v2/listen?model=flux-general-en&encoding=linear16&sample_rate=16000&mip_opt_out=true`. Keep Deepgram's default end-of-turn settings; do not use `eager_eot_threshold`.
  - A Flux turn is one utterance: `utt_id = f"{session}-t{turn_index}"`.
  - Each `Update` with a non-empty `words` list → a hypothesis with `final: false`. Updates without words are **not** sent (they would count as the "next" hypothesis and cause a fizzle).
  - `EndOfTurn` → the same words with `final: true`.
  - Word fields: `word` → `text`, `confidence` → `prob`, `start`/`end` converted to seconds from `utt_start_wall`.
- **Backend `nova3`:** `wss://<host>/v1/listen?model=nova-3&language=en&encoding=linear16&sample_rate=16000&interim_results=true&punctuate=false&smart_format=false&endpointing=300&utterance_end_ms=1000&vad_events=true&mip_opt_out=true`.
  - Hypothesis = the utterance's `is_final` words so far + the words of the latest interim result.
  - The utterance ends on `speech_final: true` or `UtteranceEnd`; send that last hypothesis with `final: true`.
- **Clock:** `stream_start_wall` is the engine-clock time of the first sample sent on the current Deepgram connection. Deepgram's times are offsets in the audio sent on that connection. Check on the first raw log whether word times are relative to the stream or to the turn, and convert accordingly. `utt_start_wall = stream_start_wall + turn start`.
- **Reconnect:** on a dropped connection, reconnect with exponential backoff (0.5 s → 8 s), `session += 1`. The open utterance is discarded (no `final`), so open sparks fizzle. Audio that arrives while disconnected is dropped. If the mic page sends nothing, send Deepgram's `KeepAlive` message so the connection stays open.
- **Logs:** `--save-raw FILE` writes every Deepgram message with its receive time (JSONL). `--save-hyps FILE` writes every emitted hypothesis (JSONL); the harness replays these files (§7). Small anonymized raw logs go to `tests/fixtures/deepgram/` so the mapping is unit-tested without the network.

### Matcher (`minefield.core`, pure)
Input: the hypothesis stream above plus the armed mines. Output: `spark`, `fizzle` and `boom` events.

1. **Normalize** each word: lowercase, NFKC, strip punctuation, then map through the deck's variants (e.g. `pineapples`, `pine apple` → `pineapple`). Multi-word variants are matched on adjacent words.
2. **Occurrences:** within an utterance, the n-th occurrence of a mine word is one occurrence. Identity is (word, n), not the timestamp; word timestamps at the end of a growing transcript can shift between hypotheses. An occurrence is *present* in a hypothesis only if its `prob ≥ MIN_WORD_PROB`; n counts every occurrence regardless of prob.
3. **Spark:** an occurrence of an armed mine's word is present for the first time in hypothesis `k` → open a candidate and emit `spark`.
4. **Boom:** the occurrence is present in `CONFIRM_N` (2) consecutive **received** hypotheses, counting hypothesis `k` → `boom`. Hypotheses the engine did not send (e.g. empty Flux updates) do not count.
   - Secondary sanity check: `|start − candidate.start| ≤ AGREE_TOL_S` (0.5).
5. **Fizzle:** a received hypothesis before confirmation does not contain it → `fizzle`; close the candidate.
6. **Final-only words:** an occurrence that appears for the first time in a `final` hypothesis (very short utterance) → boom if `prob ≥ FINAL_SOLO_MIN_PROB` (0.7); otherwise spark followed by fizzle.
7. A mine booms at most once per utterance.
8. **Latency:** `now_wall − (utt_start_wall + word.end)`. Include it in the `boom` event and in logs.

Flux sends an update about every 0.25 s, so `CONFIRM_N = 2` confirms about 0.25 s after a word first appears. If replay shows too many false confirmations, raise it to 3.

**Typed mode:** `/dock/typed` text is treated as `CONFIRM_N` identical hypotheses of a synthetic utterance. That means an immediate boom, marked `source: "typed"`.

All thresholds live in one config module (`minefield/core/config.py`) and can be overridden by env vars.

---

## 6. Twitch

Verify every endpoint, scope and payload against https://dev.twitch.tv/docs before implementing. Note the verified details in code comments.

- **App:** Public client; **device code flow** (no redirect URI is used, though the console form may require one; `http://localhost:3000` is fine).
  - Tokens are stored in `data/tokens.json` and refreshed on 401.
  - Public-client refresh tokens are single-use and expire after 30 days: always store the new refresh token returned by a refresh.
  - Scopes:
    - Bot (a mod in the channel): `user:read:chat`, `user:write:chat`.
    - One test account (optional, for testing commands alone): `user:write:chat`.
    - The broadcaster needs no token: there are no markers or clips (decision D15), and the bot reads and sends chat as a moderator. Verify this against the EventSub and Send Chat Message authorization notes; if the broadcaster must authorize after all, say so and propose a spec change.
- **EventSub WebSocket:** `channel.chat.message` v1, condition `{broadcaster_user_id, user_id: bot}`.
  - Subscribe within 10 s of `session_welcome`.
  - On `session_reconnect`: connect to the given `reconnect_url` and close the old socket only after the new welcome. Subscriptions carry over, so do **not** resubscribe.
  - On keepalive timeout or a dropped connection: open a fresh connection and resubscribe. Subscriptions of a lost session are disabled, and missed events are not replayed.
- **Commands:** parsed case-insensitively; messages from the bot itself are ignored.
  - `!mine`, `!mine CODE`;
  - `!defuse` (badges: broadcaster or moderator).
- **Send Chat Message:** `POST /helix/chat/messages` as the bot. Log `is_sent` / `drop_reason`.
- **Not used:** stream markers and clips (cut in D15: they only work on a live stream and added little to the demo). The streamer's native Clip button still works.
- Chat send failures are logged and never block the game.

---

## 7. Accuracy harness (`minefield.harness`)

The harness has three subcommands:

```
python -m minefield.harness run    --wav data/recordings/a.wav --labels data/recordings/a.labels.json --deck deck/en.json [--save-hyps data/hyps/a.jsonl]
python -m minefield.harness replay --hyps data/hyps/a.jsonl   --labels data/recordings/a.labels.json --deck deck/en.json [config overrides]
python -m minefield.harness label-assist --wav data/recordings/a.wav --deck deck/en.json
```

- **`run`:**
  - Runs the **same engine and matcher** on a WAV, streamed to Deepgram at real-time pace (`--backend` as in the engine).
  - Every deck word is armed (or only the labeled ones, with `--armed-from-labels`).
  - With `--save-hyps`, it saves the hypothesis stream.
- **`replay`:** re-runs only the matcher on a saved hypothesis stream. Tuning matcher thresholds (`CONFIRM_N`, `MIN_WORD_PROB`, deck variants) takes seconds, costs nothing and needs no API key. Changing the backend or Deepgram parameters still needs `run`.
- **`label-assist`:**
  - Sends the whole file to Deepgram's pre-recorded API (`POST /v1/listen`, `model=nova-3`, word timestamps) and writes candidate labels for every deck word found. A human corrects the file.
  - For deck-sentence recordings, the same output is checked against the sentence list.
- **Labels:** `{"events":[{"word":"pineapple","t":63.2}]}`.
  - `t` is the **end** of the spoken word, in seconds from the start of the file; latency is measured from it, as in §5 rule 8.
  - Silence recordings have empty events.
- **Report** (`reports/<name>.md` + `.json`):
  - hits / misses (a hit is a boom within ±2 s of a label);
  - false alarms, reported two ways:
    - raw, with all words armed;
    - **normalized to `MAX_MINES` live mines**: raw × `MAX_MINES` ÷ armed words. The pass target applies to this number.
  - latency median / p95 / max (wall clock; the WAV is streamed at real-time pace);
  - sparks that fizzled, per word;
  - per-word table;
  - backend, Deepgram `lag_ms` p95, reconnects.
- Commit the hypothesis files behind the reported numbers (`reports/hyps/*.jsonl`, transcripts only, no audio), so anyone can rerun `replay` without an API key.
- Keep it readable: the table is shown on screen in the demo video.

---

## 8. Work packages and acceptance

Each WP is done when its acceptance criteria pass and `uv run pytest` and `uv run ruff check` are clean.

| WP | Scope | Acceptance |
| --- | --- | --- |
| WP1 | `core`: config, normalize, deck loader, game state machine, matcher | Unit tests cover: spark→boom with `CONFIRM_N` 2 and 3; spark→fizzle; a word below `MIN_WORD_PROB` is not present; occurrence identity with shifted timestamps; final-solo prob rule; multi-word variant; arming delay; live-mine definition; max mines; one live mine per user; false alarm accepted only within the window, excluded from stats; receipt window, highlight and masking of other deck words (including a fizzled live mine's word); round recap text, false alarms excluded, truncated to `CHAT_MAX_CHARS`; hand drawn from the whole deck and taken word rejected at bind; secrecy (no word in non-boom events) |
| WP2 | `server`: app, WS hub, dock routes, typed mode, debug plant, engine heartbeat timeout | With `MINEFIELD_DEBUG=1`: plant via the debug route, wait for arming, type a sentence → `boom` reaches a test WS client |
| WP3 | `web/overlay`: chips, arming ring, spark, fizzle, boom (shake + banner with receipt + sfx), static "FALSE ALARM" stamp, reveal, plant URL + QR, latency badge | 1920×1080 transparent; renders every §4 message; the demo page `/overlay?demo=1` replays a scripted sequence |
| WP4 | `web/dock`: round controls, status lights, mine list without words, "False alarm" button (enabled for 10 s after a boom), typed box | Works as an OBS custom browser dock at 400 px width |
| WP5 | `web/mic` page + `stt` engine: Deepgram client, `flux` and `nova3` backends, reconnect, heartbeat, CLI (`--mic` / `--wav` / `--backend` / `--save-raw` / `--save-hyps`) | Unit tests map recorded Flux and Nova-3 messages (`tests/fixtures/deepgram/`) to the expected hypotheses, including empty updates and a dropped connection; speaking into the mic page produces hypotheses about every 0.25 s with `flux`; the mic page reconnects after an engine restart; the engine reconnects after the Deepgram socket is killed; the heartbeat shows backend, connection state and lag |
| WP6 | `harness`: `run`, `replay`, `label-assist`, report | `run` produces the §7 report for one WAV in about its duration; `replay` reproduces the same matcher results from saved hypotheses in seconds, without an API key |
| WP7 | `deck/en.json`: ~120 concrete, funny, everyday-but-not-too-common nouns with variants | No brands, offensive words or homophone pairs; no word among the ~1,000 most frequent English words; a harness pass on the deck-sentence recording drops misheard words |
| WP8 | `twitch_api.auth`: device code flow CLI per account, token store, refresh | `python -m minefield.twitch_api.auth --account bot` stores a working token |
| WP9 | EventSub client + commands + chat send | Commands from a test account change state and get replies; reconnect works |
| WP10 | boom message, false-alarm message, round recap message | With a fake Twitch client: a boom posts the boom message, a false alarm within 10 s posts the false-alarm message, round end posts one recap message; a failed send is logged and the game continues. Then once on the real channel (no live stream needed): all three messages appear in chat |
| WP11 | `web/plant` + plant app + code binding + tunnel helper | From a phone: hand → pick → copy `!mine CODE` → paste in chat → chip with the owner's name |
| WP13 | Polish and rehearsal fixes | Two uninterrupted rounds (typed mode + debug plant, or with a friend) |
| WP14 | Ops: `scripts/run_all.sh` (server + engine + cloudflared; fails clearly if `DEEPGRAM_API_KEY` is missing), English README (setup, Deepgram key, Twitch app registration, how to open the mic page, no-key demo path: `MINEFIELD_DEBUG=1` + `/overlay?demo=1` + typed mode + debug plant, `harness replay` on the committed hypotheses), demo-day checklist | A fresh clone on the same machine starts with one script plus the mic page in Chrome; the no-key demo path works without the STT engine |

Order and milestones:
- **M0:** WP7, WP8;
- **M1:** WP1–WP4 (WP3 basic);
- **M2:** WP5, WP6;
- **M3:** WP9, WP10;
- **M4:** WP11 (WP12, the chat simulator, was removed);
- **M5:** WP3 full, WP13, WP14.

---

## 9. Config defaults

| Name | Default |
| --- | --- |
| `STT_BACKEND` | `flux` |
| `DEEPGRAM_REGION` | `eu` |
| `CONFIRM_N` | 2 |
| `MIN_WORD_PROB` | 0.6 (tune with `replay`) |
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
