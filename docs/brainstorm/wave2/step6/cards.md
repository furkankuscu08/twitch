# Step 6: normalized cards (10 candidates)

Every card uses the same template and is written at its best variant. Scores from earlier steps are deliberately left out, because these cards are the input for blind evidence gathering and scoring. Features from eliminated candidates are marked **(absorbed)**.

Revision 2 (2026-10-26) applies the independent review in [cards-review.md](cards-review.md) and a 15-hour build budget. Revision 3 (2026-10-28) applies the evidence step ([evidence/aggregate.md](evidence/aggregate.md)): cards 5, 7 and 9 were eliminated by the user (their sections stay for the record), Checkpoint used its one pivot, and the other cards got fact fixes and named competitors only. What was accepted or changed is listed in the revision log at the end.

## Template

- **One-liner**
- **Best variant:** what is kept and what is dropped
- **Core loop:** at most 6 steps
- **Strengthening:** tagged with the criterion it answers, and how the card answers it
- **3-minute video:** beat sheet, ending before 2:55
- **Codex artifact:** one concrete thing Codex builds that the video can show
- **MVP:** in, stretch, out
- **Build parts:** card-specific hours, with an MVP subtotal and a stretch subtotal
- **Twitch surfaces, scopes and local parts**
- **Demo setup:** accounts, channels, hardware
- **Closest existing things and claimed difference:** to be checked in the evidence step
- **Risks and day-1 tests:** T-numbers refer to the test list below

## Shared constraints

- One streamer plus three test accounts.
- No commercial games or music in the video. Where a card's natural setting is a game, the demo uses a small original game built with Codex (about 1 h, paid from the 2 h buffer) or an MIT-licensed open-source game.
- No Twitch content kept beyond 24 h.
- **Budget: 15 build hours.** Recording and editing the video are not included. Every card is planned as shared base (3.5 h) + card MVP (at most 9.5 h), so at least 2 h stay free for debugging or stretch items.

## Shared base (same for every card, 3.5 h)

| Part | Hours |
| --- | --- |
| Twitch app, OAuth for broadcaster and bot, token refresh | 1 |
| EventSub WebSocket (chat, reconnect, 10 s subscribe window) + Send Chat Message | 0.5 |
| Local server (FastAPI), WebSocket push to OBS browser sources, OBS dock | 0.5 |
| obs-websocket connection and auth | 0.5 |
| **Chat simulator:** the three test accounts post a scripted chat over the real API (the Twitch CLI cannot mock chat messages). Used for rehearsal, tests and recording the demo. | 1 |

The chat simulator is Codex-built for every card and is the shared part of the Codex story. Each card adds its own Codex artifact.

## Twitch facts used across cards

These come from the reviewer's check of the Helix reference on 2026-10-26. The evidence step and the day-1 tests confirm them.

- **Create Clip** takes `title` and `duration` (5–60 s, default 30). The title must pass AutoMod. The clip is cut from Twitch's broadcast, not from a local OBS recording.
- **Create Stream Marker** fails unless the channel stores past broadcasts (VOD storage). Turn this on during setup.
- **Create Clip** captures the live output from roughly 85 s before to 5 s after the call and is asynchronous (confirm with Get Clips). Which part of that window `duration` keeps is not documented (T5).
- **`channel.raid`** gives the two channels and a viewer count, not the list of raiders. Individual raiders can only be recognized when they chat.
- **Pin Chat Message** is a documented endpoint (`moderator:manage:chat_messages`, 30–1800 s).
- **Whispers:** the phone-verified-sender rule covers whispers *sent through the API*. Whether viewers can whisper our bot from the Twitch client is a separate question that has not been tested.

## Day-1 tests

| Test | What it checks | Cards | Pass condition | filter.md # |
| --- | --- | --- | --- | --- |
| **T1** | Real-time local speech-to-text keyword spotting during a live stream | 1 | ≥80% hits, ≤1 false alarm per 10 min, ≤3 s lag, no dropped frames | #2 |
| **T1b** | Local speech-to-text of spoken answers (run in the same session as T1) | 10 | 10 scripted answers: quote ready ≤2 s after the streamer stops, ≥9 of 10 readable without edits | new (rev. 3) |
| **T2** | obs-websocket: replay buffer save + Media Source slow motion, screenshot, mute/silence events | 2, 3, 9 | Replay on screen ≤5 s after the command; screenshot ≤1 s; mute event arrives | #5 |
| **T3** | Second live channel + a real raid between the two | 4 | Both live; `channel.raid` arrives ≤5 s | #4 |
| **T4** | Sealed input: viewer → bot whisper, and the login page behind a public URL | 1, 8 | One path works end to end; whisper loss measured over 10 messages | #11 |
| **T5** | API checks in one script: Create Clip with title, Stream Marker, Pin, Get Chatters, Get Stream Markers | 1, 3, 5, 6, 7, 10 (stretch) | All return success on our new channel | low-risk list, #1 |
| **T6** | Local audio: onset detection and zero-shot audio-text scoring (CLAP) on desk sounds | 7 | Onset ≤200 ms, speech doesn't trigger; scores separate "right" from "wrong" sounds | new |
| **T7** | Read Developer Agreement IV.C | 4 (only if multi-day returns) | — | #12 |

---

## 1. Minefield

**One-liner:** Viewers secretly plant "word mines". When the streamer says a mined word out loud, it explodes on stream with the planter's name.

**Best variant:** Word mines with local speech-to-text. Dropped: Sound Tags, Try Not To Laugh, Sip Watch.

**Core loop:**
1. A viewer types `!mine`. The bot replies with a link to a plant page (Twitch login). Nobody else sees the word.
2. The overlay shows mine chips with owners' names, never the words. Rules: one live mine per viewer, 4+ letters, not a top-1000 common word, blocklist.
3. Viewers steer the conversation toward their word ("worst pizza topping?").
4. Local speech-to-text listens to the streamer's mic: faster-whisper (`base.en`/`small.en`) on a sliding ~2 s window, VAD on, live mines passed as `hotwords`, whole-word match on normalized text (plurals count).
5. Instant explosion, screen shake, the banner "Bo's mine: PINEAPPLE (planted 6 min ago)" and a stream marker. A mod can **DEFUSE** within 10 s: a rewind animation and a "false alarm" stamp, played as a gag. If not defused, a titled 30 s clip is created.
6. Unexploded mines flip over as "duds" at the end: "Cy's mine 'GIRAFFE' never went off".

**Strengthening (Impact):**
- It runs underneath normal talk, not as a separate mode, so it can stay on every stream.
- It gives quiet viewers a one-time action and a reason to talk *to* the streamer.
- **(absorbed) "Call it" mode (stretch):** viewers seal a prediction through the same plant page; envelopes open together at the reveal. One input system serves two games. Not shown in the video.

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

---

## 2. Tap on the Shoulder (production problems reach the streamer)

**One-liner:** Chat can't tap you on the shoulder while you're heads-down. Now it can: viewer reports and mod cues become a face on your desk, and chat confirms the fix.

**Best variant:** Tap on the Shoulder (report detection and mod cues) with a simplified Soundcheck confirm loop, and **(absorbed)** Desk Buddy as the signal device. Dropped: the lamp.

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

**Strengthening (Design and Technical):**
- *Design:* the signal is on camera, so viewers watch their report reach the room. The confirm step is one emoji, not a command.
- *Technical:* a distinct-user detector, mod authentication, an obs-websocket cross-check and a delay-aware confirmation, rather than a single threshold.
- *Innovation:* it covers problems OBS can't see (a mic turned away, a bad game/voice balance), because the sensor is the audience.

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

---

## 3. VAR

**One-liner:** When chat disputes a moment, two `!var` calls start a broadcast-style review: slow-motion replay, a 15-second chat jury, a verdict stamp, and a titled clip.

**Best variant:** As designed, plus "Self-VAR". The replay is only the means; the verdict is the show.

**Core loop:**
1. The streamer claims something ("IN!").
2. Two distinct viewers type `!var` within 30 s. The threshold scales with active chatters, and mods or the streamer can also call it.
3. A "VAR CHECK" stinger plays. obs-websocket saves the 60 s replay buffer.
4. An OBS Media Source, driven by obs-websocket, plays the last ~10 s shifted by a latency offset, with the last 4 s at half speed.
5. Chat votes `!yes` or `!no` for 15 s; names appear on a jury bench.
6. The verdict stamp lands. Then the app creates a 60 s clip titled "VAR: NO BASKET" and a marker. The clip holds the review, and the review holds the replay of the moment.

**Strengthening (Impact):**
- "Dispute" is broader than sports: trick shots, speedrun claims, board games, cooking ("is it raw?"), art ("did they trace it?").
- **Self-VAR:** the streamer calls VAR on their own bold claim and chat can overturn it, a recurring bit for any stream.
- Each review leaves a ready-made, titled highlight clip, which matters for small streamers' short-form reach.

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

---

## 4. Raid Torch

**One-liner:** A torch that only travels by raid: every chat that holds it leaves a mark, and the raiders who carried it light up when they chat on arrival.

**Best variant:** A same-day relay with a visible journey and torch-bearers. Dropped: G-7 (an activity carried into the next stream) and the multi-day journey. Fallback: a one-sided send-off.

**Core loop:**
1. Channels join a circle with a code, on a hosted backend.
2. While a channel holds the torch, each chatter adds one mark with `!mark <emote>`, and rings grow on the torch. Twitch-native emotes render as images; third-party emotes show as text.
3. The streamer raids. EventSub `channel.raid` hands the torch over.
4. On the target's overlay, the torch flies in with its rings and a journey map ("3 channels, 14 marks tonight").
5. **Torch-bearers:** a raider who added a mark glows when they first chat in the new channel ("Ana carried a mark from A"). The target streamer sees which torch-bearers arrived; Twitch's raid event gives only a count, so raiders without a mark stay anonymous.
6. A public journey page shows tonight's path. It resets after the evening.

**Strengthening (Impact):**
- Torch-bearers give the receiving streamer something useful on every raid: which marked raiders arrived and where they came from.
- The audience is raid trains, Twitch teams and small-streamer circles, which already coordinate raids on the same evening.
- **One-sided fallback:** if the target doesn't run the tool, the raiding channel still shows a "torch passed to X" send-off and the journey page records the hop.

**3-minute video:**
- 0:00 Hook: channel A's torch glowing, the raid, cut to channel B: the torch flies in, raiders' names glow as they chat "we brought that!".
- 0:25 How marks are added.
- 0:50 The journey map with three hops (two rehearsal hops, labeled as such) and the public page.
- 1:30 Torch-bearers from the host's view.
- 2:00 How the hosted backend links channels.
- 2:30 Codex artifact, close.

**Codex artifact:** the hosted backend with its deploy, and the journey page.

**MVP:**
- **In:** circle code, `!mark`, torch overlay, raid handoff, fly-in, torch-bearers, journey page, hosted backend.
- **Stretch:** one-sided send-off, pinned arrival message.
- **Out:** multi-day journeys, multiple torches, leaderboards.

**Build parts:**

| Part | Hours |
| --- | --- |
| Hosted backend + circle state + deploy (free PaaS) | 2.5 |
| Raid events for circle channels | 0.5 |
| `!mark` with emote fragments | 0.5 |
| Torch overlay with rings + fly-in | 2.5 |
| Torch-bearers | 1 |
| Journey page | 1.5 |
| Polish | 1 |
| **MVP subtotal** | **9.5** |
| Stretch: send-off 0.5, pinned arrival 0.5 | 1 |

**Twitch surfaces, scopes and local parts:** EventSub `channel.raid` (no authorization needed) and `channel.chat.message` in each circle channel, Get Users (avatars), optional Start a Raid and Pin Chat Message; OBS browser source; a hosted backend with a public URL.

**Demo setup:** 1 streamer + 3 test accounts, and **a second live channel** (a test account streaming from a phone or a second OBS).

**Closest existing things and claimed difference:** raid alerts; raid-train tools (R3dLabs Toolbox Stream Deck plugin, RaidRunner scheduling and lineups); RaidPort (beta: streamers raid a hub channel and a wheel picks the next raid); Teams+ (TwitchCon Hackathon 2019: trusted-viewer labels shared across a Team); organised relays and raid-train communities (Twitch Storm 2020, Raid Train Central). *Difference:* state carried across channels; the raid becomes a visible object, and marked raiders are recognized when they chat on arrival.

**Risks and day-1 tests:**
- Second live channel and a real raid (T3).
- One person's two channels may not make "community relay" feel real.
- Value depends on both sides adopting it; the send-off is the one-sided fallback.
- Hate raids made small streamers wary of raids; only channels that joined the circle with its code take part.
- Many raiders leave quickly; torch-bearers only light up for those who chat.

---

## 5. Previously On

**Eliminated in revision 3** (user decision after the evidence step). Kept for the record.

**One-liner:** When raiders arrive, or a late viewer asks, the stream plays a 10-second TV-style "Previously on…" recap built from beats dropped during the stream.

**Best variant:** The overlay recap (L1-3), plus the pinned recap (Story So Far), now that Pin Chat Message is a documented endpoint.

**Core loop:**
1. During the stream, beats come from habits the streamer already has: every stream marker (Twitch's marker shortcut, a Stream Deck) becomes a beat, read every 30 s with Get Stream Markers. A hotkey or a mod's `!beat Beat the frog king on try 9` also adds one. Title and category changes become beats automatically.
2. On an incoming raid, the overlay runs a TV bumper: "Previously on…", the last three beats with timestamps and the current goal.
3. A late viewer types `!recap`. The bot posts a compact version and pins it for 10 minutes.
4. **(absorbed)** A first-time chatter gets one quiet chat reply with the current goal and `!recap`, never an on-screen spotlight.
5. **(absorbed, stretch)** A channel glossary: mods add a few lore terms, and the first mention of a term on a recap card gets a footnote.

**Strengthening (Impact; "not a fancy raid alert"):**
- A raid alert greets the raider; this briefs the raiders.
- Small channels rarely get raids, so daily use is `!recap`, the pinned recap and the first-chatter reply: context for anyone new.
- Reading existing markers means the streamer doesn't have to learn a new habit.

**3-minute video:**
- 0:00 Hook: a raid lands, the screen dims, "PREVIOUSLY ON" sweeps in, a raider types "ahh ok, frog king".
- 0:25 Dropping beats: the marker shortcut and a mod command.
- 0:55 A late viewer's `!recap`, the pinned recap, "ohh ok".
- 1:30 A first-time chatter's quiet reply.
- 2:00 The glossary footnote moment (if built), otherwise how beats come from markers.
- 2:30 Codex artifact, close.

**Codex artifact:** the TV bumper animation system, and the beat pipeline tested with simulated raids and chat.

**MVP:**
- **In:** beats (markers, hotkey, mod command, auto), raid bumper, manual trigger, `!recap`, pinned recap, first-chatter reply.
- **Stretch:** glossary footnote (first mention only).
- **Out:** LLM-generated beats or summaries.

**Build parts:**

| Part | Hours |
| --- | --- |
| Beat store + commands + marker polling + auto-beats | 2 |
| Hotkey/dock | 1 |
| Raid EventSub + CLI mock | 0.5 |
| Bumper overlay | 2.5 |
| `!recap` + pin + first-chatter reply | 1.5 |
| Polish | 1 |
| **MVP subtotal** | **8.5** |
| Stretch: glossary footnote 1 | 1 |

**Twitch surfaces, scopes and local parts:** EventSub `channel.raid`, `channel.chat.message`, `channel.update`; Get Stream Markers (`user:read:broadcast`), Create Stream Marker (`channel:manage:broadcast`, VOD storage on), Send Chat Message, Pin Chat Message (`moderator:manage:chat_messages`); OBS browser source.

**Demo setup:** 1 streamer + 3 test accounts. Webcam and mic. A real raid needs a second live channel; the CLI mock works for rehearsal.

**Closest existing things and claimed difference:** raid alerts and auto-shoutouts (they greet the raider); a hand-pinned "today's plan"; custom `!lore` commands; AI "what did I miss" summarizers; Twitch's automatic VOD chapters on category changes. *Difference:* a human-curated, TV-style briefing aimed at newcomers, triggered by their arrival, with no AI summary.

**Risks and day-1 tests:**
- Streamers may not drop beats; markers and auto-beats reduce this.
- Real raid (T3) or CLI mock.
- Pin and markers on a new channel (T5).

---

## 6. Studio Audience

**One-liner:** Chat becomes a live theater crowd you can hear. Every laugh belongs to a real, named viewer, and it only gets louder when more people react.

**Best variant:** As designed, with chants in the MVP. **(absorbed)** Lurker seats are a stretch and stay out of the video.

**Core loop:**
1. Emotes and keywords map to five reactions: laugh, gasp, aww, applause, boo.
2. A crowd engine mixes CC0 samples. Intensity scales with *distinct* reacting viewers, so spam can't inflate it, and the crowd never sounds bigger than the number of real reactors.
3. Each viewer has a signature laugh: a sample from a pool, a playback rate and an EQ, all derived from their user ID (changeable with `!mylaugh 7`). It rises out of the crowd, and their named seat silhouette bounces.
4. The same word from 2+ viewers within 10 s becomes a chant with the word on screen.
5. A follow brings applause; a raid opens the doors and adds seats.
6. A headphone-only mode lets the streamer hear the room without putting it on stream.

**Strengthening (Innovation):**
- Sound alerts play one clip per trigger. This is one mixed, scaled crowd from free actions, with every voice traceable to a named viewer.
- Honest scaling is part of the design: no fake crowd, only real reactors.
- The headphone-only mode makes it a perception tool (hear chat mid-task), not only a gag.

**3-minute video:**
- 0:00 Hook: a missed paper-ball shot, "L" and "LUL", the crowd boos then laughs, three named seats bounce.
- 0:20 Signature laughs, so you hear who is laughing.
- 0:50 A chant forms, the word on screen.
- 1:15 A raid opens the doors.
- 1:40 Headphone mode shown as a picture-in-picture "what the streamer hears", with a waveform.
- 2:05 How mixing and scaling work; every voice traceable.
- 2:30 Codex artifact, close.

**Codex artifact:** the Web Audio crowd mixer, tuned with the chat simulator sending bursts of different sizes.

**MVP:**
- **In:** 5 reactions, 20+ CC0 samples, distinct-viewer scaling, signature laughs, seat strip, chants, follow and raid events, monitor-only toggle, volume cap.
- **Stretch:** lurker seats (silent logged-in chatters in dim seats, bots filtered; a seat lights on first reaction).
- **Out:** TTS chants, viewer-recorded audio.

**Build parts:**

| Part | Hours |
| --- | --- |
| Chat mapping | 1 |
| Web Audio crowd mixer + scaling | 2.5 |
| Signature laughs (sample × rate × EQ per ID) | 1 |
| Seat strip overlay | 2 |
| Chants | 0.5 |
| Follow and raid events | 0.5 |
| Monitor mode + picture-in-picture view | 0.5 |
| Polish | 1 |
| **MVP subtotal** | **9** |
| Stretch: lurker seats 1 | 1 |

**Twitch surfaces, scopes and local parts:** EventSub chat, `channel.follow` (`moderator:read:followers`), `channel.raid`; Get Chatters (`moderator:read:chatters`, stretch); OBS browser source with audio.

**Demo setup:** 1 streamer + 3 test accounts. Headphones, mic, webcam. Three accounts make at most three voices; a larger crowd can only be shown with the chat simulator, labeled as a simulation in the video.

**Closest existing things and claimed difference:** Sound Alerts and Blerp (viewer-triggered sounds, one clip per trigger); per-viewer entrance sounds (Streamer.bot Walkon Sounds, Blerp walk-ons); Meld Emote Storm and StreamElements' KappaGen (visual scaling with chat); hand-fired laugh tracks (Elgato sound packs, emote soundboards). Per-viewer sounds already tie a noise to a viewer. *Difference:* one mixed crowd you hear, scaled by the number of distinct reactors, with recurring voices tied to named viewers and chants.

**Risks and day-1 tests:**
- The delight may fade after 10 minutes.
- It may read as "canned laughter / fake engagement"; traceability is the answer and leads the pitch.
- Get Chatters for the stretch (T5).
- Sound spam is a known complaint about sound alerts; distinct-viewer scaling and the volume cap are the answer.

---

## 7. Foley Pit

**Eliminated in revision 3** (user decision after the evidence step). Kept for the record.

**One-liner:** Chat writes the sound-effects score, the streamer performs it with a cup and a spoon, and an audio model judges how much the spoon sounded like footsteps.

**Best variant:** Foley Pit with a Foley meter. Variants (Prop Jury, Bench Test) are dropped.

**Core loop:**
1. The streamer opens a scene card ("A tiny detective enters a storm").
2. Three viewers claim a role (weather, footsteps, surprise) and pick one cue from a small vocabulary.
3. The three-beat score fills in on screen and locks.
4. The streamer advances beat by beat and performs each sound with desk objects. Local onset detection finds each performed sound.
5. **Foley meter:** a zero-shot audio-text model (CLAP) scores the sound against its cue text: "spoon footsteps: 71% footsteps". The beat lights up with its score.
6. The scene ends with a Foley score and a one-word chat verdict, and the app creates a titled "foley reel" clip.

**Strengthening (Technical and Impact):**
- *Technical:* a local audio pipeline (onset detection → audio embedding → similarity to the cue text) turns a performance into a scored game.
- *Impact:* a recurring segment with a scene deck, suited to Just Chatting, intermissions, ASMR, music and maker streams. ASMR trigger requests are the closest real habit.

**3-minute video:**
- 0:00 Hook: the scene card, three cues, paper rain, spoon footsteps "71% footsteps", an absurd cup thunderclap "CUP THUNDER: 12% thunder", chat laughs.
- 0:30 How roles are claimed.
- 1:00 A second scene with a better performance and a higher score.
- 1:40 The final score, the chat verdict and the reel clip.
- 2:05 How the audio model judges, running locally.
- 2:30 Codex artifact, close.

**Codex artifact:** the audio scoring pipeline and its calibration script (scores for right and wrong sounds per cue).

**MVP:**
- **In:** 3 roles, 6 scene prompts, cue vocabulary, score lock, conductor advance, onset detection, Foley meter, final score and verdict, titled reel clip.
- **Stretch:** viewer-submitted scenes, best take of the stream.
- **Out:** generated audio, music.

**Build parts:**

| Part | Hours |
| --- | --- |
| Role claim + cue vocabulary | 1.5 |
| Score overlay | 2 |
| Conductor dock | 1 |
| Onset detection (Python) | 1 |
| Foley meter: CLAP scoring + calibration | 2 |
| Verdict + clip | 0.5 |
| Polish | 1 |
| **MVP subtotal** | **9** |
| Stretch: viewer scenes 1, best take 0.5 | 1.5 |

**Twitch surfaces, scopes and local parts:** EventSub chat, Send Chat Message, Create Clip (`clips:edit`); OBS browser source and dock; local mic analysis and a local audio-text model.

**Demo setup:** 1 streamer + 3 test accounts. Mic, webcam, desk objects.

**Closest existing things and claimed difference:** viewer-triggered sound effects (playback); ASMR trigger requests via channel points; Whose Line's "Sound Effects" game; improv games. *Difference:* the audience writes the score, the streamer performs it, and a model judges the performance.

**Risks and day-1 tests:**
- The streamer must enjoy performing.
- Model scores may feel random; calibrate per cue (T6).
- Repeat value is unvalidated (test with three scenes).

---

## 8. Hint Jar

**One-liner:** On first (blind) playthroughs, viewers who know the answer seal tiered hints into a jar instead of backseating. The streamer opens only the tier they want, when they want it.

**Best variant:** Hint Jar (L1-5) with Hint Airlock's mod classification (G-1). Hints go in through a private page, not public chat. The demo runs on a small original puzzle game built with Codex.

**Core loop:**
1. A viewer types `!hint` and gets a link to a hint page (Twitch login), where they pick a tier (nudge, method, answer) and write the hint.
2. Optionally, a mod approves each hint and corrects its tier on a private dock.
3. The overlay jar fills with envelopes by tier: "Nudge 2 · Method 1 · Answer 1".
4. The streamer says "okay, one nudge" and hits a hotkey. One nudge opens with its author; the answer stays visibly sealed.
5. If solved, "@ana saved the run ⭐". The same nudge from two viewers credits both.

**Strengthening (Technical and Impact):**
- *Technical:* private intake, a mod classification queue, tiered reveal logic and duplicate merging.
- *Impact:* backseating, a well-known pain, becomes help the streamer controls. The original puzzle game makes the demo a real blind playthrough without a commercial game.

**3-minute video:**
- 0:00 Hook: a backseat line "IT'S THE LEFT DOOR" in chat, the bot answers "seal it instead: !hint", the jar shows "3 hints sealed"; the stuck streamer taps once, a nudge opens, the answer stays sealed.
- 0:25 How viewers submit privately.
- 0:55 The mod reclassifies a "nudge" that is really the answer.
- 1:25 The second tier, solved, credit.
- 2:00 Under the hood, and the puzzle game Codex built for the demo.
- 2:35 Close.

**Codex artifact:** the demo puzzle game itself, plus the tool.

**MVP:**
- **In:** hint page, tiers, mod dock, jar overlay (simple physics or CSS stacking), reveal hotkey, credit, duplicate merging, demo puzzle game.
- **Stretch:** whisper intake (if T4 passes), a chat vote to open a nudge early.
- **Out:** automatic spoiler detection, commercial game integration.

**Build parts:**

| Part | Hours |
| --- | --- |
| Hint page with Twitch login + public URL | 1.5 |
| Mod dock | 1.5 |
| Jar overlay | 1 |
| Reveal logic + hotkey | 1 |
| Credit + merging | 1 |
| Demo puzzle game | 1.5 |
| Polish | 1 |
| **MVP subtotal** | **8.5** |
| Stretch: whisper intake 0.5, chat vote 0.5 | 1 |

**Twitch surfaces, scopes and local parts:** EventSub chat (`user.whisper.message` in stretch), Get Moderators (`moderation:read`), Send Chat Message; OBS browser source and dock; a public URL.

**Demo setup:** 1 streamer + 3 test accounts (one as mod). Webcam and mic. The Codex-built puzzle game.

**Closest existing things and claimed difference:** no-backseating rules and help safe words; LeagueBackseat (queues backseat messages); channel-point backseat rewards and paid backseat windows; Backseat Me (Channel Points Hackathon 2021: points buy temporary control); Universal Hint System (offline tiered hints since 1988); Chat Curtain (shows only mod-approved messages). *Difference:* the help is tiered, gated by the streamer and revealed as a show.

**Risks and day-1 tests:**
- Sealed intake (T4).
- Backseating complaints are common, but many say rules and bans are enough, and some viewers want no hints at all. The jar is where unwanted hints go; the streamer may never open it.
- Twitch's tag is "First Playthrough" ("Blind Playthrough" was removed in 2020); use that wording in the video.
- The demo puzzle must feel like a real playthrough.

---

## 9. Photo Booth

**Eliminated in revision 3** (user decision after the evidence step). Kept for the record.

**One-liner:** Meet-and-greet for every viewer: type `!snap`, and you and the streamer pose together in a Polaroid that develops live, and the whole chat ends up on the corkboard.

**Best variant:** A photo *with* the viewer: their Twitch avatar is composited into the frame next to the streamer. The raid group photo is in the MVP. Dropped: ticket stubs, the museum.

**Core loop:**
1. A viewer types `!snap first win` (once per stream). The streamer hears a cue and leaves room in the frame.
2. The overlay counts 3-2-1; obs-websocket grabs the frame (the camera, or a "booth" scene).
3. The app places the viewer's avatar beside the streamer. A Polaroid develops over 5 s, captioned "Ana · first win · Oct 30". The viewer gets a link that expires after 24 h.
4. A raid triggers a group photo with all raiders' avatars squeezed in.
5. The outro shows a corkboard collage: "4 of us were here today".

**Strengthening (Innovation):**
- The viewer is *in* the photo, not just named under it, like a TwitchCon meet-and-greet.
- The raid group photo and the end collage turn single snaps into a channel ritual.
- A consent toggle: the streamer can blur their face or capture only a booth scene.

**3-minute video:**
- 0:00 Hook: `!snap`, the streamer leans toward an empty spot, the flash fires, the Polaroid develops with Ana's avatar beside them.
- 0:25 The viewer opens their link on a phone.
- 0:45 The raid group photo.
- 1:15 The end-of-stream collage.
- 1:45 How frames are captured, composited and expire; the consent toggle.
- 2:25 Codex artifact, close.

**Codex artifact:** the compositor that places avatars into the frame and builds the collage.

**MVP:**
- **In:** snap command, countdown, capture, avatar composite, Polaroid, caption, link page with 24 h expiry, raid group photo, collage, consent toggle.
- **Stretch:** face-aware avatar placement (face detection), physical print.
- **Out:** AI stylization.

**Build parts:**

| Part | Hours |
| --- | --- |
| obs-websocket screenshot | 0.5 |
| Avatar composite | 1.5 |
| Polaroid overlay | 2 |
| Queue/cooldown | 0.5 |
| Link page on a hosted backend + expiry | 1.5 |
| Raid group photo | 1 |
| Collage outro | 1 |
| Consent toggle | 0.5 |
| Polish | 1 |
| **MVP subtotal** | **9.5** |
| Stretch: face-aware placement 1 | 1 |

**Twitch surfaces, scopes and local parts:** EventSub chat and raid, Get Users (`profile_image_url`), Send Chat Message; OBS browser source; obs-websocket; a hosted link page (a tunnel dies when the PC sleeps).

**Demo setup:** 1 streamer + 3 test accounts. Webcam and mic.

**Closest existing things and claimed difference:** StreamUP's "Polaroid Picture" for Streamer.bot (a channel-point redeem takes a Polaroid of an OBS source; reported by the reviewer, to be verified); generic chat-to-overlay commands; physical subscriber-slip printers. *Difference:* the viewer appears in the photo with the streamer, the raid becomes a group photo, and the stream ends with a collage of everyone who was there.

**Risks and day-1 tests:**
- obs-websocket screenshot (T2).
- Hosting for the link page.
- Streamers may not want their face in shared links; the consent toggle answers this.
- Novelty against StreamUP (evidence step).

---

## 10. Checkpoint

**One-liner:** Go heads-down without ghosting chat: messages become save crystals, and at the checkpoint the streamer answers out loud, the words type onto the card, and each viewer gets a threaded reply quoting what the streamer said.

**Best variant:** Checkpoint with spoken answers and answer receipts (revision 3 pivot, see [pivots/checkpoint-draft.md](pivots/checkpoint-draft.md), candidate C). Fallback if day-1 test T1b fails: the pause trigger (candidate B).

**Core loop:**
1. The streamer hits a hotkey or a mod types `!focus`. A corner badge: "Focus: messages saved 0".
2. Each normal viewer message drops a save crystal in the viewer's color. Commands and bot lines are filtered out. The app keeps the message id, author, text and first-time flag.
3. The streamer hits "checkpoint". A lower-third call-in card shows the first saved message. Questions and first-time chatters come first.
4. The streamer answers aloud without stopping work. Local speech-to-text (faster-whisper) types the words onto the card as they are spoken.
5. About 2 s of silence, or "next", closes the card: it stamps ✓ and flies off. After 3 s the bot replies in the viewer's thread: "✓ answered on stream: 'It's a Micron 05, it doesn't bleed' (12:04)". If the transcript is empty or low-confidence, the reply drops the quote: "✓ answered on stream (12:04)". "Skip" closes the card with no reply.
6. At the end: "Checkpoint cleared: 4 answered, 4 receipts sent".
7. *(Stretch)* When a clip of the answer is confirmed, a second threaded reply adds "▶ watch it: <clip link>".

**Strengthening (Innovation, Impact and Design):**
- *Innovation:* question queues end when the question is on screen. Here the stream hears the answer and sends it back in writing. None of Meld, StreamerQnA, Social Stream Ninja or Senchabot listens to the streamer or replies after an answer.
- *Impact:* the streamer never lifts a hand from the work, and every viewer gets a written answer in their own thread, even if they scrolled away, left, or watch the VOD with chat replay.
- *Design:* the words typing onto the card and the ✓ fly-off are the moment to watch.
- No command needed and no AI summary: every message keeps its author and gets the streamer's own words.

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

**Closest existing things and claimed difference:** Meld X AMA Question Queue (same core loop up to the featured question; well-known, so this card used its one pivot), StreamerQnA, Social Stream Ninja featured message, Senchabot featured message, Chatterino highlights. *Difference:* the streamer answers by voice without lifting a hand, and each viewer receives the streamer's actual words as a threaded reply.

**Risks and day-1 tests:**
- Speech-to-text speed and accuracy on the user's machine (T1b). If it fails, switch to the pause-trigger fallback.
- A thinking pause closes the card early: 2 s threshold plus a hold key.
- A misheard word in a viewer's quote: the confidence gate sends the plain receipt instead.
- AutoMod or blocked terms drop the reply: read `drop_reason`.

---

## Revision log

**Revision 2, 2026-10-26.** Source: [cards-review.md](cards-review.md) (independent Opus reviewer that read only cards.md, rules.md and A-capabilities.md). Budget raised from ~10 to 15 build hours by the user.

Template and shared changes:
- A shared base (3.5 h) replaces the per-card "EventSub chat + bot" lines; each card lists only its own parts, with MVP and stretch subtotals.
- A Codex-built chat simulator is part of the shared base.
- Each card names one concrete Codex artifact.
- Each strengthening section is tagged with the criterion it answers.
- Scopes, hardware and T-numbered day-1 tests are on every card.
- Twitch facts corrected: Create Clip title and duration (5–60 s), markers need VOD storage, Pin Chat Message exists, the whisper phone rule covers API senders.
- Missing competitors from the review were added to each card; they are checked in the evidence step.

Per-card changes:
- **Minefield:** instant explosion with a 10 s mod DEFUSE; titled clip in the MVP; spotter specified (hotwords, sliding window, VAD); accuracy harness; "Call it" stays a stretch but leaves the video; whisper intake moved to stretch; friends plant real words to avoid a staged look.
- **Tap:** new one-liner; second hook case OBS can't see ("far away"); the bot's 👍/👎 prompt replaces `!heard B`; obs-websocket check in the MVP; lamp dropped; HTTPS for the phone page.
- **VAR:** replay through an OBS Media Source; shorter review (10 s replay, 15 s vote); 60 s titled clip; Self-VAR as the second case; history strip as a stretch.
- **Raid Torch:** new one-liner; same-day relay by default (no Developer Agreement dependency); torch-bearers; hosted backend; three-hop map in the video; one-sided mode is now a fallback, not a headline.
- **Previously On:** beats from existing markers via Get Stream Markers; pinned recap in the MVP; glossary cut to a first-mention footnote stretch; markers/VOD beat replaced.
- **Studio Audience:** reframed around real, named viewers; chants in the MVP; headphone mode shown as picture-in-picture; signature laughs via sample × rate × EQ; lurker seats are a stretch, out of the video; scopes added.
- **Foley Pit:** new one-liner; CLAP Foley meter; titled reel clip in the MVP; ASMR named as the closest habit; emote rating replaced by score + verdict.
- **Hint Jar:** Codex-built puzzle game for the demo; simpler jar overlay; whisper intake only as a stretch; new hook; chat vote as a stretch.
- **Photo Booth:** pivot to a photo with the viewer (avatar composite); raid group photo in the MVP; consent toggle; hosted link page; StreamUP named as the closest competitor.
- **Checkpoint:** new one-liner; context thumbnails; threaded reply ping; urgent lane in the MVP; the "why it isn't a question queue" beat removed.

Not taken from the review: none dropped outright. The VAR history strip and the Hint Jar chat vote were kept only as stretch items.

**Revision 3, 2026-10-28.** Source: the evidence step ([evidence/](evidence/)) and the pre-registered pivot rule in [evidence/README.md](evidence/README.md).

- **Eliminated by the user after the evidence step:** Previously On (Twitch shipped mid-stream AI summaries and Recaps in 2026), Photo Booth (StreamUP Polaroid Picture), Foley Pit (no demand found; CLAP scores correlate poorly with human judgment). Their sections stay above for the record.
- **Decision:** a commercial game is not needed in the video; the on-screen activity can be a small Codex-built original game or an MIT-licensed open-source game.
- **Shared:** demo games allowed (Codex-built or MIT-licensed, paid from the buffer); Twitch facts added for the Create Clip window and the `channel.raid` payload; T3 now lists only Raid Torch.
- **Minefield:** competitors named (OK Gamers, Streamer.bot Voice Control, swear-jar tools, Wordeous, AnkhbotSecretWord) with the difference sentence; risks: baiting trolls (blocklist), hotword hallucination on silence (VAD).
- **Tap:** "muted" and "silent" are separate OBS signals; the confirmation says "chat confirmed" because latency differs per viewer; well-known OBS plugins named (Muted Notification, Remember to Talk); demo game for the fullscreen case; counter-signal noted.
- **VAR:** competitors named (tomaae replay, BarRaider, Fyre, Glitch Studios, Senchabot, Streamer's Court); optional demo game with close calls; interruption risk noted.
- **Raid Torch:** the raid event has no raider list, so only marked raiders who chat are recognized (one-liner and step 5 corrected); RaidPort, Teams+ and relays named; hate-raid and early-leave risks noted.
- **Studio Audience:** per-viewer sound tools named (Streamer.bot walk-ons, Blerp); three accounts make three voices, so a larger crowd is shown only as a labeled simulation; sound-spam risk noted.
- **Hint Jar:** competitors named (Backseat Me, Universal Hint System, Chat Curtain, paid backseat windows); counter-signals and "First Playthrough" wording noted.
- No new features were added to the cards above; the only design change in revision 3 is the Checkpoint pivot.
- **Checkpoint pivot (its one pivot under the rule):** the user ruled its loop the same core loop as the well-known Meld X AMA Question Queue. Candidates were drafted by an Opus subagent in [pivots/checkpoint-draft.md](pivots/checkpoint-draft.md); the user approved candidate C, spoken answers with answer receipts. Added on review: a confidence gate that sends the plain receipt when the transcript is weak, and the bot as moderator for chat limits. Cut: context thumbnails, urgent lane, reminder, scene auto-start. New day-1 test T1b. MVP stays at 9 h.
