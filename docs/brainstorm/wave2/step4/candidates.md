# Quality gate: candidates

37 candidates, in random order. Each has the same fields. "Notes" are feasibility notes; they are tracked separately and are not grounds for FATAL.

## C01: Lurker presence made visible

- **What it is:** Silent viewers appear as dim lanterns or stars on a small skyline overlay, built from the chatter list, with no names and no prompt to speak. A viewer's first message makes their light flare. `!lurk` lets someone say "I'm here, don't wait for me".
- **First 10 seconds of the demo:** Five dim lights on a skyline; one viewer types; a light flares.
- **Closest existing things:** Lurk commands, viewer counters.
- **Notes:** none

## C02: Guest Star green room

- **What it is:** Viewers queue to join the stream as on-air callers through Twitch's Guest Star feature; a green-room overlay shows who is waiting and the streamer picks one.
- **First 10 seconds of the demo:** A green-room card lists two waiting viewers; the streamer picks one and their camera joins the stream.
- **Closest existing things:** Guest Star itself, call-ins over Discord.
- **Notes:** Guest Star is in beta with unknown eligibility.

## C03: One line over the game

- **What it is:** For streamers with a single monitor: a small click-through, always-on-top window over the fullscreen game shows exactly one line, the latest first-time message or question. Everything else is dropped. The streamer glances, answers aloud, and presses a key to dismiss; the next qualifying line takes the slot.
- **First 10 seconds of the demo:** Fullscreen gameplay; a viewer's question appears as one line in the corner; another viewer's "lol" produces nothing; a first-time "hi" replaces it.
- **Closest existing things:** Full chat overlays; products sold specifically as chat for streamers without a second monitor.
- **Notes:** Window behavior over fullscreen games is untested; the video needs a license-safe (e.g. open-source) game.

## C04: Raid ring for small streamers

- **What it is:** Small streamers opt into a ring. At the end of a stream, the tool suggests a ring member who is live right now and pre-fills the raid and a shoutout.
- **First 10 seconds of the demo:** The streamer wraps up; a card shows two live ring members; one click raids.
- **Closest existing things:** Raid trains, Twitch's own raid suggestions, Discord raid communities.
- **Notes:** The demo needs 2–3 live channels.

## C05: Raid lands at a bad moment

- **What it is:** If a raid lands while the streamer is on a BRB or starting-soon screen, the raider's name stays on screen and the streamer gets a reminder until they tap "thanks", which also sends the official shoutout. Variant: the scene switches automatically to a live welcome.
- **First 10 seconds of the demo:** BRB screen; a raid arrives; a persistent "Raid from X: thank them!" card; the streamer returns, taps, and the shoutout fires.
- **Closest existing things:** Raid alerts, auto-shoutout bots.
- **Notes:** A real raid needs a second live channel.

## C06: Chat-consensus clipping

- **What it is:** When two or more chatters react the same way within seconds (or explicitly agree), the tool creates a clip of the last ~85 s, absorbing stream latency, optionally rendering a vertical crop for short-form platforms.
- **First 10 seconds of the demo:** A funny moment; two viewers spam the same emote; a "clipped!" toast appears and the clip link lands in chat.
- **Closest existing things:** Chat-spike auto-clippers, AI highlight tools, Twitch's own clip button.
- **Notes:** none

## C07: Chat-called replay review

- **What it is:** When viewers dispute a moment, two of them type `!var`. A "VAR CHECK" stinger plays, the last ~20 s replay from the local replay buffer with the final seconds in slow motion, chat votes yes/no for 20 s with names on a jury bench, a verdict stamp lands, and a titled clip is created.
- **First 10 seconds of the demo:** The streamer throws a paper ball: "IN!"; two viewers call VAR; slow motion shows it bouncing off the rim; the jury votes; "NO BASKET".
- **Closest existing things:** An OBS instant-replay script triggered by chat, native polls.
- **Notes:** none

## C08: Chat reactions amplified

- **What it is:** Chat emotes and keywords become a live theater-crowd soundscape (laughs, gasps, boos, applause). Intensity scales with the number of distinct viewers reacting, so three viewers sound like a full house. Each viewer has a recognizable signature laugh and a bouncing seat silhouette with their name. A headphone-only mode lets the streamer hear chat without reading it.
- **First 10 seconds of the demo:** The streamer misses a paper-ball shot; one viewer types "L", two type "LUL"; a packed theater boos, then laughs, and three named silhouettes bounce.
- **Closest existing things:** Sound Alerts (paid soundboard), per-user entrance sounds, visual emote walls.
- **Notes:** none

## C09: Viewer plants it, the streamer sets it off

- **What it is:** Viewers secretly plant word mines (`!mine pineapple`; the bot deletes the message at once). The overlay shows the mines with owners' names, never the words. Viewers steer the conversation toward their word. When the streamer says it, local speech-to-text catches it: explosion, the planter's name, and an auto-titled clip. Variants: viewers attach sound effects to the streamer's catchphrases; webcam smile detection in a "try not to laugh" round.
- **First 10 seconds of the demo:** Three mines live; the streamer says "honestly, pineapple on pizza is—" BOOM; a banner names the planter; cut to that viewer's bait question from minutes earlier.
- **Closest existing things:** Speech-recognition swear jars, the party game Taboo.
- **Notes:** Depends on speech-to-text accuracy on casual speech.

## C10: Bookmark a moment for later

- **What it is:** A viewer bookmarks something to revisit: "show that brush again", `!rewind` on a funny moment, or a promise the streamer made ("I'll show you later"). The streamer gets a short list at a break or at the end and picks one for a deliberate encore or replay, crediting the viewer.
- **First 10 seconds of the demo:** During a drawing a viewer types `!encore brush`; at the end the streamer opens the encore list and redoes the stroke slowly while the viewer's name shows.
- **Closest existing things:** Stream markers, clip requests in chat, mod notes.
- **Notes:** none

## C11: Local live captions for viewers

- **What it is:** Local speech-to-text turns the streamer's speech into a small caption row on stream, optionally translated. Audio never leaves the machine.
- **First 10 seconds of the demo:** The streamer speaks; a one-line caption appears under the facecam.
- **Closest existing things:** OBS caption plugins, Twitch's own caption support.
- **Notes:** Needs caption-grade speech-to-text accuracy.

## C12: Glanceable chat state in the room

- **What it is:** A spare phone propped on the desk shows a cartoon face that represents chat: it waves and shows a new chatter's name in huge letters, raises a hand with a counter when a question is waiting, changes expression with emote mood, and dozes when chat is quiet. One tap shows the waiting question. It sits in the camera shot, so viewers see their message move an object in the room. Variants: a smart bulb that takes the chatter's color; distinct headphone sounds per message type.
- **First 10 seconds of the demo:** The streamer is drawing; a test account types "hi, first time here"; the phone waves and shows the name; the streamer greets them without putting the pen down.
- **Closest existing things:** On-screen chat pets (Elgato Mochi), Elgato Prompter chat mode, Lumia Stream light effects, reading chat on a propped phone.
- **Notes:** none

## C13: Lore footnotes

- **What it is:** Moderators keep a small glossary of the channel's inside jokes in a web panel. When a term appears in chat, a small numbered footnote card slides into a corner of the stream explaining it, credited to the lore author, with a cooldown per term. Variant: footnotes appear only on request (`!why <term>`) without showing who asked.
- **First 10 seconds of the demo:** A regular types "bean moment again"; a footnote pops up ("1 the bean: ate a raw coffee bean on stream and cried"); the newcomer account types "ohhh lol".
- **Closest existing things:** Bot custom commands (`!bean`) that answer only people who already know to ask; channel About panels.
- **Notes:** none

## C14: Missed hellos from another platform

- **What it is:** For streamers simulcasting to Twitch and YouTube: greetings from YouTube live chat that the streamer would otherwise miss collect in a small tray on the streamer's Twitch dock.
- **First 10 seconds of the demo:** A YouTube viewer says hi; the tray lights up; the Twitch streamer greets them by name.
- **Closest existing things:** Multi-platform chat aggregators (e.g. Restream chat).
- **Notes:** Needs a live-enabled YouTube channel and the YouTube API.

## C15: Shared Chat collab bridge

- **What it is:** During a Twitch Shared Chat collab between two channels, an overlay color-codes each message by its home channel and pairs "pen pals" across the two communities.
- **First 10 seconds of the demo:** Messages from two communities appear in two colors; a pairing card introduces two viewers from opposite channels.
- **Closest existing things:** Twitch Shared Chat itself, collab overlays.
- **Notes:** Shared Chat eligibility for new channels is unknown; needs two live channels.

## C16: Viewers write the brief, the streamer performs it

- **What it is:** The streamer opens a short scene ("a tiny detective enters a storm"). Three viewers each claim a role (weather, footsteps, surprise) and pick a cue; the score fills in on screen; the streamer then performs the sounds live with desk objects (paper, cup, spoon) as the overlay advances. Variants: viewers assign fictional identities to three real props for an improvised scene; viewers propose tiny experiments the streamer predicts and then performs.
- **First 10 seconds of the demo:** The brief and three viewer cues appear; the streamer crinkles paper for rain and produces an absurd thunderclap with a cup.
- **Closest existing things:** Viewer-triggered sound effects (playback, not performance), improv games.
- **Notes:** none

## C17: Focus capture, surfaced at a break

- **What it is:** Before a busy stretch (a hard level, a tricky drawing section) the streamer hits a hotkey. Every normal chat message is held (commands and bot lines filtered out) and shown as a growing pile of colored "save crystals" in a corner. At the next break the streamer hits "checkpoint" and pages through the held messages as on-stream call-in cards, answering each aloud; first-time chatters come first. Variant: a moderator collects one question, one contribution and one announcement for the streamer's return.
- **First 10 seconds of the demo:** Crystals stack up while the streamer is busy; "CHECKPOINT" flashes and the first viewer's message appears as a TV-style call-in card.
- **Closest existing things:** Q&A queues, chat highlight tools, AI "what did I miss" summaries. Claimed difference: no command needed, no summary, every message keeps its author.
- **Notes:** none

## C18: Sealed predictions

- **What it is:** Before an outcome, viewers type `!seal <guess>`; the bot deletes the message at once so no one can copy it; the overlay shows named sealed envelopes; at the reveal they all open together.
- **First 10 seconds of the demo:** Three named envelopes on screen; the outcome happens; they flip open showing who called it.
- **Closest existing things:** Twitch Predictions (channel points), chat guessing games.
- **Notes:** none

## C19: Viewers drive the camera setup

- **What it is:** One viewer at a time becomes "director" and issues discrete commands that change the stream's camera crop or filter ("zoom on hands", "noir"), credited on screen. Variant: viewers plant positional creaks into a horror game's audio.
- **First 10 seconds of the demo:** A viewer types `!cut hands`; the camera crops to the streamer's hands with "Directed by Ana".
- **Closest existing things:** Twitch Plays-style controls, viewer-triggered effects (Crowd Control).
- **Notes:** Directors see results 2–30 s late, so only discrete commands work.

## C20: Something travels with the raid

- **What it is:** When a channel raids another, something travels with the raid and appears on the target stream: a one-line note from the outgoing streamer or co-written by chat ("we just finished a pie"), or a digital torch that collects an emote mark from every chat that held it and arrives showing its journey. Both channels run the tool.
- **First 10 seconds of the demo:** Channel A's torch glows with emote rings; raid; on channel B the torch flies in with its rings and raiders type "we brought that!".
- **Closest existing things:** Raid alerts, raid trains (no state carried between channels).
- **Notes:** Needs a second live channel; only same-day journeys are allowed under the 24 h data rule.

## C21: GIF jukebox

- **What it is:** GIFs that viewers post in chat (a new Twitch chat feature) queue into a small picture frame on stream, one at a time, with a mod veto.
- **First 10 seconds of the demo:** A viewer posts a GIF; it plays inside a picture frame on stream.
- **Closest existing things:** Media-share overlays (StreamElements).
- **Notes:** GIF availability on new channels is unknown; third-party GIFs may carry rights issues in a video.

## C22: Timed chat-settings mode

- **What it is:** One key turns chat to emote-only for a set time ("don't tell me the code"), shows a countdown badge, and automatically restores whatever chat settings were on before. Variant: a game where boss fights switch chat to emote-only and emotes become ammo.
- **First 10 seconds of the demo:** A viewer's spoiler is rejected, an emote goes through, the timer ends and words work again.
- **Closest existing things:** Twitch's own emote-only toggle in the dashboard, mod commands.
- **Notes:** none

## C23: Spoiler-hold filter

- **What it is:** While a story section is on, chat lines that look like spoilers or directions are held out of the streamer's view (or out of public chat) in a drawer that the streamer opens after the section.
- **First 10 seconds of the demo:** A viewer types "the key is behind the painting"; it slides into a "held" drawer; after the chapter the streamer opens it.
- **Closest existing things:** AutoMod and blocked terms, no-spoiler rules.
- **Notes:** none

## C24: Production problems reach the streamer

- **What it is:** When the stream has a problem the streamer can't notice (mic muted, game too loud, hand covering the camera), viewer reports and moderator cues reach the streamer through a private channel that works over a fullscreen game: a desk lamp turns red, a headphone-only chime plays, the dock shows the issue in big text. Trigger: two or more viewers mention "mic/audio" within 60 s, or a mod taps a preset. The helper gets an on-stream thank-you. Variant: a repair-and-confirm loop where the streamer says "Test B" after a fix and viewers reply `!heard B good` or `!heard B quiet`.
- **First 10 seconds of the demo:** Close-up of a muted mic; chat fills with "MIC??"; a lamp behind the streamer turns red; the streamer winces, unmutes, and a thank-you credit pops.
- **Closest existing things:** Smart lights on Twitch events (WooferBot, Streamer.bot), OBS mute indicators, a friend relaying chat.
- **Notes:** Lamp is optional (a phone-flash fallback exists).

## C25: Viewer voicemail call-in

- **What it is:** Viewers leave 15-second voice messages on a web page; a mod approves them; the streamer airs them during a break with a retro phone overlay and answers.
- **First 10 seconds of the demo:** A ringing-phone overlay; a viewer's recorded voice plays; the streamer answers live.
- **Closest existing things:** Paid text-to-speech messages, call-in segments over Discord.
- **Notes:** Needs recording consent and mod approval before airing.

## C26: "You are here" context for late arrivals and raiders

- **What it is:** During the stream the streamer or mods drop short beats or chapter titles ("beat the frog king on try 9"). When a raid arrives, or on request, the stream shows a 10-second TV-style "Previously on…" card with the last three beats. Variant: each new chapter is pinned at the top of native Twitch chat, creates a stream marker, updates the stream title, and saves a clip of the last 90 s.
- **First 10 seconds of the demo:** A raid lands; the screen dims and a "PREVIOUSLY ON" card sweeps in with three beats; a raider types "ahh ok, frog king".
- **Closest existing things:** Raid alerts and auto-shoutouts (they welcome the raider, they don't brief the raiders), a hand-pinned "today's plan" message.
- **Notes:** A real raid needs a second live channel; the pin variant depends on an API untested on a new channel.

## C27: Newcomer welcome and orientation

- **What it is:** When someone chats for the first time this stream, the channel orients them without a public spotlight: a regular on "welcome duty" is pinged to say hi, or a small menu card appears on stream only then, or regulars' self-written one-line bios appear the first time they talk so newcomers know who's who. Variant: a thermal printer prints each first-time chatter's name and the streamer pins it on a real wall.
- **First 10 seconds of the demo:** A new account says hi; a small card introduces the regular who answers ("@kay: mod, makes the bad puns"); the newcomer replies.
- **Closest existing things:** First-chatter alerts in Streamlabs and Streamer.bot, Twitch's own first-time-chatter highlight.
- **Notes:** none

## C28: Tiered hints

- **What it is:** On blind playthroughs or puzzles, viewers who know the answer submit hints at a strength (nudge / method / answer) instead of backseating. Hints are sealed: deleted from public chat by the bot, or sent to a private mod-approved queue. An overlay jar fills with envelopes. When stuck, the streamer opens only the level they want, and the helper gets credit.
- **First 10 seconds of the demo:** The streamer is stuck on a puzzle; envelopes drop into a jar; the streamer sighs, hits a key, and a nudge appears while the answer stays sealed.
- **Closest existing things:** No-backseating rules, backseat queues (LeagueBackseat).
- **Notes:** The demo would use our own puzzle, not a commercial game.

## C29: Chat translation for the streamer

- **What it is:** Messages in a language the streamer doesn't speak are translated in the streamer's private dock, and the streamer's typed reply can be translated back.
- **First 10 seconds of the demo:** A viewer writes in Turkish; the dock shows the translation; the streamer answers in English and the reply goes out in Turkish.
- **Closest existing things:** Translation bots and browser extensions.
- **Notes:** A cloud translator sends chat text to a third party; a local model avoids that.

## C30: Per-viewer souvenir moment

- **What it is:** A viewer types `!snap <caption>`. The streamer hears a cue and poses, the overlay counts down, a flash fires, and a Polaroid of the moment develops on screen with the viewer's name and caption; the viewer gets a link to save it (expires in 24 h). At stream end all snaps form a "who was here today" collage. Variants: a numbered ticket stub per attendee; an end-of-stream "museum" crediting viewer contributions.
- **First 10 seconds of the demo:** A viewer types `!snap first win`; the streamer holds up a mug; a flash; a Polaroid develops in the corner.
- **Closest existing things:** Generic chat-to-overlay commands, physical subscriber-slip printers.
- **Notes:** Image links need public hosting.

## C31: Question queue

- **What it is:** Viewers ask with `!ask` or any line ending in `?`. Questions wait on screen, verbatim with the asker's name (at most 3 visible), until the streamer pulls one with a hotkey and answers aloud. Non-questions never enter. Variant: other viewers `+1` a question, and the pulled question is pinned at the top of native Twitch chat via the Pinned Chat API.
- **First 10 seconds of the demo:** A viewer's question appears in a 3-slot stack; another viewer's "lol" does not; the streamer pulls the first question and it enlarges.
- **Closest existing things:** StreamerQnA and Meld AMA queue widgets; YouTube Live Q&A mode (Twitch has no native equivalent).
- **Notes:** The pin variant depends on an API untested on a new channel.

## C32: Private filtered chat view

- **What it is:** A private dock for the streamer with switchable lenses over chat: Questions, First-timers, Mentions, Mods. Nothing appears on stream.
- **First 10 seconds of the demo:** During a flood of trivia answers the streamer flips to "Questions" and sees the one real question.
- **Closest existing things:** Chatterino filters and highlights, Twitch mod view.
- **Notes:** none

## C33: Collective-control toys

- **What it is:** Chat votes slowly push a planchette across an on-screen Ouija board to spell an answer to the streamer's question, letter by letter. Variants: chat messages fall as blocks toward the facecam and the streamer clears lines by voice; three viewers each drive one backing loop on a music stream.
- **First 10 seconds of the demo:** The streamer asks "what should I eat?"; the planchette crawls to P-I-Z-Z-A.
- **Closest existing things:** Twitch Plays, chat polls.
- **Notes:** none

## C34: Maker continuity check

- **What it is:** A maker streamer declares a checkable step ("Stage C: both wings get two blue dots"). Viewers submit observations tagged to that stage (`!mark C left wing has one`); a mod approves; at a planned checkpoint the streamer opens a small checklist, fixes or dismisses each, and stamps the stage complete.
- **First 10 seconds of the demo:** A paper creature with mismatched wings; at the checkpoint one viewer observation appears; the streamer adds the missing dot and stamps "Stage C complete".
- **Closest existing things:** Checklists, backseating in chat, mod relays.
- **Notes:** none

## C35: Mobile moderation with undo

- **What it is:** A big-button phone page for moderators: a timeout needs a confirm tap, and a full-width Undo stays for 10 seconds and reverses it. Ban is placed far from Timeout.
- **First 10 seconds of the demo:** A mod accidentally times out a harmless viewer, hits Undo before the bar empties, and the viewer's next message lands.
- **Closest existing things:** Twitch's mobile mod view (where accidental bans happen), public `!timeout` commands.
- **Notes:** none

## C36: Raid pre-check

- **What it is:** Before raiding, the streamer picks a target and the tool shows whether the target's chat is follower-only and how long new followers must wait (e.g. 10 minutes), plus title and uptime. The raid is not started until the streamer confirms or picks someone else.
- **First 10 seconds of the demo:** The target is set to follower-only, 10 minutes; the streamer hits raid; a card says raiders won't be able to talk for 10 minutes; the streamer picks another channel and the real raid fires.
- **Closest existing things:** Twitch's raid screen sometimes hints at follower-only; streamers check the target's chat by hand. Several public posts ask Twitch for exactly this.
- **Notes:** Reading another channel's chat settings is expected to work but untested.

## C37: Private mod production panel

- **What it is:** A private phone web panel for moderators to run the show without public `!commands`: fire on-stream cards and lower-thirds, queue messages, drop stream markers with notes, send cues to the streamer ("guest ready"), and leave a handoff log for the next mod.
- **First 10 seconds of the demo:** A mod taps a button on a phone and a lower-third appears on stream; the mod's private note becomes a stream marker.
- **Closest existing things:** Streamer.bot and Mix It Up remote triggers, Twitch mod view.
- **Notes:** none
