## Scores
| Card | Innovation | Impact | Tech | Design | Total | Risk | Risk depends on |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Tap on the Shoulder | 3 | 4 | 4 | 4 | 15 | Medium | T2 mute/silence threshold |
| Minefield | 5 | 3 | 3 | 5 | 16 | High | T1 spotter hits, false alarms, and lag |
| VAR | 3 | 3 | 4 | 5 | 15 | Medium | T2 replay on screen and the latency offset |
| Hint Jar | 4 | 3 | 3 | 4 | 14 | Low | T4 sealed hint page |
| Checkpoint | 3 | 4 | 3 | 4 | 14 | Medium | T1b live answer transcript |
| Studio Audience | 3 | 3 | 4 | 3 | 13 | Low | Three real voices; no day-1 test on the MVP |
| Raid Torch | 4 | 2 | 3 | 3 | 12 | High | T3 second live channel and a real raid |

## Reasons
### Tap on the Shoulder
- Innovation (3): Well-known OBS plugins already cover the muted and silent mic (Muted Notification at 12.4k downloads, Remember to Talk). The tape’s second case — viewers reporting “far away,” a cross-check against OBS, an in-room face, then a delay-aware thumbs confirmation — is a combination that was not found intact, and that beat is visible.
- Impact (4): A dead mic on a live channel is documented (Snoop Dogg for over an hour; the OBS forum request about streamers forgetting they muted) and it applies to any broadcast with a mic. Weekly use is the soft spot: the card says real failures may be too rare to stay installed, and the DrDisrespect write-up shows viewers sometimes already get the warning through in chat.
- Tech (4): The 9-hour MVP leaves buffer, and the Codex artifact is concrete: the phone face plus a detector suite driven by the shared chat simulator. QR pairing, the headphone-only chime, and the delay window are real integration on top of the shared obs-websocket base.
- Design (4): The first twenty seconds states both cases in the camera shot: OBS catches a mute, then the face shows FAR AWAY when chat does. Three accounts cover the report, the mod phone cue, and two thumbs; the later “why it works” minute is explanation.
- Risk (Medium): T2 has to deliver a mute event and a usable silence threshold. A bad threshold makes the “chat + OBS” line false, while the far-away path can still be filmed from chat alone.
- Biggest weakness: The failure is vivid and uncommon, so the tool may sit idle, and the calm mode that would make it a daily face is stretch.

### Minefield
- Innovation (5): All three researchers, and a link-check re-search, found no loop where viewers secretly pick the word and the streamer’s unscripted speech sets it off. Existing speech triggers use words the streamer chose (Streamer.bot Voice Control, OK Gamers), and existing secret-word games resolve in typed chat; the planter’s named explosion is the missing loop, and it is the whole hook.
- Impact (3): No direct request for this game; the support is adjacent (manual swear jars, bingo, unverified posts about mic-word effects) on talk-heavy streams such as Just Chatting at 14.2%. A verified Dexerto piece shows viewers already baiting streamers into on-air words, so the desire is indirect and the social downside is part of the record.
- Tech (3): Hotwords, VAD, whole-word matching, and the accuracy harness are a concrete Codex artifact, and 9.5 hours still leaves the required buffer. T1’s bar — at least 80% hits, at most one false alarm per 10 minutes, under 3 seconds — is unmet until day 1, and a miss or a bogus boom is the product.
- Design (5): Lunch chat, a named boom, and the cut back to Bo’s bait question land in the first twenty seconds with a few accounts. The mishear-and-defuse gag and the end-of-stream dud flip give the tape two more visual beats.
- Risk (High): T1 can fail on casual speech, and there is no fallback spotter; faster-whisper hotword hallucinations are a verified failure mode even with VAD left on. T4’s sealed plant page is a second gate.
- Biggest weakness: The joke only exists if the spotter is right on ordinary talk, and that test has not been run.

### VAR
- Innovation (3): Chat-fired replay is already well known (tomaae at 12.6k downloads; Streamer.bot replay-buffer actions) and Twitch already ships polls; Glitch Studios already plays a branded half-speed replay. The joined ritual — two calls, slow motion, a 15-second jury, a stamp, a titled clip — was not found as one loop, and that ceremony is what the first twenty-five seconds show.
- Impact (3): Disputed moments sit in the largest part of viewing, competitive games, and a five-figure replay script shows people have wanted chat to trigger a second look. No request for a chat jury turned up, that script was last updated in 2019, and the replay request on file wants the streamer to pick the moment.
- Tech (4): At 8.5 hours this MVP has the most slack in the set, and the Codex artifact is the replay path itself plus a simulator test of call thresholds and vote timing. The review stays on the live output so the clip can hold it, with a nudge-back hotkey for the latency offset.
- Design (5): A paper ball, “IN!”, two `!var` calls, a siren, and a “NO BASKET” stamp explain the product in the first twenty seconds with three voters. The self-VAR circle drawing is a second round that still works on a desk.
- Risk (Medium): T2 has to put the replay on screen within 5 seconds and the offset has to land on the shot. A long review can still push the original moment out of the clip’s capture window.
- Biggest weakness: An automatic stoppage runs against the streamer who wanted control of when a replay plays, and both the replay and the vote already ship separately.

### Hint Jar
- Innovation (4): Private tiered hints, sealed on stream and opened one tier at a time by the streamer, were not found; the link check’s search for a Twitch tiered-hint tool came up empty. Queued backseats and the offline Universal Hint System are the neighboring parts, and the sealed answer staying sealed is the beat the video is built on.
- Impact (3): Backseating is a verified complaint (the Limbus Company Steam thread) and it clusters in blind puzzle, adventure, horror, and indie play, where those categories are growing and blind-run share is unknown. Most replies in that thread say rules, timeouts, and bans already handle it, and some viewers want no hints at all.
- Tech (3): The 8.5-hour build is a login page, a mod dock, a jar, a hotkey, and credits, which fits cleanly and is ordinary next to the speech and replay work. The Codex artifact is the demo puzzle plus the tool, the straightforward generation the budget already prices at about an hour and a half.
- Design (4): A shouted “LEFT DOOR,” a bot redirect, and one opened nudge with the answer envelope still sealed is clear in the first twenty seconds with three accounts. The mod re-tier and the credit are easy to follow and visually quiet.
- Risk (Low): T4 is a logged-in hint page on a public URL, and one working path is the pass. The loop has no speech or replay cliff once that page loads.
- Biggest weakness: The same thread that proves the annoyance also says ordinary moderation already fixes it, so the jar can fill and never be opened.

### Checkpoint
- Innovation (3): Featuring a queued question is a well-known loop: Meld’s AMA queue was the same core loop before the pivot, and StreamerQnA has 9.5k downloads. After the pivot, the visible difference is the spoken answer typing onto the card and a threaded reply quoting those words, which the single post-pivot check did not find elsewhere.
- Impact (4): Streamlabs already documents the manual version — scheduled chat breaks and a mod’s running question list — for heads-down art, making, coding, cooking, and focused play. That is a weekly habit where it fits, with thinner evidence that the viewer is still around when the receipt arrives.
- Tech (3): The voice-to-receipt pipeline is a concrete Codex artifact (segmenting, silence close, confidence gate, threaded reply, `drop_reason`) and the 9-hour MVP fits. T1b wants a readable quote within 2 seconds on 9 of 10 answers and is still untested; the pause-trigger fallback keeps a demo and drops the new half.
- Design (4): By 0:19 the tape has crystals, a first-time question, words typing while the pen keeps moving, a check, and a split screen of the threaded quote. Three accounts match the bit; the skip and the low-confidence plain receipt are clear and a little procedural.
- Risk (Medium): T1b can miss the speed or readability bar on this machine. The hold key and the plain receipt cover a pause or a mishear, and a failed test switches the demo to the pause-trigger fallback.
- Biggest weakness: The prize version puts the streamer’s words into a viewer’s thread, and that transcript test has not been run.

### Studio Audience
- Innovation (3): One mixed crowd whose loudness follows the count of distinct reactors, with a recurring voice on a named seat and a chant, was not found as a single system. Sound Alerts, per-viewer walk-ons, and Meld’s emote storm are well-known neighbors, and the “this laugh belongs to Ana” pitch overlaps walk-on sounds that already ship.
- Impact (3): Sound alerts and handmade emote-laugh boards are in current use, and a verified Dexerto piece shows how bleak a silent chat feels, on talk and variety streams (Just Chatting 14.2%). A verified request to block one viewer’s Sound Alerts, and the VoxBooster note that a laugh on every emote turns into repetitive noise, cut against wanting this every week.
- Tech (4): The Web Audio mixer is the Codex artifact and the product: distinct-viewer scaling, a voice derived from the user id, a chant rule, and a volume cap, tuned on simulator bursts, inside 9 hours. The MVP does not depend on Get Chatters or a second channel.
- Design (3): Three named seats bouncing on a missed shot, then a signature laugh, is understandable immediately, and a chant only needs two accounts. The premise — the room gets louder as more distinct people react — cannot be shown with three real voices, so the bigger crowd is a labeled simulation.
- Risk (Low): No day-1 test gates the MVP, and the card already tells the video to label simulator bursts. The recording described can be made with the three test accounts.
- Biggest weakness: Under the hackathon’s three-account rule, the scaling that separates this from a soundboard is the part the judges only see as a simulation.

### Raid Torch
- Innovation (4): Raid schedulers and hub wheels move the raid itself; none carries a visible object with per-chatter marks onto the next channel and lights those people when they speak. The fly-in and the torch-bearer glow are on screen, with two of the three hops labeled as rehearsal.
- Impact (2): Raid trains are a live 2026 practice (Raid Train Central’s page opened) among small and mid-size circles. All three researchers found no request for a carried torch or named arrivals, both channels have to adopt it, many raiders leave without chatting, and a verified PinkNews piece documents why small streamers are wary of raids.
- Tech (3): Cross-channel state, the deploy, and the journey page are a real Codex artifact, and the design correctly treats `channel.raid` as a count, lighting only marked people who then chat. The MVP sits at the 9.5-hour cap, and the demo adds a second live encode plus a real raid that the hour table does not include.
- Design (3): The torch flying in and a marked raider lighting up on their first line are readable images. A handoff between one person’s two channels, plus a map whose extra hops are labeled rehearsal, leaves the community relay thin for a three-minute tape.
- Risk (High): T3 requires a second live channel and a raid event within 5 seconds. Raids also have a 90-second countdown and can be cancelled, so the hook shot is the fragile one.
- Biggest weakness: The object is new, and the multi-channel relay that would give it meaning cannot be shown with this entrant and was not asked for.

## Ranking
1. Minefield: The planter-versus-speech loop is the one the search actually missed, and the boom is still a complete three-minute show with three accounts if the spotter holds.
2. Tap on the Shoulder: Tied on points with VAR, and the one I would place next because the pain is documented and the phone-face demo works with a mic, a spare phone, and three accounts.
3. VAR: The most broadcast-like tape in the set, a full ritual in one paper-ball shot, with thinner evidence anyone wants a jury and a replay that has to land on the right frames.
4. Checkpoint: The weekly heads-down habit is already written down by Streamlabs, and the quote landing in the viewer’s thread is a sharp payoff, held to this slot by an untested transcript.
5. Hint Jar: A clear sealed-hint show with a loop Twitch tools did not already have, for a narrower crowd whose own thread mostly trusts bans and timeouts.
6. Studio Audience: The surest build of the seven, and the three-account rule strips out the crowd scaling the project is about.
7. Raid Torch: A new object whose community relay cannot appear in this demo, with a live second channel and two-sided adoption in the way.