# Checkpoint: pivot draft

Draft for user approval. Written 2026-10-28. Card text is in [../cards.md](../cards.md) (section 10). Evidence is in [../evidence/](../evidence/).

## Rule recap

- Checkpoint's loop counts as the **same core loop** as the well-known [Meld X AMA Question Queue](https://meldstudio.co/gallery/x-ama-question-queue/): a viewer chats, the message is captured, the streamer picks it later, and it is shown on stream. That gives the card **one pivot chance** ([../evidence/README.md](../evidence/README.md)).
- A valid pivot changes at least one core-loop step (input, trigger or output), adds something the competitors lack at that step, is visible in the first 20 s of the video and fits ≤ 9.5 h of card MVP.
- If the user rejects every pivot, the card goes to scoring unchanged and the raters see Meld next to it.

## Candidates

What the competitors do at each step (checked on 2026-10-28):

| Step | Meld AMA queue | StreamerQnA | Social Stream Ninja | Senchabot featured msg |
| --- | --- | --- | --- | --- |
| Input | Message ending in `?`, or `!ask` | Configured chat command | Any message; operator clicks it | One viewer message |
| Trigger | Streamer clicks the next question | Streamer shows them one by one | Manual click or "Feature next message in queue"; an auto-feature toggle with no documented trigger | Manual |
| Output on stream | Question at the top of an on-screen list | Bubble overlay | Featured lower third | Message on screen |
| Back to the viewer | Nothing documented | Bot replies when the question is *submitted*, not when answered | Manual reply only: "Featuring a message does not reply to the viewer" | Not checked (unverified) |

None of them clips the answer, listens to the streamer, or reacts to what the streamer is doing.

### A. Clip receipt (the candidate already proposed)

**Step changed:** output to the viewer (step 4). *Before:* the bot replies in thread "✓ answered on stream at 12:04". *After:* when the streamer hits "next", the app creates a Twitch clip of the answer and the bot replies in thread with the clip link, so a viewer who left can still watch their answer.

**What competitors lack:** none of the four makes clips or sends anything to the viewer after an answer (table above). Clip bots do exist, for example [Fossabot `!clip`](https://docs.fossabot.com/commands/default/), which clips the stream on command and posts the link. What is new is tying the clip to one viewer's message and replying in that message's thread. So this is a new combination of two existing pieces.

**How the clip lines up with the answer:**
- *Create Clip (live):* the capture window is about 90 s around the API call: about 85 s before it and about 5 s after it. Calling at "next" with `duration` = answer length + 6 s should cover the answer. The docs do not say which part of the window `duration` selects when it is set through the API. The default publishes "the last 30 seconds", so we assume the last N seconds, but this is **unverified**. Answers longer than about 54 s get cut (the maximum is 60 s).
- *Create Clip From VOD* (generally available since 2026-02-05): `vod_offset` is the clip's **end**, so we can ask for exactly [card shown, "next" + 3 s]. It needs VOD storage (already on for markers), the live archive's `vod_id` from Get Videos, and a required `title`. Whether Get Videos lists the in-progress archive during the stream is **unverified**.
- Creation is asynchronous (HTTP 202). We poll Get Clips by `id` and send the reply once the clip appears.

**First 20 s:** the streamer answers Ana, hits next, and 5–15 s later Ana's chat shows "▶ your answer: clips.twitch.tv/…". A cut to the clip playing on Ana's phone makes it visible. As a plain chat line it is small and comes late.

**Hours:** +1.5 h (create, poll, VOD-offset path, reply, failure handling). Cut context thumbnails (1 h) and the reminder (0.5 h). MVP stays at **9 h**.

**Risks:** the clip window misses the start of the answer; clip processing delay at demo time; a clip is a link the viewer must open; the `duration` placement is undocumented; a fresh channel's clip settings (day-1 test T5).

**Effect on criteria:**
- Innovation: small gain. Clip-plus-link is a known pattern; only the per-message pairing is new.
- Impact: real gain. A viewer who left still gets the answer.
- Tech: gain (async API, timing math, VOD offsets).
- Design: neutral. A link in chat is not much to watch.

### B. Pause trigger: the checkpoint opens when the streamer comes up for air

**Step changed:** trigger (step 3). *Before:* the streamer must remember to hit "checkpoint" (a reminder nags after N minutes). *After:* the app notices a natural pause and opens the checkpoint on its own. The work source stops changing (a 64×36 `GetSourceScreenshot` diff at 2 Hz) **and** the mic picks up speech (`InputVolumeMeters`). A ring counts down "Checkpoint in 3…", and the countdown cancels if the work resumes. If the streamer goes back to work in the middle of a checkpoint, the remaining cards fold back into crystals.

**What competitors lack:** every competitor advances by a click, or by an auto-feature toggle with no documented trigger (Social Stream Ninja). None of them reads the streamer's activity.

**First 20 s:** inking, and 6 crystals stack. The streamer caps the pen, leans back and says "okay chat". The ring fills and CHECKPOINT fires without a button. Clearly visible.

**Hours:** pause detector 2 h (screenshot diff, mic level, hysteresis, tuning). Cut the reminder (0.5), scene auto-start (0.5), urgent lane (0.5) and context thumbnails (1). MVP becomes **8.5–9 h**.

**Risks:** false triggers when the streamer pauses to think, or missed triggers. It only works for visual work (games with animated menus never look "still"). The output is unchanged, so after the trigger the video still looks like a featured-message queue. That is the core of the Meld similarity.

**Effect on criteria:**
- Innovation: moderate gain.
- Impact: gain. Nothing to remember, which suits real heads-down use.
- Tech: gain (signal processing).
- Design: gain (the countdown ring is fun to watch).
- Weakness: the similarity to Meld stays in the part judges watch longest.

### C. Spoken answers with answer receipts (recommended)

**Steps changed:** the answer step (step 4), both its input and its output to the viewer.
- *Input before:* the streamer answers aloud, then takes a hand off the work to hit "next".
- *Input after:* the streamer just talks, hands still on the work. Local speech-to-text writes the words into the card as they are spoken. About 2 s of silence closes the card (a "next" or "skip" key is the fallback).
- *Output before:* "✓ answered on stream at 12:04".
- *Output after:* the bot replies in the viewer's thread with **what the streamer actually said**: "✓ answered on stream: 'It's a Micron 05, it doesn't bleed' (12:04)".

**What competitors lack:** none of the four listens to the streamer or sends the answer back. Social Stream Ninja can reply only when an operator types the reply by hand. A web search for a Twitch question tool that transcribes the streamer's answer found none. The nearest hits were tools where an **AI** answers chat with text-to-speech ([Twitch-OpenAI-TTS](https://github.com/skrrtn/Twitch-OpenAI-TTS)), which is the opposite direction. The answer lives in chat, so a viewer who scrolled away, left, or watches the VOD with chat replay still gets it.

**First 20 s:** Ana's card is up. The streamer keeps inking and says "Ana, it's a Micron 05, it doesn't bleed". The words type onto the card, the card stamps ✓ and flies off, and Ana's chat shows the threaded quote. Everything is visible inside 20 s, with no cut.

**Hours:** local speech-to-text 2 h and voice close 0.5 h. The receipt replaces the old reply ping at the same 0.5 h. Cut context thumbnails (1), urgent lane (0.5), reminder (0.5) and scene auto-start (0.5). MVP stays at **9 h** (table below).

**Risks:**
- A wrong word ends up in a viewer's quote. Mitigation: a 3 s undo before the quote is sent, plus "skip".
- The card closes on a thinking pause. Mitigation: a 2 s silence threshold plus a hold key.
- Transcription speed on the user's machine is unverified (add day-1 test T1b).
- The bot's message may be dropped by AutoMod or blocked terms (read `is_sent` / `drop_reason`).

Cutting thumbnails also removes the fact problem Astra raised: an OBS screenshot taken when a message arrives does not match the delayed video the viewer saw.

**Effect on criteria:**
- Innovation: largest gain. A queue that hears its answers is new, and it no longer reads as "Meld with extras".
- Impact: gain. Every viewer gets a written answer, and the streamer never lifts a hand.
- Tech: gain (live speech-to-text, segmenting, threaded replies). It reuses the speech-to-text work from test T1.
- Design: gain. The words typing onto the card and the ✓ fly-off are good to watch.

### D. Pinned to the work: viewers point at where their message is about

**Step changed:** input (step 2). *Before:* any normal message becomes a crystal in a corner badge. *After:* during focus a faint lettered grid sits over the work. A message with a cell code ("C4 why is this line thicker?") drops a crystal pinned on that spot of the canvas. At the checkpoint the card zooms into that region, so everyone sees what the question is about.

**What competitors lack:** none of the four is spatial. Click-on-video Twitch extensions such as Heat exist and are adjacent; **not checked in this pass**.

**First 20 s:** the grid fades in, colored pins pop onto the drawing, and the checkpoint zooms into pin C4. Very visual.

**Hours:** grid and parser 1 h, pin overlay replacing the badge (1.5 → 2 h), zoom crop 1 h. Cut thumbnails, urgent lane and reminder. MVP **≈ 9.5 h**, right at the cap.

**Risks:** cell codes are effectively a command, which breaks the card's "no command needed" promise. It only fits visual work. Viewers must learn the grid.

**Effect on criteria:**
- Innovation: gain.
- Design: gain.
- Impact: unclear (adds friction for viewers).
- Tech: neutral.

## Comparison table

| | A. Clip receipt | B. Pause trigger | C. Spoken answers + receipts | D. Pinned to the work |
| --- | --- | --- | --- | --- |
| Step changed | Output to the viewer | Trigger | Answer step: input (voice) + output (quote) | Input |
| Competitors lack it? | Yes for the 4 queues; clip bots exist | Yes | Yes; nothing similar found | Yes for the 4 queues; click extensions not checked |
| Visible in the first 20 s | Weak (link, delay, needs a cut) | Strong | Strong | Strong |
| Card MVP hours | 9 | 8.5–9 | 9 | ≈ 9.5 |
| Main risk | Clip timing, undocumented `duration` placement | False or missed triggers | Speech-to-text errors and speed | Viewers must use codes |
| Moves away from Meld? | A little (adds a tail step) | Partly (on-stream output unchanged) | Yes (both the answer and the return path are new) | Partly |
| Innovation | small + | + | ++ | + |
| Impact | + | + | + | ? |
| Tech | + | + | + | 0 |
| Design | 0 | + | + | + |

## Recommendation

**Pivot to C: spoken answers with answer receipts.** Add the clip from A as a **stretch** that arrives as a second threaded reply, not as part of the pivot.

Why:
1. It changes the step where Checkpoint and Meld differ most visibly. Meld's loop ends when the question is on screen. In C the loop continues: the stream hears the answer and sends it back in writing. No competitor does either half.
2. It serves the card's purpose better than the original. Answering by voice means the streamer never lifts a hand from the work, which is the most "heads-down without ghosting" version.
3. It shows on screen without a cut in the first 20 s. A's link needs a phone cut-in and a 5–15 s wait.
4. It costs the same 9 h, mostly by cutting context thumbnails, which had a latency fact problem anyway.
5. The clip is a coherent add-on to the receipt (the same reply thread, the same step), so it can be added later if day-1 test T5 passes and buffer hours remain. Its timing is not fully documented, so it should not carry the pivot.

B is the best fallback if the speech-to-text test fails. It is a cheap, visible trigger change, but it leaves the Meld-like output untouched.

## Rewritten core loop (recommended pivot)

1. The streamer hits a hotkey or a mod types `!focus`. A corner badge appears: "Focus: messages saved 0".
2. Each normal viewer message drops a save crystal in the viewer's color. Commands and bot lines are filtered out. The app keeps the message id, author, text and first-time flag.
3. The streamer hits "checkpoint". A lower-third call-in card shows the first saved message. Questions and first-time chatters come first.
4. The streamer answers aloud without stopping work. Local speech-to-text types the words onto the card as they are spoken.
5. When the streamer stops talking (about 2 s of silence), or hits "next", the card stamps ✓ and flies off. After a 3 s undo window, the bot replies in the viewer's thread: "✓ answered on stream: '<quote>' (12:04)". "Skip" closes the card without a receipt.
6. At the end: "Checkpoint cleared: 4 answered, 4 receipts sent".
7. *(Stretch)* When a clip of the answer is confirmed, a second threaded reply adds "▶ watch it: <clip link>".

## Revised MVP build parts

| Part | Hours | Change from the card |
| --- | --- | --- |
| Focus toggle (hotkey, mod `!focus`) + filter | 1 | Scene auto-start cut (−0.5) |
| Crystal badge overlay | 1.5 | Same |
| Call-in card overlay with live transcript line and ✓ stamp | 1.5 | Transcript line added in the same budget |
| Dock + ordering + next/skip/undo | 1 | Undo added |
| Local speech-to-text: mic capture, voice-activity segmenting, faster-whisper, partial updates | 2 | **New** |
| Voice close: silence rule, hold key, tuned on recorded audio clips | 0.5 | **New** |
| Answer receipt: trim the quote to fit 500 chars, reply in thread, handle `drop_reason` | 0.5 | Replaces the reply ping |
| Polish | 1 | Same |
| **MVP subtotal** | **9** | |
| Cut | | Context thumbnails (1), urgent lane (0.5), reminder (0.5), scene auto-start (0.5) |
| Stretch: clip link reply (Create Clip From VOD, falling back to Create Clip; poll Get Clips) | 1 | From A |
| Stretch: close on the next viewer's name; out-of-order matching | 0.5 | |
| Stretch: reminder back | 0.5 | |

New day-1 test **T1b:** 10 scripted spoken answers on the user's machine. Pass: quote ready ≤ 2 s after the streamer stops talking, and ≥ 9 of 10 quotes readable without edits.

**Codex artifact:** the voice-to-receipt pipeline, tested with recorded answer audio and simulated chat.

## Revised first-20-seconds video hook

- **0:00** Time-lapse of inking. Six colored crystals stack in the corner badge ("Focus: 6 saved").
- **0:05** The streamer taps the checkpoint key. The card reads "@ana (first time!): what pen is that?"
- **0:08** Still inking, the streamer says "Ana, it's a Micron 05, it doesn't bleed." The words type onto the card as they are spoken.
- **0:14** Silence. The card stamps ✓ and flies off.
- **0:16** Split screen of Ana's chat: a threaded reply appears, "✓ answered on stream: 'it's a Micron 05, it doesn't bleed' (12:04)".
- **0:19** The next card is already up.

Rest of the video:
- 0:20–1:00: two more cards, including one closed with "skip" and one undone.
- 1:00–1:30: a viewer who "left" opens chat later and finds the answer.
- 1:30–2:05: under the hood: segmenting, silence rule, reply threading.
- 2:05–2:30: the Codex artifact.
- 2:30: close.
- If the clip stretch is done, it gets 10 s around 1:00.

## Fact check list

Checked against the official docs on 2026-10-28 unless marked otherwise.

| # | Fact | Status | Source |
| --- | --- | --- | --- |
| 1 | Create Clip captures about 90 s around the call: about 85 s before and about 5 s after. The two Twitch pages disagree on the example: the reference says "2:35 to 4:05", the guide says "3:35 to 4:05". | Verified (the docs are inconsistent) | [Reference: Create Clip](https://dev.twitch.tv/docs/api/reference/#create-clip), [Clips guide](https://dev.twitch.tv/docs/api/clips/) |
| 2 | `duration` is a float from 5 to 60 with 0.1 precision, default 30. `title` is optional. A title that fails AutoMod returns 400. Both were added 2025-12-19. | Verified | [Reference](https://dev.twitch.tv/docs/api/reference/#create-clip), [Changelog 2025-12-19](https://dev.twitch.tv/docs/change-log/) |
| 3 | Which part of the 90 s window `duration` selects when set through the API. By default the last 30 s are published, so it is probably the last N seconds. | **Unverified** (test in T5) | Same |
| 4 | `has_delay` (shifts the window later) is still described in the clips guide but is gone from the current reference. | **Unverified** whether it still works; do not rely on it | [Clips guide](https://dev.twitch.tv/docs/api/clips/) |
| 5 | Creation is asynchronous: HTTP 202 returns `id` and `edit_url`, and you confirm with Get Clips `?id=`. The reference says to assume failure after 60 s; the guide says after 15 s. | Verified (the docs are inconsistent) | [Reference](https://dev.twitch.tv/docs/api/reference/#create-clip), [Clips guide](https://dev.twitch.tv/docs/api/clips/) |
| 6 | Scope: `clips:edit` on a user token. Create Clip From VOD needs `editor:manage:clips` or `channel:manage:clips`, requires a `title`, treats `vod_offset` as the clip's end, and has been generally available since 2026-02-05. | Verified | [Reference: Create Clip From VOD](https://dev.twitch.tv/docs/api/reference/#create-clip-from-vod), [Changelog](https://dev.twitch.tv/docs/change-log/) |
| 7 | Get Clips on a clip from the current broadcast may return an empty `video_id` and a null `vod_offset` for minutes. The `url` is usable earlier. | Verified (the `url` part is inferred) | [Clips guide](https://dev.twitch.tv/docs/api/clips/) |
| 8 | Rate limits: no clip-specific limit is documented. The general token bucket is per client ID per user per minute (the example header shows 800), and a 429 can also happen for other reasons. | Verified that no specific limit is documented | [API guide: rate limits](https://dev.twitch.tv/docs/api/guide/#twitch-rate-limits) |
| 9 | Clips on a tiny channel: the guide lists only two conditions: clips enabled, and follower/subscriber restrictions. No viewer minimum is documented. Create Clip returns 404 if the channel is not live and 400 if the category is not clippable. | Docs verified; real behavior on our new channel **unverified** (T5) | [Clips guide](https://dev.twitch.tv/docs/api/clips/), [Reference](https://dev.twitch.tv/docs/api/reference/#create-clip) |
| 10 | Moderators and editors are not limited by follower-only clip settings. | **Unverified** (third-party page quoting Twitch Support; the Twitch help page did not load) | [allthings.how](https://allthings.how/how-to-disable-clip-creation-on-twitch/) |
| 11 | Get Videos `type=archive` gives the VOD id. Whether the in-progress archive is listed during the stream is not stated directly; the Create Clip From VOD reference says a live stream "is actively creating a VOD". | **Unverified** (test in T5) | [Reference: Get Videos](https://dev.twitch.tv/docs/api/reference/#get-videos) |
| 12 | Send Chat Message: `reply_parent_message_id`, 500-character limit, response has `is_sent` / `drop_reason`, and `pin` cannot be combined with a reply. | Verified | [Reference: Send Chat Message](https://dev.twitch.tv/docs/api/reference/#send-chat-message) |
| 13 | Chat send limits: 20 messages per 30 s and 1 per second per channel for a normal account; 100 per 30 s if the bot is broadcaster, mod or VIP. Make the bot a mod. | Verified | [Chat docs: rate limits](https://dev.twitch.tv/docs/chat/#rate-limits) |
| 14 | obs-websocket `GetSourceScreenshot` can scale to ≥ 8 px and returns base64. `InputVolumeMeters` fires every 50 ms and is opt-in. `CurrentProgramSceneChanged` exists. (Candidate B) | Verified | [obs-websocket protocol.md](https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md) |
| 15 | Meld's AMA page says nothing about notifying the viewer, clips or recording the answer. Social Stream Ninja replies only by hand, does not reply on feature, and has no clips or speech-to-text. StreamerQnA replies only on submission. | Verified on the pages | [Meld](https://meldstudio.co/gallery/x-ama-question-queue/), [SSN dock guide](https://socialstream.ninja/docs/dock-live-guide.html), [StreamerQnA](https://github.com/chinzistor/StreamerQnA) |
| 16 | Senchabot Featured Message behavior after an answer. | **Unverified** (the evidence link points to a chat-poll setup page) | [Senchabot](https://extensions.senchabot.com/setup/chat-poll) |
| 17 | Fossabot `!clip` creates a clip of the live stream on command. | Verified (docs listing) | [Fossabot default commands](https://docs.fossabot.com/commands/default/) |
| 18 | Local faster-whisper speed and accuracy on the user's machine. | **Unverified** (new day-1 test T1b) | — |
| 19 | EventSub `channel.chat.message` carries the `message_id` needed for the reply. | Not rechecked here; shared-base assumption, confirmed by the evidence step for Send Chat Message replies | [Reference](https://dev.twitch.tv/docs/api/reference/#send-chat-message) |
