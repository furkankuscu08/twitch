# Wave 2 / L3: Capability and transfer

Lens: start from underused Twitch surfaces and from mechanisms proven elsewhere but missing on Twitch for free; combine them. Researched 2026-10-25. Labels: **[V]** verified on a primary page I read, **[S]** secondary or snippet, **[I]** inference, **[U]** unknown.

## API facts checked for this lens

- **Pinned Chat API** (GA 2026-05-29) [V, Helix reference + change-log]:
  - `PUT /helix/chat/pins` pins **any message by `message_id`**, including a viewer's own message. The pinner must be the broadcaster or a mod (`moderator:manage:chat_messages`).
  - Duration is 30–1800 s, or until the stream ends if omitted. One mod pin at a time, and a new pin replaces the old one. `PATCH` changes only the duration.
  - Send Chat Message with `pin: true` sends and pins in one call (always 20 min).
  - No Affiliate gate is mentioned [V, absence]. Not yet tested on a new channel [U]. The pin rate limit is unpublished [U].
- **Custom Power-Ups:** each has a `bits` price, so viewers pay money [V]. Parked.
- **Stream markers:** need `channel:manage:broadcast`, fail if VODs are off [V]. **Modify Channel Information** can change the title on any channel; only `delay` is Partner-only [V]. The title-change rate limit is unknown [U].
- **Shared Chat:** `channel.chat.message` carries `source_broadcaster_*` fields [V]. Who can start a Shared Chat session is [U].
- **Watch Streaks:** delivered in `channel.chat.notification` since 2026-04-02 [V]. This is Twitch's only free, native "earned attendance" signal.
- **Prior art** [S, search]:
  - Q&A queue widgets exist (StreamerQnA, Meld AMA Queue, a Patreon Streamer.bot widget). None uses the native pin.
  - Raid tools are alerts and clip shoutouts. I found no "handoff" tool.
  - Loyalty points and watch-time leaderboards exist (StreamElements, Streamlabs). I found no level shown on every message that decays.

## A. Crowd map

1. AI co-host or chatbot that answers chat and remembers viewers
2. "Twitch Plays" (chat controls a game)
3. Live poll or prediction overlay, often with LLM-generated questions
4. Chat trivia or quiz with a leaderboard
5. Chat bingo or stream-event bingo
6. Tabletop dice roller or TTRPG initiative overlay
7. "Streamer distractions": viewers trigger effects or challenges (Crowd Control lite)
8. Chat-fed pet or avatar in the overlay
9. AI clip generator, or a "what did I miss" chat summarizer
10. Live sports or game-stats overlay
11. Collab helper: co-stream scheduler or shared overlay

## B. Wide list

1. **Floor (Pinned Q&A):** `!ask` queues a question. The streamer taps once, and the viewer's own message is natively pinned and indexed with a marker. `YouTube Q&A`, `Pinned Chat`, `need #1`, `need #6`
2. **Story So Far:** a living pinned "you are here" header, kept in sync with markers, the stream title and the last clip. `Pinned Chat`, `markers`, `need #3`, `raid`
3. **Chat Footnotes:** a mod-written lore dictionary. When a lore term is used in chat, an overlay footnote explains the inside joke. `need #3`, `need #4`
4. **Lit Medals:** a free per-channel level beside names in an overlay chat. It goes "unlit" after missed streams. `Bilibili fan medal`, `Kick Level Up`
5. **Raid Torch:** a cross-channel object that moves only by raids and gathers marks from each chat. `raid as handoff`
6. **Raid Doorway:** an incoming raid gets a pinned "here is where we are" message plus the raider's latest clip on the overlay. `raid`, `clips`
7. **Mod Cockpit:** a private mod web panel for pins, markers and overlay cards, replacing public `!commands`. `need #4`
8. **Consensus Clip:** when 2 of 3 chatters spam the same emote, a clip is created. The 85 s look-back absorbs latency. `clips`, Twitch 2026 priority
9. **Sealed Envelope:** `!seal <guess>` is deleted at once by the bot. The overlay shows named sealed envelopes that open together. `locked-in predictions`
10. **Shared Chat Bridge:** collab overlay that color-codes messages by source channel and pairs "pen pals" across the two communities. `Shared Chat`
11. **Chapter Title Sync:** the directory title follows the current chapter. `Modify Channel Info`, discoverability
12. **Watch Streak Constellation:** each streak share adds a star to a monthly shared sky. `Watch Streaks`
13. **Emote-Only Rush:** chat settings as game state. Boss fight means emote-only chat, and emotes become ammo. `chat settings`
14. **Lurker Lanterns:** an anonymous count of silent viewers drawn as dim lanterns that brighten when someone types. `need #2, lurker-safe`
15. **Shoutout Ring:** an opt-in ring of small streamers. At stream end, the bot suggests a live member to raid and pre-fills a shoutout. `raid`, `shoutouts`
16. **Daily Stamp:** one hour of presence unlocks a collectible stamp reveal. `Kick Daily Rewards`
17. **Marker Notebook:** mods privately drop annotated markers, which become a post-stream to-do and clip list. `markers`, `need #4`, `need #8`
18. **GIF Jukebox:** chat GIFs (new `gif` fragment) queue into a small overlay frame, with a mod veto. `GIFs in chat`
19. **Guest Star Green Room:** viewers queue to join as callers. `Guest Star (beta)`
20. **Raid Last Call:** chat votes on a one-line "what you're walking into" message, which is pinned before an outgoing raid. `raid`, `Pinned Chat`

## C. Five full cards

### Story So Far
- **One-liner:** A living, natively pinned "you are here" header in Twitch chat, synced with stream markers, the stream title and a "missed it?" clip. A late viewer or a raider knows what is happening at a glance.
- **Who installs it / who gets the value:**
  - **Streamer:** installs it (OAuth, a browser source, a hotkey). They get VOD chapters and a current directory title without typing.
  - **Viewers:** newcomers and raiders get context without asking. Regulars get a clip of what they missed.
  - **Mods:** set chapters from a private panel.
- **Streamer category fit:** Any stream with phases: story games, challenge runs, IRL and travel, art and making, science and coding. Weak for short-round competitive games.
- **Core loop:**
  1. The streamer or a mod hits "New chapter" and types a short title.
  2. The bot sends `📍 Ch. 4 · The Bridge · missed Ch. 3? <clip>` with `pin: true`, replacing the old pin.
  3. At the same moment: a marker is created, the title can update to `[Ch. 4] The Bridge | …`, and a clip of the last 90 s is saved as Ch. 3's last moment.
  4. The overlay plays a small TV-style chapter card.
  5. On `channel.raid`, the pin is re-sent as "👋 Raiders from X: we're in Ch. 4."
- **First 10 seconds of the demo:** One keypress. The overlay chapter card slides in, the pinned bar at the top of the real Twitch chat flips, and the directory shows the new title. A test account "arrives late" and its first message is about the bridge, not "what's going on?".
- **Twitch surfaces used:** Send Chat Message (`pin`) or Pin Chat Message; Create Stream Marker; Create Clip; Modify Channel Information; EventSub `channel.raid`, `stream.online`/`offline`, `channel.chat.message`; overlay.
- **Works with 1 streamer + 3 test accounts? How?** Yes. One late arriver is the whole use case. Account 1 is a mod who sets chapters; account 2 arrives late. The raid variant needs a second live channel owned by the builder [V: raids need a live target]. That part is optional.
- **Closest existing thing and the meaningful difference:**
  - Streamers pin a static "today's plan" by hand, and Twitch makes VOD chapters on category change [I]. Marker commands exist [I].
  - I found no tool that treats the native pin as an **auto-updating status line** tied to markers, title and clips [S].
  - It lives inside native chat, where newcomers actually look, and persists on the VOD and in the directory.
- **Why wouldn't 30 other teams build this?** The Pinned Chat API is five months old [V], and most teams start from games or AI co-hosts. It is a quiet utility whose spectacle is in polish [I].
- **Evidence it links to:** Need #3, new viewers excluded [V]. Raids as social handoff [V]. Need #9, production quality [V]. Twitch 2026 discoverability priority [V]. Unvalidated: that late arrivers read pins. Validate by asking 5 small streamers how often "what did I miss?" comes up.
- **MVP scope / out of scope:**
  - **In:** chapter button (dock + hotkey), pin, marker, optional title sync, raid welcome, chapter card, end-of-stream chapter list.
  - **Out:** auto-detected chapters, LLM summaries, multi-platform, anything kept beyond 24 h.
- **Riskiest assumption:** Pinning works on a new non-Affiliate channel and tolerates a pin every few minutes. Test on day 1. The fallback (overlay header plus plain bot message) loses the point.

### Floor (Pinned Q&A)
- **One-liner:** YouTube-style Q&A for Twitch. The streamer taps a queued `!ask` question, and the viewer's **own message** is pinned natively with their name, shown on the overlay, and indexed with a marker.
- **Who installs it / who gets the value:**
  - **Streamer:** gets a ranked question list readable while busy (need #1) and a VOD index.
  - **Viewers:** the asker gets a public status moment. Lurkers can `+1` without writing.
  - **Mods:** approve or pick from a private panel.
- **Streamer category fit:** Just Chatting, education, coding and science, art, AMAs, between-round gaming.
- **Core loop:**
  1. A viewer types `!ask how do you shade metal?`, and others type `+1 3`.
  2. The streamer taps a question on a dock or phone.
  3. The original message is pinned for the answer, an overlay card shows "@name asks…", and a marker is set.
  4. At stream end, the bot posts the answered list with timestamps.
- **First 10 seconds of the demo:** A test account asks. The streamer taps a phone button. The question jumps to the top of real Twitch chat with the viewer's name, the overlay card lights up, and the viewer reacts "my question got pinned!".
- **Twitch surfaces used:** `channel.chat.message`, Pin/Unpin Chat Message, Create Stream Marker, Send Chat Message, overlay.
- **Works with 1 streamer + 3 test accounts? How?** Yes. Three askers, a few `+1`s and two answers make a full demo. In small channels the promise is "your question will be seen".
- **Closest existing thing and the meaningful difference:** Overlay queue widgets (StreamerQnA, Meld) [S], and YouTube's native Q&A [V]. The difference is the native pin of the viewer's own message [S: not found in existing tools], plus voting and marker indexing.
- **Why wouldn't 30 other teams build this?** Q&A sounds plain, and the pin trick needs knowledge of a May 2026 API. Risk: judges file it next to polls.
- **Evidence it links to:** Q&A exists on YouTube, not Twitch [V]. Need #1 [V]. Need #6 [V]. Lurker-respecting via `+1` [I].
- **MVP scope / out of scope:**
  - **In:** `!ask`, `+1`, tap-to-pin dock, overlay card, markers, end list.
  - **Out:** duplicate merging, LLM question detection, Discord intake.
- **Riskiest assumption:** That it reads as new rather than "another queue widget". The video must center the pin moment. Pin permission on a new channel is also [U].

### Raid Torch
- **One-liner:** A digital torch that moves between channels **only through raids**. Each chat that holds it adds a mark (an emote ring), and it arrives on the next channel's overlay carrying its whole journey.
- **Who installs it / who gets the value:**
  - **Streamers:** every streamer in a raid circle or team installs it. Their raids become a shared story instead of a 10-second alert.
  - **Viewers:** get a reason to ride the raid and see their mark on another channel's screen.
- **Streamer category fit:** Small-streamer circles, raid trains, Twitch teams, VTuber groups. Category-agnostic.
- **Core loop:**
  1. While a channel holds the torch, chatters type `!mark <emote>` (one each). Each becomes a ring on the torch.
  2. The streamer raids, and `channel.raid` hands off the torch.
  3. The receiving overlay shows the torch flying in ("4 channels, 23 marks"), and the bot pins "🔥 The torch arrived from X".
- **First 10 seconds of the demo:** Channel A's torch glows with emote rings. Raid. Cut to channel B: the torch flies in with its rings and a journey map, and the raiders type "we brought that!".
- **Twitch surfaces used:** EventSub `channel.raid` (no auth needed [V]), optional Start Raid, Pin Chat Message, `channel.chat.message`, Get Users (avatars), overlay, and a shared backend.
- **Works with 1 streamer + 3 test accounts? How?** Partly. It needs two live channels (the builder plus a test account streaming from a phone), since raids need a live target [V]. This is the most setup-heavy of the five.
- **Closest existing thing and the meaningful difference:** Raid trains (R3dLabs Toolbox [S]) and raid alerts. Neither carries **state** across channels. The torch turns the raid's social handoff into a visible object.
- **Why wouldn't 30 other teams build this?** It needs two channels to demo and a network to matter [I].
- **Evidence it links to:** Raids are valued as social discovery and handoff [V, E2]. Unvalidated: whether raid circles would adopt it. Ask 2–3 raid-train Discords.
- **MVP scope / out of scope:**
  - **In:** one torch per circle code, marks, raid handoff, journey view, pinned arrival.
  - **Out:** multiple torches, leaderboards.
  - Store IDs only, with a 24 h expiry. A multi-day journey conflicts with the 24 h rule [U].
- **Riskiest assumption:** A cross-channel artifact feels meaningful with only two channels on video.

### Lit Medals
- **One-liner:** A free, Bilibili-style per-channel fan medal beside each name in a styled overlay chat. It rises with attendance, Watch Streaks and chat, and goes grey ("unlit", level kept) after three missed streams.
- **Who installs it / who gets the value:**
  - **Streamer:** recognizes regulars without a paid tier.
  - **Viewers:** visible, free status (Kick Level Up envy [V]). Lurkers earn by attending.
  - **Mods:** grant a "medal of the day".
- **Streamer category fit:** Any channel with regulars. Small and mid communities.
- **Core loop:**
  1. A viewer chats, and the overlay line shows `[🏅7] name: …`.
  2. The first message of a stream relights a grey medal with a flare.
  3. A Watch Streak share gives a bonus.
  4. Level-ups get a tiny ceremony.
- **First 10 seconds of the demo:** Three medalled names, one grey. That viewer types "back!", and the medal relights and ticks up to 8.
- **Twitch surfaces used:** `channel.chat.message`, `channel.chat.notification` (Watch Streaks), `stream.online`/`offline`, Get Chatters, overlay chat.
- **Works with 1 streamer + 3 test accounts? How?** Yes, with seeded levels and a dev clock to simulate missed streams (must be labeled as simulated).
- **Closest existing thing and the meaningful difference:** StreamElements and Streamlabs loyalty points and `!top` [S] are hidden balances you query. The medal is **shown on every message** and has a **lit/unlit recency rule**. Twitch sub badges are paid [V].
- **Why wouldn't 30 other teams build this?** It looks like a loyalty bot, and few teams know Bilibili or Kick [I].
- **Evidence it links to:** Per-channel earned status is the most repeated cross-platform pattern [V]. Kick envy [V]. Counter-evidence: thin love for free versions, and farming scripts [V].
- **MVP scope / out of scope:**
  - **In:** level formula, overlay chat with medals, relight and level-up animations, streak bonus.
  - **Out:** native chat badges (not possible [I]), cross-channel levels.
- **Riskiest assumption:**
  - **Data retention:** persistent per-user counters beyond 24 h may count as Twitch content [U]. This must be resolved first, or the idea is parked.
  - **Overlay only:** medals are visible only in the overlay chat.

### Chat Footnotes
- **One-liner:** Inside jokes get footnotes. Mods keep a channel lore dictionary. When a lore word or emote appears in chat, a tiny numbered footnote card slides into the overlay corner ("³ 'the bucket': the mug that fell in 2025, don't ask").
- **Who installs it / who gets the value:**
  - **Streamer:** installs it.
  - **Mods:** get a private creative job curating lore (need #4).
  - **Newcomers:** get included (need #3).
  - **Regulars:** enjoy seeing their lore canonized (need #10).
- **Streamer category fit:** Any channel with running jokes. VTubers and variety streamers above all.
- **Core loop:**
  1. A regular types "bucket moment again".
  2. A footnote card shows for 8 s, rate-limited per term.
  3. `!lore bucket` gives the full entry.
  4. A start-of-stream pin reads "New here? Lore: bucket³, the wall⁷".
- **First 10 seconds of the demo:** Chat spams "BUCKET 🪣🪣". A handwritten-style footnote pops up. The "new viewer" account types "ohhh lol".
- **Twitch surfaces used:** `channel.chat.message` (text and emote fragments), Pin Chat Message, overlay, a mod web panel.
- **Works with 1 streamer + 3 test accounts? How?** Yes. Two regulars use the joke and one newcomer gets it. This is an ideal small-channel story.
- **Closest existing thing and the meaningful difference:** Static `!lore` commands and About-panel text [I]. Footnotes are **triggered by the conversation** at the moment the joke is used.
- **Why wouldn't 30 other teams build this?** It is a culture idea, not a tech idea, and not near any organizer example [I].
- **Evidence it links to:** Need #3 (169-point Reddit thread on clique chats) [V]. Needs #4 and #10 [V].
- **MVP scope / out of scope:**
  - **In:** lore panel, matcher, footnote overlay, `!lore`, start pin.
  - **Out:** auto-suggested lore (an LLM is tempting; skip it).
  - Lore is written by mods, not stored chat, so the 24 h rule is likely fine [I].
- **Riskiest assumption:** That footnotes feel charming, not like "explaining the joke kills it". The styling carries it.

## D. Parked

- **Custom Power-Up quests:** Power-ups are Bits-priced [V], and Get Custom Power-up is listed as Affiliate/Partner [V, wave 1 A]. Would need Bits usable on a new channel and on test accounts.
- **Shared Chat Bridge:** Shared Chat eligibility is [U], and it needs two live channels. Would need a day-1 test between two non-Affiliate channels.
- **Sealed Envelope on native Predictions:** whether Predictions work without Affiliate is [U/S]. Would need Create Prediction to pass on day 1. The `!seal` version stays in the wide list.
- **Lit Medals with long memory:** may break the 24 h storage rule [U]. Would need derived per-user counters to be allowed, or viewer opt-in.
- **Guest Star Green Room:** beta with eligibility [U]. Would also need real callers.
- **Whisper ballots:** whisper senders need a verified phone, and the bot can whisper at most 40 recipients a day [V]. Would need inbound viewer whispers to work without that friction [U].

## E. Your pick

**Story So Far.** It is the purest example of this lens. It puts a brand-new API most teams will not notice (Pinned Chat, GA May 2026) at the visible center. It fuses that API with markers, the title and clips in a way I found no tool doing. It also serves the best-supported small-channel evidence: new or raided viewers lacking context (need #3) and raids as social handoff. One late arrival is the whole story, so it fits a 1-streamer demo. It respects lurkers, needs no AI, and its moment (one keypress changes the overlay, the native pinned bar and the directory title) reads in one shot. The day-1 risk is pinning on a new channel. If pins work, **Floor** is the runner-up on the same plumbing. If pins fail, both lose their core, and I would switch to **Chat Footnotes**, which needs only chat plus overlay.
