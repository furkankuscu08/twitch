# L2: Spectacle-driven ideas

Labels: **[V]** verified (source read or brief evidence), **[S]** search summary or secondary source, **[I]** inference, **[U]** unknown. Prior-art checks were quick web searches on 2026-10-25. "Not found" means absence of evidence, nothing stronger.

**Lens notes.** Three patterns survive the latency and tiny-audience filters and still look good on video:
1. **Viewers plant it, the streamer sets it off.** Viewers act in advance. The payoff fires on the streamer's side the moment the streamer does something (says a word, laughs, misses a shot). Viewer latency stops mattering, and the streamer's real reaction becomes the clip.
2. **Amplify, don't demand.** Make what a small chat already does (an emote, a "hi") big in sound or in the room. Lurkers are never asked to do more.
3. **One personal moment per viewer.** What would be spam in a 5k chat is a feature at 3 viewers.

**Video constraint.** The rules forbid third-party copyrighted material in the video without permission [V, rules.md], so the demos below use IRL desk content instead of commercial game footage.

---

## A. Crowd map

1. An LLM co-host or chatbot with a persona and a TTS voice that answers chat.
2. An LLM "what did I miss" chat summarizer or question-surfacing dashboard.
3. Twitch Plays <game> (chess, a Pokémon-like, a browser game) driven by chat commands.
4. AI-generated trivia or quiz with a points leaderboard overlay.
5. Home-made polls or predictions with a points economy (native polls may be gated).
6. A dice roller or TTRPG overlay (organizer example).
7. A chat-spike auto-clipper with AI titles or a highlight reel.
8. Chaos and distraction effects: chat triggers screen shake, filters, jumpscares, TTS.
9. Chat avatars or a virtual pet living on the overlay.
10. A stream-vs-stream battle or shared scoreboard, or a sports or game-stat overlay.

## B. Wide list

1. **Minefield.** Viewers plant secret word mines; the streamer's own speech sets them off. `need #2 (lurker-safe)`, `streamer-side trigger`, `clips`
2. **Sound Tags.** Viewers attach a sound to a streamer catchphrase ("every 'okay' quacks"). `streamer-side trigger`, `need #10`
3. **Try Not To Laugh.** Viewers submit jokes; webcam smile detection decides if the streamer cracked. `streamer-side trigger`, `clips`
4. **Studio Audience.** Chat reactions become a scaled crowd soundscape with signature laughs. `need #1`, `need #2`
5. **Leitmotif.** Each chatter gets a generated musical motif; present viewers form a copyright-safe background score. `per-channel identity`, `need #1`
6. **Lurker Sky.** Each logged-in viewer is a star at a hash-fixed spot; a first message makes it flare. `need #2`, `raid`
7. **Desk Buddy.** The old phone on the desk becomes chat's on-camera face. `need #1`, `physical output`
8. **Glow.** A smart bulb in shot takes the color of whoever is chatting. `need #1`, `physical` (overlaps Lumia Stream)
9. **Wall of Firsts.** A thermal printer prints each first-time chatter; the streamer pins it on the real wall. `need #3`, `physical`
10. **Photo Booth.** `!snap`, the streamer poses, a Polaroid develops on screen. `tiny audience`, `discoverability`
11. **VAR!** Chat calls a replay review, a chat jury rules, a titled clip is made. `need #8`, `clips priority`
12. **Previously On.** Last stream's chat-marked moments open the next stream as a TV cold open; `!lore` for newcomers. `need #3`, `clips`
13. **Director's Chair.** One viewer at a time directs camera crops and filters, credited on screen. `tiny-audience roles`
14. **Call-in Line.** Viewers leave 15-second voicemails; the streamer airs them with a retro phone overlay. `talk shows`, `non-typers`
15. **Haunt.** Viewers plant left/right positional creaks into a horror game's audio. `streamer distraction`
16. **Ouija.** Chat votes slowly push a planchette to spell answers. `collective control`
17. **Raid Baton.** Your chat co-writes a one-line baton carried on screen into the raided channel. `raid handoff`
18. **Sip Watch.** The webcam spots the streamer's mug; chat bets on the next sip. `locked-in predictions`
19. **Ticket Stubs.** Each attendee gets a numbered stub for that stream ("seat 3 of 4"). `per-channel identity`
20. **Trio Jam.** On music streams, three viewers each drive one backing loop. `tiny audience`
21. **Gravity Tetris.** Messages fall as blocks toward the facecam; the streamer clears lines by voice. `layout changes`
22. **Bounty Board.** Viewers post tiny IRL dares settled by a VAR-style check. `challenge`

---

## C. Five full cards

### Minefield
- **One-liner:** Viewers secretly plant "word mines". When the streamer says a mined word out loud, it explodes on stream with the planter's name and a titled clip is created.
- **Who installs it / who gets the value:** The streamer installs a bot, a local speech listener and an overlay. *Streamer:* a running gag at any viewer count that turns ordinary talk into clip moments. *Viewers:* a 5-second action that pays off later with their name on screen, plus a reason to talk to the streamer (baiting). *Mods:* `!mines` to list or clear.
- **Streamer category fit:** Just Chatting, talk-heavy gaming, art, cooking, podcast-style streams; any language the speech model supports [I].
- **Core loop:**
  1. A viewer types `!mine pineapple`. The bot, as a moderator, deletes the message within about a second and posts "💣 Bo planted a mine (3 live)".
  2. The overlay shows three mine chips with owner names, never the words.
  3. Viewers steer the conversation toward their words ("worst pizza topping?").
  4. The streamer says "pineapple", and a local recognizer matches it in about a second [I].
  5. Explosion, screen shake, and the banner "Bo's mine: PINEAPPLE (planted 6 min ago)". The bot posts in chat, and the app creates a clip and a stream marker.
  6. Unexploded mines expire as "duds" with a small reveal (blocklist-checked).
- **First 10 seconds of the demo:** The corner shows "💣 3 mines live" with chips for Ana, Bo and Cy. The streamer is chatting about lunch: "...honestly, pineapple on pizza is—" BOOM. The screen shakes, the banner names Bo, and the streamer yells "WHO baited me?!" Cut to Bo's chat message from four minutes earlier: "what's the worst pizza topping?"
- **Twitch surfaces used:** EventSub `channel.chat.message`; Helix Send Chat Message, Delete Chat Messages (bot as moderator), Create Clip (new optional title parameter [S]), Create Stream Marker; OBS browser source; local offline speech-to-text on the mic only (Vosk or faster-whisper). Optional: planting by whisper (`user.whisper.message` [S]).
- **Works with 1 streamer + 3 test accounts? How?** Yes, this is the ideal size. Each account plants one mine, so each of the three viewers owns a third of the danger. The baiting conversation is the script.
- **Closest existing thing and the meaningful difference:** Speech-recognition swear jars (a Vosk-based Minecraft mod [S], JarGone hardware [S]); OK Gamers (2019 grand prize) used streamer speech to start a poll [V, D]; Taboo. *Difference:* the audience picks secret targets, so it is a viewer-vs-streamer game hidden inside normal talk, not a self-imposed filter. No Twitch tool found [U].
- **Why wouldn't 30 other teams build this?** It needs a streamer-side speech pipeline (rare among overlay builders) and inverts the default "chat controls X" pattern. It runs underneath normal streaming, not as a separate game mode.
- **Evidence it links to:** #2 (lurker-safe: one action, no "keep chat alive" pressure; a reason to talk *to* the streamer [I]); #1 (the streamer never needs to read chat [I]); Twitch's 2026 clips priority [V]. Fun is unvalidated: run a 20-minute session with 3 friends and count plants and baiting messages.
- **MVP scope / explicitly out of scope:** *In:* planting with secret deletion; overlay chips; whole-word matching; explosion; clip and marker; dud expiry; word rules (4+ letters, not in a top-1000 frequency list, blocklist, one live mine per viewer). *Out:* cross-stream leaderboards, a defuse mini-game, multi-word phrases, any LLM.
- **Riskiest assumption:** Speech-to-text catches casual speech over game audio with few false positives (1-hour spike on day 1). Second: streamers enjoy being baited rather than feeling policed.

### Studio Audience
`Familiar base: alert/overlay tools (sound alerts)`
- **One-liner:** Chat's reactions become a live theater crowd you can hear. Every LUL is a laugh and every "L" a boo, so a 3-person chat sounds like a full house and the streamer hears chat without reading it.
- **Who installs it / who gets the value:** The streamer installs one browser source. *Streamer:* hears reactions mid-game, on air or in a headphone-only mode. *Viewers:* no extra effort; each gets a signature laugh derived from their user ID (nothing stored, `!mylaugh 7` to change), so regulars are recognizable by ear. *Mods:* a mute command.
- **Streamer category fit:** comedy, Just Chatting, IRL challenges, gaming fails, variety.
- **Core loop:**
  1. A viewer sends an emote or keyword. A lookup table maps it to a reaction: laugh, gasp, aww, applause or boo.
  2. The crowd engine mixes CC0 samples. Intensity scales with *distinct* reacting viewers, so spam can't inflate it.
  3. The viewer's own laugh rises out of the crowd, and their seat silhouette in a bottom strip bounces with a name tag.
  4. The same word from 2+ viewers within 10 seconds becomes a clap-chant with the word on screen. A follow brings applause; a raid opens the doors, adds N seats and a roar.
- **First 10 seconds of the demo:** The streamer misses a paper-ball shot into a bin. One account types "L" and two type "LUL". A packed theater boos, then laughs, and three silhouettes bounce with their names. The streamer takes a bow, and the crowd applauds.
- **Twitch surfaces used:** EventSub chat, follow and raid; Get Chatters (`moderator:read:chatters`, broadcaster or moderator token [S]) to seat lurkers as dim silhouettes; an OBS browser source with audio.
- **Works with 1 streamer + 3 test accounts? How?** Yes. The joke is exactly that 3 people sound like 300, with each viewer acting as one "section" of the house.
- **Closest existing thing and the meaningful difference:** Streamlabs' single new-chatter sound [S]; Streamer.bot "first words" per-user sounds [S]; Sound Alerts (paid soundboard); Meld's Emote Storm scales *visual* emotes with activity [S]. No chat-to-crowd soundscape found [U]. *Difference:* one mixed, scaled crowd from free actions, with each viewer identifiable, instead of one-shot sounds.
- **Why wouldn't 30 other teams build this?** Teams think visually and try to make chat talk *more*. This amplifies what already exists. Audio design is outside most hackathon comfort zones.
- **Evidence it links to:** #1 (perceive chat without reading) [V]; #2 (amplify without demanding, lurkers untouched) [V]; #10 (pick your laugh) [V]. Whether it stays pleasant is unvalidated: run a 30-minute session and check the streamer leaves it on.
- **MVP scope / explicitly out of scope:** *In:* 6 reaction types, 20+ CC0 samples, distinct-viewer scaling, signature laughs, the seat strip, follow and raid events, a monitor-only toggle, a volume cap. *Out:* TTS chants of arbitrary words, viewer-recorded audio, per-game sound packs.
- **Riskiest assumption:** That the delight lasts past minute 10 and doesn't turn into canned-laughter cheese. Judges might also read it as "fake engagement". The counter is showing a real name behind every sound.

### VAR!
`Familiar base: polls + chat-triggered instant replay`
- **One-liner:** When chat disputes a moment, two `!var` calls start a broadcast-style review: slow-motion replay, a 20-second chat jury, a verdict stamp and an auto-titled clip.
- **Who installs it / who gets the value:** The streamer installs a bot, the OBS replay buffer (via obs-websocket) and an overlay. *Streamer:* disputes become segments, each leaving a curated clip. *Viewers:* their skepticism becomes the referee's call, with their names on the jury. *Mods:* call or cancel a review.
- **Streamer category fit:** IRL trick shots and challenges, speedrun claims, sports and fighting games, board games, cooking ("is it raw?"), art ("did they trace it?").
- **Core loop:**
  1. The streamer claims something.
  2. 2 distinct viewers type `!var` within 30 seconds. The threshold scales with the number of active chatters.
  3. A "VAR CHECK" stinger plays with a whistle.
  4. obs-websocket saves the replay buffer. The overlay replays the last ~20 seconds, shifted by a latency offset, with the final 5 seconds at 50% speed in picture-in-picture.
  5. Chat votes `!yes` or `!no` for 20 seconds, with names shown on a jury bench.
  6. A verdict stamp appears, and the app creates a clip ("VAR: NO BASKET, called by Ana") and a marker.
- **First 10 seconds of the demo:** The streamer throws a paper ball: "IN! That's in!" Two accounts type `!var`. A siren sounds and the slow-motion replay shows the ball bouncing off the rim. Three jurors vote, the stamp reads "NO BASKET ❌", the streamer protests, and the clip link lands in chat.
- **Twitch surfaces used:** EventSub chat; Helix Create Clip (title and duration parameters, up to 90 seconds [S]), Create Stream Marker and Send Chat Message; an OBS browser source; obs-websocket (local).
- **Works with 1 streamer + 3 test accounts? How?** Yes. Two callers and three jurors, while the streamer argues their case.
- **Closest existing thing and the meaningful difference:** The OBS "Instant Replay" Lua script already lets viewers trigger a picture-in-picture replay with a chat command [S, obsproject.com]. *Difference:* the review ritual (jury, verdict, stamp, titled clip). The replay is only the means. The verdict is the show.
- **Why wouldn't 30 other teams build this?** Poll builders stop at a widget. Replay plumbing, latency offsets and sports-broadcast design are rarer. To be honest, someone may build "instant replay", so the jury is the differentiator.
- **Evidence it links to:** #8 (clip workflow) [S]; Twitch's 2026 clips-and-highlights priority [V]; "locked-in picks with a reveal" [S]. How often disputable moments happen on small streams is unvalidated: ask 3–5 streamers or watch small IRL and challenge streams live.
- **MVP scope / explicitly out of scope:** *In:* call threshold, replay with slow motion, vote, stamp, clip and marker, a latency offset slider. *Out:* telestrator drawing, multi-camera angles, AI judging.
- **Riskiest assumption:** That the replay lands on the right moment despite 2–30 seconds of viewer latency. The plan is a 60-second buffer, a streamer-set offset and a "nudge back" hotkey.

### Desk Buddy
- **One-liner:** The old phone a streamer already props up to read chat becomes chat's face on the desk. It waves at newcomers, laughs at LULs and raises a hand when a question is waiting. The streamer can read it at a glance, and viewers see it on camera.
- **Who installs it / who gets the value:** The streamer opens a URL on any phone or tablet (QR pairing). *Streamer:* peripheral awareness of who is new, whether a question is waiting, and the mood, without reading. *Viewers:* their message visibly moves an object in the streamer's room. *Mods:* `!q` flags a question.
- **Streamer category fit:** single-monitor gaming with a controller, art, cooking, music performance (hands busy), IRL desk streams. VR is not a fit.
- **Core loop:**
  1. A viewer chats, and the server classifies the message as one of: first-time chatter, returning regular, emote mood, question ("?" or `!q`), follow or raid.
  2. The phone face reacts: newcomers get a wave and their name in huge letters; regulars get their color (derived from user ID, nothing stored); emotes become expressions.
  3. Questions stack up as a raised hand with a counter. One tap shows the question in big text, and a second tap clears it.
  4. When chat is quiet, the buddy dozes. This is honest and doesn't guilt anyone.
- **First 10 seconds of the demo:** A wide shot shows the streamer drawing, with a phone propped beside the monitor showing a big-eyed face. Cy types "hi, first time here!" The phone waves and shows "NEW: CY", and the streamer says "welcome Cy!" without putting the pen down. Ana asks a question, and the buddy's hand goes up.
- **Twitch surfaces used:** EventSub chat, follow and raid; Helix Send Chat Message (the bot confirms "question queued"); a phone web page over WebSocket with Wake Lock; an optional OBS browser-source mirror.
- **Works with 1 streamer + 3 test accounts? How?** Yes. A newcomer, a regular and a question-asker cover every state.
- **Closest existing thing and the meaningful difference:** Elgato's Mochi the Cat (on-screen pet reacting to chat) [S]; Elgato Prompter Chat Mode (chat on a teleprompter) [S]; a DIY ESP32 "hype robot" [S]; reading chat on a propped phone (need #1 workaround) [V]. *Difference:* not a pet (crowd map #9; no care loop), no new hardware; it shows the *state* of chat (new, question, mood) at a glance, and it lives in the room, on camera.
- **Why wouldn't 30 other teams build this?** Teams default to overlays, and physical output looks hard. This is physical with zero hardware to buy.
- **Evidence it links to:**
  - #1: the most consistent need, found in three sources [V].
  - #2: loneliness, since the buddy is a presence [V].
  - Past winners with physical outputs [V, D] (descriptive only).
  - That a glance beats reading is unvalidated. To validate, have 2–3 streamers try it for one session each.
- **MVP scope / explicitly out of scope:** *In:* 6 states, the question queue with tap, color identity, Wake Lock, QR pairing. *Out:* a native app, smart lights, voice output, iOS haptics.
- **Riskiest assumption:** That it is clearly better than plain chat on the same phone. If it isn't, it is just a mascot.

### Photo Booth
- **One-liner:** A viewer types `!snap`. The streamer gets a cue and strikes a pose, the overlay counts down and flashes, and a Polaroid of the moment develops on screen with the viewer's name and caption. All snaps form a "class photo" at the end of the stream.
- **Who installs it / who gets the value:** The streamer installs a bot, obs-websocket and an overlay. *Viewers:* a personal souvenir and their name on stream, with a link to save it. *Streamer:* a warm per-viewer ritual built for small numbers, plus shared images that carry the channel name [I]. *Mods:* approve or skip the queue.
- **Streamer category fit:** Just Chatting, IRL, art (a snap of the canvas), cosplay, cooking, music.
- **Core loop:**
  1. A viewer types `!snap first win!` (1 per viewer per stream). The streamer hears a chime and sees the name.
  2. The overlay counts down 3-2-1; obs-websocket GetSourceScreenshot grabs the camera or program frame.
  3. A Polaroid slides in and develops over 5 seconds, captioned "Ana · first win! · Oct 30". The bot posts a link that expires after 24 hours [I, stays inside the storage rule].
  4. The photo joins a corkboard strip. The outro scene shows the collage "who was here today".
- **First 10 seconds of the demo:** Ana types `!snap first win`. A shutter chime plays, the streamer holds up a trophy mug, a flash fires, and a Polaroid develops in the corner. Cut to the end of the stream: a corkboard with three Polaroids and "4 of us were here".
- **Twitch surfaces used:** EventSub chat and raid (a raid triggers a "group photo with the raiders"); Helix Send Chat Message; an OBS browser source; obs-websocket.
- **Works with 1 streamer + 3 test accounts? How?** Yes. Three snaps make a full corkboard; the design assumes a small chat.
- **Closest existing thing and the meaningful difference:** Generic chat-to-overlay commands [S]; physical subscriber-slip printers [S]; no snapshot or Polaroid tool found [U]. *Difference:* the streamer poses, each photo is captioned and collectible per viewer, and the stream ends in a collage.
- **Why wouldn't 30 other teams build this?** It deliberately doesn't scale to big chats, which is counter-intuitive, and few teams touch OBS frames.
- **Evidence it links to:** Twitch's discoverability priority [V]; per-channel identity and attendance mechanisms [V pattern, love unproven]; #3 (a newcomer gets a personal moment) [I]. Mostly unvalidated.
- **MVP scope / explicitly out of scope:** *In:* snap, countdown, Polaroid, caption, corkboard, collage, expiring link page. *Out:* AI stylization. Printing a physical copy to pin on the wall is a stretch goal.
- **Riskiest assumption:** That viewers of a small streamer want souvenirs, and that streamers are comfortable with their face going out in links.

---

## D. Parked

- **Click to place things on the video (Heat-style).** Needs an Extension. *Would need:* an approved Extension in time.
- **Red Light Green Light (viewers move while the streamer looks away).** Breaks the latency filter. *Would need:* viewer latency under 1 second.
- **Hydrate-style physical rewards through channel points.** Custom Rewards may be affiliate-gated [U]. *Would need:* the day-1 Create Custom Reward test to pass. A chat-command version already passes the filters.
- **A buddy that remembers what you said last stream.** Breaks the 24-hour storage rule. *Would need:* only derived counts, no content, to be allowed [U].
- **Live cross-channel Pong.** Latency, plus two live channels. *Would need:* a turn-based redesign.
- **Spoiler-proof predictions using stream delay.** Stream delay is unavailable on new channels [V]. *Would need:* Affiliate status.
- **Live viewer voice or video guests (Guest Star).** It is in beta [V] and hard to demo solo. *Would need:* stable API access plus real guests.

## E. My pick

**Minefield.** It is the only card where the best moment is generated entirely on the streamer's side, so 2–30 seconds of latency doesn't matter. Three viewers is the ideal count (one mine each), and the clip writes itself: the streamer's real reaction to their own word, with the bait message as the punchline. It matches nothing on the crowd map, needs no generative AI (speech-to-text is plainly the right tool, and it plays to the builder's strengths), and gives lurkers a one-time action instead of a duty to keep chat alive. The main risk, speech matching, can be confirmed or ruled out in a 1-hour spike on day 1. If the spike fails, Desk Buddy is the fallback (lowest technical risk, strongest need). If time remains, Studio Audience's crowd gasp could be a 1-hour add-on to the explosion.
