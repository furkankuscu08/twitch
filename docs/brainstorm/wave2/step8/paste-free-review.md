# Free review: 4 Twitch hackathon project ideas

You are an independent reviewer. We are a solo entrant in a hackathon and have narrowed our ideas to four. We want your honest, free-form opinion before we choose one and start building.

## What to read

Read these files and nothing else in the repository:
1. `docs/competition/rules.md`: the official rules, including the judging criteria.
2. `docs/competition/overview.md`: the official overview and submission requirements.
3. `docs/competition/resources.md`: the official FAQ and resources.
4. This file.

You may search the web (for example, for existing products or technical constraints). When a claim in your review comes from a search, give the link.

## What we want

Free format. No scoring table is required. For each idea, tell us what you think is good and what is bad about it, and what you would add, remove or change, and why. Then say which one you would build and why.

You may also propose a combination of these ideas or a different idea, in a short separate section.

The order of the ideas below is arbitrary.

**Write your review in Turkish** (technical terms and product names may stay in English). Save it to `docs/brainstorm/wave2/step8/review-opus.md`. Do not modify any other file.

## The builder

- Solo. An ML engineer, strong in Python, FastAPI and Docker. New to Twitch, with no audience.
- Turkish; speaks English with an accent. The video will be in English.
- Machine: Windows 11 with WSL2 (the repo lives in WSL), RTX 4070 Laptop GPU with 8 GB, Ryzen 7 8845HS, 32 GB RAM. Mic capture from inside WSL2 is unreliable, so any speech-to-text would run as a native Windows Python process; OBS runs on Windows.
- Devices and people: one phone of their own, 2–3 more through friends; 1–2 friends can join the recording.
- Time: about 20–25 hours in total until the deadline, including recording and editing the video. The build budget is about 17.5 hours: a shared base (3.5 h) + the idea's MVP (up to 12 h) + at least 2 h of buffer. Video recording and editing come on top.
- Dates: today is 28 October 2026. Day-1 tests are planned for 29 October, the build for 30 October – 1 November, the video for 1–2 November. Deadline: 2 November 2026, 14:00 PT.

## Shared build facts (apply to every idea)

**Constraints**
- One streamer plus three test accounts (plus 1–2 friends). No real audience.
- No commercial games or commercial music in the video. Where an idea's natural setting is a game, the demo can use a small original game built with Codex (about 1 h, paid from the buffer) or an MIT-licensed open-source game.
- No Twitch content kept beyond 24 h.

**Shared base (built first for any idea, 3.5 h):** Twitch app with OAuth for broadcaster and bot and token refresh; EventSub WebSocket chat and Send Chat Message; a local FastAPI server pushing to OBS browser sources and an OBS dock; obs-websocket connection; and a Codex-built chat simulator in which the three test accounts post scripted chat over the real API (used for rehearsal, tests and recording).

**How Codex is used:** the whole project is built with Codex in one main thread. The chat simulator is the shared Codex-built part; each idea names one more concrete Codex artifact.

**Twitch facts**
- Create Clip takes `title` and `duration` (5–60 s). It captures the live output from roughly 85 s before to 5 s after the call and is asynchronous. Which part of that window `duration` keeps is not documented.
- Create Stream Marker needs VOD storage enabled.
- Send Chat Message supports threaded replies (`reply_parent_message_id`, 500-character limit; a dropped message returns `drop_reason`). A bot that is a moderator can send 100 messages per 30 s instead of 20.
- Threaded replies are ordinary public chat messages, visible to everyone in chat.
- The Wake Lock API (keeping a phone screen on) needs HTTPS.

**Day-1 tests (planned before building; a failed test means the fallback in the idea's risks)**

| Test | What it checks | Ideas | Pass condition |
| --- | --- | --- | --- |
| T1 | Real-time local speech-to-text keyword spotting during a live stream, with the builder's own voice | Minefield | ≥80% hits, ≤1 false alarm per 10 min, ≤3 s lag, no dropped frames |
| T1b | Local speech-to-text of spoken answers | Checkpoint | Quote ready ≤2 s after the streamer stops; ≥9 of 10 readable without edits |
| T2 | obs-websocket: replay buffer + Media Source slow motion; mute/silence events; source screenshots | VAR, Tap on the Shoulder | Replay on screen ≤5 s; mute event arrives |
| T4 | A Twitch-login page behind a public URL; for Tap, a phone page over HTTPS with Wake Lock | Minefield, Tap on the Shoulder | One path works end to end |
| T5 | API checks: Create Clip with title, Stream Marker, threaded reply | All | All succeed on a new channel |

## How to read the evidence

Three independent researchers searched the web for each card: **A**, **G** and **C**. A separate link check (**L**) opened pages that only one researcher had found. For Checkpoint, whose design changed after the research, the changed part was checked by one more source (**P**).

- **Confirmed**: found by two or more researchers.
- **Verified**: found by one researcher, and the link check opened the page.
- **Unverified**: the page could not be opened (blocked site, Reddit, X, or a search snippet only). It may exist; treat it as weaker evidence.
- **Overlap**: `Same core loop` (same who acts, same trigger, same output on stream), `Partial`, or `Adjacent`.
- **Well-known**: a major streaming platform or tool (Twitch, StreamElements, Streamlabs, Streamer.bot, Elgato, OBS, Meld, Sound Alerts, StreamUP), ≥1,000 users or installs, ≥100 GitHub stars, or a post with ≥10,000 views.
- Stream-type shares come from a research snapshot: Just Chatting 14.2% of viewing, IRL 1.8%, games make up most of the top 15 categories, indie games +51% YoY, horror +6%.

## The 4 ideas and their evidence

Each idea is followed by the evidence our research found, then by the additions we are considering for the 12 h MVP. The card text describes the original MVP (up to 9.5 h); the additions are separate so you can judge them on their own.

### Idea: Tap on the Shoulder

**One-liner:** Chat can't tap you on the shoulder while you're heads-down. Now it can: viewer reports and mod cues become a face on your desk, and chat confirms the fix.

**Core loop:**
1. **Inputs:**
   - ≥2 distinct viewers mention mic, audio, "far away", black screen or frozen within 60 s, or anyone types `!mic`;
   - a mod taps a preset on a private phone page ("you sound far away", "game too loud", "mic muted", "answer @x");
   - obs-websocket reports the mic input muted, or its level below a silence threshold for N s while live (two separate signals).
2. A phone face on the desk, in the camera shot, turns alarmed and shows the issue in huge letters. A chime plays in the streamer's headphones only. When chat and OBS agree, the face says so ("chat + OBS: mic muted").
3. The streamer fixes it and taps a "fixed" hotkey.
4. The bot posts "Fix #2: sound right now? 👍/👎". Replies that arrive earlier than fix time plus an estimated stream delay are ignored (latency differs per viewer, so the result reads "chat confirmed", not "everyone heard it").
5. The issue resolves on the dock, and the overlay credits the first reporter.
6. When nothing is wrong, the face shows calm chat state (a first-time chatter waves, a question is waiting).

**3-minute video:**
- 0:00 Hook: a muted mic, caption "OBS can see this one…", the face panics, unmute. Then "…but not this one": the mic is turned away, chat says "you sound far away", the face shows FAR AWAY, the streamer fixes it.
- 0:30 The bot asks "sound right now?", two 👍, a credit pops.
- 1:00 A mod cue from a phone: "game too loud".
- 1:30 Calm mode: the face waves at a first-time chatter and raises a hand for a question.
- 2:00 Why it works through a fullscreen game and stream delay.
- 2:30 Codex artifact, close.

**Codex artifact:** the phone face page and the detector's test suite, driven by the chat simulator with noisy chat scripts.

**MVP:**
- **In:** report detector, mod cue page, phone face (QR pairing, Wake Lock, HTTPS), headphone chime, obs-websocket mute/silence check, confirm prompt, credit overlay.
- **Stretch:** calm mode (everyday chat states), a Stream Deck "fixed" button.
- **Out:** lamp, OBS scene control, ML audio analysis.

**Build parts:**

| Part | Hours |
| --- | --- |
| Report detector | 1 |
| Mod cue page with Twitch login | 1.5 |
| Phone face page + pairing over HTTPS | 2.5 |
| obs-websocket mute/silence check | 1 |
| Confirm loop + dock | 1.5 |
| Credit overlay | 0.5 |
| Polish | 1 |
| **MVP subtotal** | **9** |
| Stretch: calm mode 1 | 1 |

**Twitch surfaces, scopes and local parts:** EventSub chat, Get Moderators (`moderation:read`), Send Chat Message; OBS browser source and dock; obs-websocket; a phone web page over a secure WebSocket (public URL or local certificate; Wake Lock needs HTTPS).

**Demo setup:** 1 streamer + 3 test accounts (one as mod). A spare phone in the camera shot, a webcam and a mic. For the fullscreen-game case, a small Codex-built game (about 1 h, from the buffer).

**Closest existing things and claimed difference:** OBS plugins that warn the streamer privately: Muted Notification (12.4k downloads; talking into a muted mic), Remember to Talk (2.4k downloads; mic silent too long), Audio Source Mute Indicator; Twitch Guardian (keyword-alert Chrome extension); Elgato Prompter chat mode and Mochi chat pet; WooferBot and Streamer.bot lights on Twitch events; a friend relaying chat. The well-known plugins cover only the "your mic is muted or silent" input. *Difference:* it routes human judgment (viewer reports, mod cues) to a signal in the room that survives a fullscreen game, cross-checks OBS, then closes the loop with the audience's confirmation.

**Risks and day-1 tests:**
- Real problems may be too rare to keep it installed; calm mode answers this.
- Reports may reflect one viewer's device, so the UI says "2 listeners report…", not "your mic is broken".
- obs-websocket mute and silence events (T2).
- Some streamers monitor their own mic, and viewers sometimes do tell them in chat. The hook's second case ("you sound far away") is one no OBS plugin can detect.

### Evidence: Tap on the Shoulder

**Card in one line:** viewers and mods report production problems (muted mic, black screen, "you're too far away"); the report is checked against OBS, reaches the streamer in the room, and chat confirms the fix.

**Competitors**

| Name | What it does | Found by / status | Overlap | Well-known |
| --- | --- | --- | --- | --- |
| [Muted Notification](https://obsproject.com/forum/resources/muted-notification.1706/) | OBS filter: sound or red mark when you talk into a muted source | G / verified | Partial | Yes (12,466 downloads) |
| [Remember to Talk](https://obsproject.com/forum/resources/remember-to-talk.2484/) | Private alert when the mic has been silent too long | C / verified | Partial | Yes (2,448 downloads) |
| [Audio Source Mute Indicator](https://obsproject.com/forum/resources/audio-waves-visualizer.2247/) | Tone and overlay on mute/unmute | C / verified | Partial | No |
| [Twitch Guardian](https://chromewebstore.google.com/detail/twitch-guardian/fcfdekecgocobpjhldifpplcifkfflme) | Desktop alert when chat keywords appear | A, G, C / confirmed | Partial | No (about 40–60 users) |
| [Elgato Prompter Chat Mode](https://help.elgato.com/hc/en-us/articles/20461145372813-Elgato-Prompter-Chat-Mode) | Chat shown behind the camera lens | A, G, C / confirmed | Adjacent–Partial | Yes (Elgato) |
| [WooferBot](https://wooferbot.com/), [Mochi the Cat](https://marketplace.elgato.com/product/mochi-the-cat-6ac71734-f507-4887-8350-10357f6e6ea0) | Mascots that react to stream events; WooferBot drives smart lights | A, G, C / confirmed | Adjacent–Partial | Mochi via Elgato |
| StreamNotch (Mac app), ViperVex mic widget | Own-mic warnings | G / verified; ViperVex unverified | Adjacent | No |

**Difference:** each part exists alone (OBS mute/silence alerts, chat keyword alerts, reactive mascots). Not found: viewer reports and mod cues cross-checked against OBS, delivered as one in-room signal, closed by a chat confirmation. A: "yes, narrowly"; G: "partly"; C: "yes, parts exist". The well-known plugins cover only the streamer-private "your mic is muted/silent" input.

**Demand**
- Snoop Dogg streamed with no audio for over an hour; chat was emote-only and could not tell him ([Kotaku, 2021](https://kotaku.com/twitch-spammers-just-wanted-to-save-snoop-dogg-from-str-1847293788), C / verified).
- OBS forum request for a streamer-only mute icon, "streamers often forget they've muted" ([2018](https://obsproject.com/forum/threads/mic-mute-notifier-icon-main-screen.80363), C / verified).
- A new streamer talked for two hours on a muted mic, through a raid (G, Reddit, unverified); raided streams left on a black screen (G, X, unverified); viewers reporting audio and confirming fixes (A, Reddit, unverified); an art streamer and a moderator asking how to get the streamer's attention (A, Reddit, unverified).

**Counter-signals**
- "Monitor your own mic in OBS instead of waiting for chat" (G, Reddit, unverified); the OBS-only plugins above show some streamers solve the mute case privately (C).
- DrDisrespect muted himself for about 10 minutes and viewers did tell him ([mein-mmo](https://mein-mmo.de/en/drdisrespect-experiences-an-outburst-in-cod-warzone-accidentally-mutes-himself,611302/), L / verified).
- Viewers' audio reports can conflict (A, Reddit, unverified).

**Audience fit:** any broadcast with a mic: all three say type-independent. Most useful when the streamer is heads-down or in a fullscreen game. Natural-setting demo: Yes with a small original fullscreen game; the desk failure cases (muted, black scene, far away) need no game.

**Fact issues**
- OBS reports mute state and volume levels; "muted" and "unexpectedly silent" are different signals and need thresholds (A).
- Viewer latency is per player, so "everyone has seen the fix" cannot be guaranteed; "chat confirmed" can (A).

**Proposed additions for the 12 h MVP (+3 h on top of the 9 h above):**

| Addition | Hours | What it does |
| --- | --- | --- |
| Calm mode | 1 | The former stretch item moves into the MVP: when nothing is wrong, the face waves at first-time chatters, raises a hand for a waiting question, dozes when chat is quiet. |
| Soundcheck | 1 | At the start of a stream the streamer presses "soundcheck"; the face shows "SOUNDCHECK A", the streamer talks, the bot asks chat "Test A: mic vs game? !heard good / quiet / loud", and mic and game levels are measured from `InputVolumeMeters`. The face shows both: "chat: quiet · meter: −28 dB → raise mic". |
| Black or frozen screen | 0.5 | `GetSourceScreenshot` takes a small frame once a second; very low brightness → "BLACK SCREEN", no change for 10 s → "FROZEN?". Only on game or camera scenes. Shown as "chat + OBS" when chat reports the same. |
| End-of-stream issue report | 0.5 | "3 issues · avg fix 42 s · first reporter: @ana" on the dock and in chat. |

---

### Idea: VAR

**One-liner:** When chat disputes a moment, two `!var` calls start a broadcast-style review: slow-motion replay, a 15-second chat jury, a verdict stamp, and a titled clip.

**Core loop:**
1. The streamer claims something ("IN!").
2. Two distinct viewers type `!var` within 30 s. The threshold scales with active chatters, and mods or the streamer can also call it.
3. A "VAR CHECK" stinger plays. obs-websocket saves the 60 s replay buffer.
4. An OBS Media Source, driven by obs-websocket, plays the last ~10 s shifted by a latency offset, with the last 4 s at half speed.
5. Chat votes `!yes` or `!no` for 15 s; names appear on a jury bench.
6. The verdict stamp lands. Then the app creates a 60 s clip titled "VAR: NO BASKET" and a marker. The clip holds the review, and the review holds the replay of the moment.

**3-minute video:**
- 0:00 Hook: paper ball, "IN!", two `!var`, siren, slow motion off the rim, jury, "NO BASKET" stamp.
- 0:25 The clip link lands; play 5 s of it.
- 0:45 Self-VAR: "I can draw a perfect circle", the streamer calls VAR on themselves, chat overturns it.
- 1:30 How the latency offset lands the replay on the right moment, and the nudge-back hotkey.
- 2:10 Codex artifact, close.

**Codex artifact:** the replay pipeline (buffer save → Media Source → slow motion) and a simulator-driven test of call thresholds and vote timing.

**MVP:**
- **In:** call threshold, replay buffer save, Media Source slow-motion playback, latency offset and nudge-back hotkey, vote, jury bench, stamp, titled clip, marker.
- **Stretch:** verdict history strip ("claims upheld 2/5 today", counters only), a second camera angle.
- **Out:** telestrator, AI judging.

**Build parts:**

| Part | Hours |
| --- | --- |
| Replay save + Media Source playback | 2 |
| Latency offset + hotkey | 1 |
| Call and vote logic | 1 |
| Overlay: stinger, jury bench, stamp | 2.5 |
| Clip + marker | 0.5 |
| Polish | 1.5 |
| **MVP subtotal** | **8.5** |
| Stretch: history strip 0.5, second angle 1 | 1.5 |

**Twitch surfaces, scopes and local parts:** EventSub chat; Create Clip (`clips:edit`), Create Stream Marker (`channel:manage:broadcast`, VOD storage on), Send Chat Message; OBS replay buffer and Media Source via obs-websocket; OBS browser source.

**Demo setup:** 1 streamer + 3 test accounts. A webcam on the action, a mic, desk props. Optionally a small Codex-built game designed to produce close calls (about 1 h, from the buffer) to show the game-stream setting.

**Closest existing things and claimed difference:** chat-called replays: tomaae OBS instant replay (12.6k downloads, last updated 2019), BarRaider OBS Tools `!replay` (can also post a clip), Fyre Instant Replay (StreamElements widget; mentions vote-to-trigger without details); Glitch Studios Instant Replay (mod-triggered branded replay with slow motion); Streamer.bot replay-buffer actions; native polls and Senchabot chat polls; Streamer's Court (a Steam game where chat votes a verdict, no replay). *Difference:* a full review ritual (call, replay, jury, verdict, titled clip) instead of a replay or a poll alone.

**Risks and day-1 tests:**
- Replay buffer and Media Source playback (T2).
- Latency means the replay must land on the right moment (offset + nudge-back).
- The 60 s clip may cut the original moment; the replay inside the review still shows it. Clip title and window (T5).
- An immediate review interrupts play; a streamer asking for replays wanted control over when they run.

### Evidence: VAR

**Card in one line:** chat calls a VAR review on a disputed moment; a slow-motion replay plays, a 15 s chat jury votes, a verdict stamp lands, and a titled clip is made.

**Competitors**

| Name | What it does | Found by / status | Overlap | Well-known |
| --- | --- | --- | --- | --- |
| [tomaae OBS instant replay](https://obsproject.com/forum/resources/picture-in-picture-instant-replay.746/) | Replay buffer as picture-in-picture; viewers can trigger it by chat command | G, C / confirmed | Partial | Yes (12,642 downloads; last update Oct 2019) |
| [Streamer.bot replay buffer actions](https://docs.streamer.bot/api/sub-actions/obs-studio/replay/set-replay-buffer-state) | Save and play replay-buffer footage from any trigger | A, G / confirmed | Partial | Yes (Streamer.bot) |
| [Twitch native polls](https://dev.twitch.tv/docs/api/reference/#create-poll) | Timed chat vote | A, C / confirmed | Partial (jury half) | Yes (Twitch) |
| [Fyre Instant Replay](https://thefyrewire.com/login/instant-replay) | StreamElements widget: `!replay` plays a clip on the overlay; mentions "vote-to-trigger options" without details | A / verified | Partial | No |
| [Glitch Studios Instant Replay](https://overlay.glitchstudios.dev/instant-replay) | Mod-triggered branded replay with countdown and 0.5× slow motion; no voting | A / verified | Partial | No |
| [BarRaider OBS Tools](https://docs.barraider.com/faqs/obs-tools/actions/) | `!replay` instant replay; can create and post a Twitch clip; no voting | C / verified | Partial | Not verified |
| [Senchabot chat poll](https://extensions.senchabot.com/setup/chat-poll) | Mod-started chat poll with on-stream bars | G / verified | Partial (jury half) | No |
| Streamer's Court (Steam, 2022) | Streamer rules on a viewer "crime", chat votes guilty/not guilty; no replay | L / verified | Adjacent | No |
| OK Gamers; Oddshot (defunct) | Speech-started poll; `!shot` replay | G; C (snippet) | Adjacent | No |

Dropped: PROVE IT (unverifiable). Unverified: RTS Action Replay (X post).

**Difference:** replay on command and chat votes both ship, and slow-motion branded replays exist. Not found: call threshold → replay → timed jury → verdict → titled clip as one ritual. A and G: "partly"; C: "yes". A re-search for VAR overlays, `!var` bots and replay-then-vote tools found nothing closer.

**Demand**
- Indirect: 12.6k downloads of a chat-called replay script (historic; last updated 2019) (C, L / verified).
- A streamer asks how to save moments and replay them between rounds (A, Reddit, unverified). Streamers are advised to use the replay buffer (G, X, unverified). Twitch tested a live rewind for viewers (C, snippet).
- Direct requests for a chat jury or VAR review: not found (A, G, C).

**Counter-signals:** the replay request wants control over *when* the replay happens, not an immediate interruption (A, unverified).

**Audience fit:** tied to disputed, visible outcomes: competitive games (the bulk of viewing), sports-like IRL challenges, desk trick shots. Natural-setting demo: Yes with a small original game designed to produce close calls ("did it touch the line?"), or a desk challenge.

**Fact issues**
- Create Clip captures the live output in a window of about 85 s before and 5 s after the call; `duration` 5–60 s; creation is asynchronous (A, G, C, P). The clip must be created while the review is on the live output, and a long review can push the original moment out of the clip.

**Proposed additions for the 12 h MVP (+3.5 h on top of the 8.5 h above):**

| Addition | Hours | What it does |
| --- | --- | --- |
| VAR pending | 1 | When the call threshold is met, the replay buffer is saved at once, but the review does not start. A corner badge shows "🟨 VAR PENDING (2 calls)"; the streamer presses "review now" when ready. An "auto" mode keeps the original behaviour. Warning after 2 min, call dropped after 5 min. |
| Telestrator | 1.5 | At the end of the slow motion the frame freezes; a mod or the streamer draws a line or circle in the dock, and the drawing appears on stream over the frozen frame. The verdict stamp lands on it. |
| Referee reputation | 1 | Callers whose call overturns the claim and jurors who vote with the verdict earn points, kept across streams (SQLite). "Referee of the night" at the end of the stream. |

---

### Idea: Checkpoint

**One-liner:** Go heads-down without ghosting chat: messages become save crystals, and at the checkpoint the streamer answers out loud, the words type onto the card, and each viewer gets a threaded reply quoting what the streamer said.

**Core loop:**
1. The streamer hits a hotkey or a mod types `!focus`. A corner badge: "Focus: messages saved 0".
2. Each normal viewer message drops a save crystal in the viewer's color. Commands and bot lines are filtered out. The app keeps the message id, author, text and first-time flag.
3. The streamer hits "checkpoint". A lower-third call-in card shows the first saved message. Questions and first-time chatters come first.
4. The streamer answers aloud without stopping work. Local speech-to-text (faster-whisper) types the words onto the card as they are spoken.
5. About 2 s of silence, or "next", closes the card: it stamps ✓ and flies off. After 3 s the bot replies in the viewer's thread: "✓ answered on stream: 'It's a Micron 05, it doesn't bleed' (12:04)". If the transcript is empty or low-confidence, the reply drops the quote: "✓ answered on stream (12:04)". "Skip" closes the card with no reply.
6. At the end: "Checkpoint cleared: 4 answered, 4 receipts sent".
7. *(Stretch)* When a clip of the answer is confirmed, a second threaded reply adds "▶ watch it: <clip link>".

**3-minute video:**
- 0:00 Hook: inking time-lapse, 6 crystals stack. The streamer taps checkpoint; the card reads "@ana (first time!): what pen is that?". Still inking, the streamer says "Ana, it's a Micron 05, it doesn't bleed"; the words type onto the card; silence, ✓, fly-off; split screen of Ana's chat with the threaded quote. The next card is up at 0:19.
- 0:20 Two more cards: one closed with "skip", one with a low-confidence transcript that sends the plain receipt.
- 1:00 A viewer who "left" opens chat later and finds the answer.
- 1:30 Under the hood: voice segmenting, the silence rule, reply threading.
- 2:05 Codex artifact.
- 2:30 Close. If the clip stretch is done, it gets 10 s around 1:00.

**Codex artifact:** the voice-to-receipt pipeline, tested with recorded answer audio and simulated chat during focus.

**MVP:**
- **In:** focus toggle (hotkey, mod), filter, crystal badge, call-in card with live transcript line, dock with next/skip, ordering, local speech-to-text, silence close with hold key, answer receipt with confidence gate.
- **Stretch:** clip link reply; closing on the next viewer's name; reminder; scene auto-start.
- **Out:** context thumbnails (cut in revision 3; also removes the stream-delay mismatch), urgent lane, LLM summaries, history beyond the stream.

**Build parts:**

| Part | Hours |
| --- | --- |
| Focus toggle (hotkey, mod `!focus`) + filter | 1 |
| Crystal badge overlay | 1.5 |
| Call-in card overlay with live transcript line and ✓ stamp | 1.5 |
| Dock + ordering + next/skip | 1 |
| Local speech-to-text: mic capture, voice-activity segmenting, faster-whisper, partial updates | 2 |
| Voice close: silence rule, hold key, tuned on recorded clips | 0.5 |
| Answer receipt: confidence gate, trim to 500 chars, threaded reply, `drop_reason` handling | 0.5 |
| Polish | 1 |
| **MVP subtotal** | **9** |
| Stretch: clip link reply (Create Clip From VOD, fallback Create Clip; poll Get Clips) 1, name-based close 0.5, reminder 0.5 | 2 |

**Twitch surfaces, scopes and local parts:** EventSub chat (`message_id`), Send Chat Message with `reply_parent_message_id` (500-char limit, read `is_sent` / `drop_reason`); the bot is a moderator (100 messages per 30 s instead of 20). Stretch: `clips:edit` or `channel:manage:clips`, Get Clips. OBS browser source and dock; local mic + faster-whisper (shared with Minefield).

**Demo setup:** 1 streamer + 3 test accounts. Webcam and mic. A focus task on our own content (drawing, building, or a small Codex-built game).

**Closest existing things and claimed difference:** Meld X AMA Question Queue (same core loop up to the featured question; well-known), StreamerQnA, Social Stream Ninja featured message, Senchabot featured message, Chatterino highlights. *Difference:* the streamer answers by voice without lifting a hand, and each viewer receives the streamer's actual words as a threaded reply.

**Risks and day-1 tests:**
- Speech-to-text speed and accuracy on the user's machine (T1b). If it fails, switch to the pause-trigger fallback.
- A thinking pause closes the card early: 2 s threshold plus a hold key.
- A misheard word in a viewer's quote: the confidence gate sends the plain receipt instead.
- AutoMod or blocked terms drop the reply: read `drop_reason`.

### Evidence: Checkpoint

**Card in one line (after the pivot):** during a focus stretch messages become save crystals; at the checkpoint the streamer answers out loud, the words type onto the card, and each viewer gets a threaded reply quoting what the streamer said.

**Evidence status:** competitors and demand below were found by A, G and C for the pre-pivot card. The post-pivot difference was checked by one source (P).

**Competitors**

| Name | What it does | Found by / status | Overlap | Well-known |
| --- | --- | --- | --- | --- |
| [Meld X AMA Question Queue](https://meldstudio.co/gallery/x-ama-question-queue/) | Messages ending in "?" or `!ask` collect in an on-screen queue; the streamer clicks one to feature it | A, G, C / confirmed | Same core loop **before** the pivot (user's ruling); after the pivot: Partial | Yes (Meld) |
| [StreamerQnA](https://obsproject.com/forum/resources/streamerqna.1977/) | Command-submitted questions shown one at a time; bot replies on submission, not on answer | A, G, C / confirmed | Partial | Yes (9,543 downloads) |
| [Social Stream Ninja featured message](https://socialstream.ninja/docs/dock-live-guide.html) | Operator features a message; replying to the viewer is manual | A, G, C / confirmed | Partial | No counts |
| Meld Chat Highlight, Senchabot Featured Message, AskMeLive | Put one message on screen | G / verified or snippet | Adjacent–Partial | Meld |
| Chatterino highlights, Twitch Chat History | Help find or catch up on messages | A, C | Adjacent | Chatterino, Twitch |

**Difference after the pivot (P):** none of Meld, StreamerQnA, Social Stream Ninja or Senchabot listens to the streamer or sends anything back after an answer; a search for a Twitch tool that transcribes the streamer's answer found none. The nearest hits are tools where an AI answers chat by text-to-speech, the opposite direction. Senchabot's after-answer behaviour is unverified.

**Demand (for the problem)**
- A Streamlabs guide describes the manual version: scheduled breaks to read chat, mods keeping a running list of questions ([Streamlabs](https://streamlabs.com/content-hub/post/how-to-maintain-game-concentration-while-streaming), C).
- An art streamer misses greetings while drawing; viewers stop chatting when their messages get no reaction (A, Reddit, unverified); a paid question-queue product launched in October 2026 (G, X, unverified); Twitch built Chat History so newcomers can catch up (C).

**Counter-signals:** some viewers won't wait through a long non-response; a saved message does not mean its author stays (A, unverified). After the pivot, a misheard word could end up in a viewer's quote (P; the card sends a plain receipt when the transcript is weak).

**Audience fit:** heads-down formats: art (#40, about 17 viewers per channel), making, coding, cooking, and focused gameplay. Natural-setting demo: Yes (drawing, building, or a small original game). Type-independent: partly.

**Fact issues:** the pre-pivot context-screenshot timing problem (A) no longer applies; thumbnails were cut. Threaded replies (`reply_parent_message_id`) are documented (A, C, P). Local speech-to-text speed and accuracy on the user's machine are untested (day-1 test T1b).

**Proposed additions for the 12 h MVP (+3 h on top of the 9 h above):**

| Addition | Hours | What it does |
| --- | --- | --- |
| FAQ | 1.5 | Every answered card is stored (question, final transcript, confidence, time, clip link). When a new chat message looks like a question, it is compared with the questions already answered in this stream (small embedding model such as `all-MiniLM-L6-v2`, cosine threshold starting at 0.85). On a match with a confident earlier answer, the bot replies in the viewer's thread: "📌 Answered earlier (12:04): 'It's a Micron 05, it doesn't bleed' ▶ clip · type !ask to ask anyway". During focus the message does not become a crystal; the dock counts it as auto-answered. Same stream only. |
| Clip link in the receipt | 1 | The former stretch item: the receipt carries a link to a clip of the answer. |
| Undo window | 0.5 | The 3 s before the receipt is sent becomes a visible countdown on the dock; "undo" turns it into the plain receipt without the quote. |

---

### Idea: Minefield

**One-liner:** Viewers secretly plant "word mines". When the streamer says a mined word out loud, it explodes on stream with the planter's name.

**Core loop:**
1. A viewer types `!mine`. The bot replies with a link to a plant page (Twitch login). Nobody else sees the word.
2. The overlay shows mine chips with owners' names, never the words. Rules: one live mine per viewer, 4+ letters, not a top-1000 common word, blocklist.
3. Viewers steer the conversation toward their word ("worst pizza topping?").
4. Local speech-to-text listens to the streamer's mic: faster-whisper (`base.en`/`small.en`) on a sliding ~2 s window, VAD on, live mines passed as `hotwords`, whole-word match on normalized text (plurals count).
5. Instant explosion, screen shake, the banner "Bo's mine: PINEAPPLE (planted 6 min ago)" and a stream marker. A mod can **DEFUSE** within 10 s: a rewind animation and a "false alarm" stamp, played as a gag. If not defused, a titled 30 s clip is created.
6. Unexploded mines flip over as "duds" at the end: "Cy's mine 'GIRAFFE' never went off".

**3-minute video:**
- 0:00 Hook: chatting about lunch, "pineapple on pizza is—" BOOM, banner, Bo's chat line "GOT HIM 😈", cut back to Bo's bait question.
- 0:20 How it works: `!mine`, the plant page, chips, the rules.
- 0:50 Round two: two viewers bait; one mine hits, one fails; a misheard word fires and a mod defuses it.
- 1:40 The dud reveal at the end of the stream.
- 2:00 Under the hood: local speech-to-text, nothing recorded, hotwords and whole-word matching, with accuracy numbers from our test harness.
- 2:30 Codex artifact, close.

**Codex artifact:** an accuracy harness that replays recorded test talk through the spotter and reports hits, false alarms and lag.

**MVP:**
- **In:** plant page, chips overlay, local keyword spotting, explosion and banner, marker, titled clip, DEFUSE, dud reveal.
- **Stretch:** whisper intake (if T4 passes), "Call it" mode.
- **Out:** leaderboards across streams, multi-word phrases, any LLM.

**Build parts:**

| Part | Hours |
| --- | --- |
| Plant page with Twitch login + public URL | 1.5 |
| Speech-to-text spotter + matching rules | 2.5 |
| Accuracy harness | 1 |
| Overlay: chips, explosion, banner | 2 |
| Marker, clip, DEFUSE, duds | 1.5 |
| Polish | 1 |
| **MVP subtotal** | **9.5** |
| Stretch: whisper intake 0.5, "Call it" 1.5 | 2 |

**Twitch surfaces, scopes and local parts:** EventSub `channel.chat.message` (`user.whisper.message` in stretch), Send Chat Message, Create Stream Marker (`channel:manage:broadcast`, VOD storage on), Create Clip (`clips:edit`); OBS browser source; local speech-to-text on the mic only; a public URL for the plant page.

**Demo setup:** 1 streamer + 3 test accounts. Mic and webcam. To keep the demo from looking staged, one or two friends plant words through the page, so the streamer really doesn't know them.

**Closest existing things and claimed difference:** OK Gamers (TwitchCon Hackathon 2019 grand prize: streamer speech starts a chat poll); Streamer.bot Voice Control (phrases the streamer configured trigger actions); speech-recognition swear jars (Blabla Radar Swear Jar, obs-popup-overlay); stream-bingo overlays (1up.vision Bingo); secret-word chat games (AnkhbotSecretWord) and Taboo-style games (Wordeous). *Difference:* every speech trigger found uses words the streamer chose, and every viewer-chosen secret-word game runs in typed chat. Here viewers secretly choose the words and the streamer's own speech sets them off, inside ordinary talk.

**Risks and day-1 tests:**
- Speech-to-text accuracy and false hits on casual speech (T1).
- Sealed intake: the plant page needs a public URL and login; whisper intake is unverified (T4).
- Fun is unvalidated: a 20-minute session with three people.
- Trolls already try to bait streamers into saying things on air; the blocklist screens planted words before they go live.
- faster-whisper hotwords can be hallucinated on silence; VAD stays on (known fix).

### Evidence: Minefield

**Card in one line:** viewers secretly plant words; when the streamer says one, an automatic explosion names the planter.

**Competitors**

| Name | What it does | Found by / status | Overlap | Well-known |
| --- | --- | --- | --- | --- |
| [OK Gamers](https://devpost.com/software/ok-gamers) (TwitchCon Hackathon 2019, grand prize) | Streamer says "Ok gamers" + a question; speech-to-text starts a chat poll | A, G, C / confirmed | Partial | No (archived 2020, 3 stars) |
| [Streamer.bot Voice Control](https://docs.streamer.bot/guide/voice-control) | Phrases the streamer configured trigger actions, including mid-sentence | A, C / confirmed | Partial | Yes (Streamer.bot) |
| [1up.vision Bingo](https://www.1up.vision/en/features/bingo) | Bingo board of stream events, marked by hand | A, G, C / confirmed | Partial–Adjacent | No counts found |
| [Blabla Radar Swear Jar](https://blablaradar.com/en/swear-jar) | Browser speech recognition counts words from the user's own list | A / verified | Partial | No |
| [obs-popup-overlay](https://github.com/erfur/obs-popup-overlay) | Offline speech recognition shows an image on one hotword | G / verified | Partial | No (0 stars) |
| [scpedicini/swearjar](https://github.com/scpedicini/swearjar) | Browser beep on a censored-word list | G / verified | Partial–Adjacent | No |
| [Don't Get Got](https://draughtslondon.com/ultimate-guide-to-the-dont-get-got-game/) (Big Potato party game) | Players hold secret missions, one of which is "get a player to say the word 'banana'"; played face to face, no Twitch | Extra search, 28 Oct / verified | Adjacent (same "make someone say it" goal, different medium) | Retail party game; no counts checked |
| [Heads Up! Phones Down (Twitch extension)](https://support.aspyr.com/hc/en-us/articles/22586269678093-Heads-Up-Phones-Down-Edition-Twitch-Extension-Overview) | The game picks a word hidden from the streamer; viewers type hints in chat; no listening to the streamer | Extra search, 28 Oct / verified | Adjacent | Aspyr product; no counts checked |
| AnkhbotSecretWord, Wordeous (19 Steam reviews), Kloot swear-jar counter, Taboo, Nightbot counters, LocalVocal (1.7k stars, captions only) | Secret word typed in chat; Taboo-style games; manual counters; speech-to-text building block | C, G, A / verified or common knowledge | Adjacent | LocalVocal only |

**Difference:** all three researchers say it survives. Every speech trigger found uses words the streamer chose; every viewer-chosen secret-word game runs in typed chat. A re-search in the link check found nothing closer.

**Demand**
- No direct request for this game (A, G, C).
- Indirect: streamers run manual swear jars and bingo cards (G: X posts, unverified; A: a channel's `!swear` command page). Two Reddit threads ask for mic word detection to trigger an effect (A, G; unverified, Reddit).

**Counter-signals**
- Trolls already try to make streamers say things on air ([Dexerto, 2019](https://www.dexerto.com/entertainment/korean-irl-streamers-baited-lewd-donation-prank-1045134/), C / verified). A tool that rewards steering the streamer into a word needs a word filter.
- faster-whisper hotwords can hallucinate on silence; the maintainer's fix is the VAD filter ([issue 1356](https://github.com/SYSTRAN/faster-whisper/issues/1356), A / verified).

**Audience fit:** any stream where the streamer talks: Just Chatting (14.2%) and IRL (1.8%), plus talkative game streams (share not measured). English speech-to-text as specified. Researchers disagree on "type-independent" (A yes if the streamer talks, G no, C mostly); they agree it depends on talk. Natural-setting demo: Yes (all three).

**Fact issues:** none contradicted. Create Clip with title and 5–60 s duration is supported. VAD is required.

**Proposed additions for the 12 h MVP (+2.5 h on top of the 9.5 h above):**

| Addition | Hours | What it does |
| --- | --- | --- |
| Fuse | 1 | If the match confidence is high, the mine explodes at once. If it is medium, a burning fuse and a 3 s ticking sound appear first; a mod or the streamer can cut it ("false alarm"). The threshold is tuned with the accuracy harness. |
| Sweep | 1 | The streamer has 3 sweeps per stream. Suspecting a trap, the streamer types the suspected word into the dock (saying it would set it off). If it matches a live mine, the mine is "SWEPT" and the planter's chip goes dark; if not, the sweep is lost. |
| Bomb Squad table | 0.5 | Kept across streams (SQLite): most explosions caused, longest-surviving mine, the streamer's sweep accuracy; shown with the dud reveal. |

---
