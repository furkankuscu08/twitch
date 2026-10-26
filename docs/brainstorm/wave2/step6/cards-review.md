# Step 6 review: pre-comparison critique of the 10 cards

Independent reviewer. I read only cards.md, rules.md and A-capabilities.md. I do not rank the cards. Tags: **[Inn] [Imp] [Tech] [Des]**; hours are extra build hours.

Verified API facts used below (Helix reference, https://dev.twitch.tv/docs/api/reference/, read 2026-10-26):
- **Create Clip** has `title` and `duration` parameters (5–60 s, default 30). The title must pass AutoMod.
- **Create Stream Marker** fails if the channel has not enabled VOD storage.
- **Pin Chat Message** exists (`moderator:manage:chat_messages`, 30–1800 s).
- **Get Chatters** needs `moderator:read:chatters`.
- **The phone-verified-sender rule** applies to the *API sender* of a whisper.

---

## 1. Minefield

**Verdict:** Strong 20 seconds: a word, a BOOM, and a name. Judges get it instantly, and the hidden-target twist feels new. The risk is that the demo looks staged, because the builder controls all four accounts.

**Top problems**
- The "mod can cancel within 3 s" rule is ambiguous. If the explosion waits 3 s, the punchline dies. If it fires at once, "cancel" means undo.
- The speech-to-text spike is under-specified. Chunked faster-whisper adds 1.5–3 s of lag and can normalize words ("pine apple"). Vosk with a grammar limited to the planted words force-fits noise into false hits.
- The whisper risk is mis-stated. The phone rule covers whispers *sent* through the API. Whether viewers can whisper the bot from the Twitch client depends on client rules and the bot's "Block whispers from strangers" setting, which is unverified.
- The absorbed "Call it" mode costs 30 s of video and dilutes the idea.

**Improvements**
1. Explode instantly. A mod can "DEFUSE" within 10 s, which plays a rewind animation; the defuse becomes a gag. [Des] 0.3 h
2. Spotter: faster-whisper `tiny.en`/`base.en` with the `hotwords` parameter, a sliding 2 s window, and a whole-word match on normalized text. Keep Vosk partials as a fallback. Test with 30 min of casual talk. [Tech] 0 h
3. Clip with `title="Bo's mine: PINEAPPLE"` and `duration=30`. This is a verified parameter, so move it from stretch to in. [Des/Imp] 0.2 h
4. Cut "Call it" from the video. Spend those 30 s on the "dud reveal" montage: each failed bait is funny. [Des] −0 h
5. Dud reveal at the end: "Cy's mine 'GIRAFFE' never went off" with 3 s of the bait attempts (from marker timestamps). [Imp] 0.5 h

**One-liner:** keep. **Hook:** keep, but end the 20 s on the planter's chat line: "GOT HIM 😈".

**Fairness:** Fairly written. The speech-to-text risk is honestly flagged; the 3 s cancel window is the only unclear part.

---

## 2. Tap on the Shoulder

**Verdict:** A relatable pain, with a muted mic as the hook. A judge's first thought, though, is "OBS already knows my mic is muted." The core loop has many parts, and the "Test B" protocol is confusing on first viewing.

**Top problems**
- The hook problem can be detected without chat (obs-websocket `InputMuteStateChanged`). That undercuts the "human judgment" claim right at 0:00.
- `!heard B good` is high-friction syntax for viewers and hard to explain in a video.
- The Wake Lock API and phone pages need a secure context (HTTPS/wss). So the "phone over LAN WebSocket" plan needs the tunnel or mkcert, which the hours omit.
- The Tech strengthening is over-sold: it lists five components where the card has 9.5 h. The hours table already includes two stretch items (obs check, everyday states), so the real MVP is about 7.5 h plus shared infrastructure.

**Improvements**
1. Keep the mute hook, but add a second case OBS *cannot* see: wrong input device ("you sound far away") or game/voice balance. Say this in one line. [Inn] 0 h
2. Replace "Test B" with an automatic bot post: "Fix #2 — sound right now? 👍/👎". The label is attached for the viewer, and replies earlier than fix time + measured latency are ignored. [Des] −0.3 h
3. Make the obs-websocket mute check MVP. "Chat and OBS agree" is a stronger technical story than either alone. [Tech] 1 h (already counted)
4. Drop the lamp entirely; the phone face is enough. [Des] 0 h
5. Rename "Desk Buddy" in the video; judges will not know the term. [Des] 0 h

**One-liner:** "Chat can't tap you on the shoulder while you're heads-down — now it can: viewer reports and mod cues become a face on your desk, and chat confirms the fix."

**Hook:** Keep the muted mic. Add a caption "OBS can see this one…", then cut to "…but not this one" (a far-away mic) with the face panicking.

**Fairness:** Slightly over-sold on Technical, and it is the only card needing extra hardware (a spare phone in shot, plus a webcam).

---

## 3. VAR

**Verdict:** A strong, legible ritual: siren, slow motion, jury, stamp. "VAR" carries instant meaning. A judge may still think "replay buffer + poll," so the ritual polish must carry Innovation.

**Top problems**
- **Clip length:** the verified Create Clip maximum is **60 s**, not 90. Moment → latency (5–15 s) → two `!var` → stinger → 20 s replay → 20 s vote → stamp is about 60–70 s. So "a clip of the whole review" probably cuts off the original moment.
- Playing the replay inside a browser source depends on the container and codec. Default OBS formats (mkv, hybrid mp4) may not play in CEF. Serving the file costs 2 h as written, and that is the riskiest line.
- The replay buffer must be at least 45 s long to cover chat latency plus typing time. The card says "last ~20 s, shifted"; this is fine, but the buffer length is not stated.
- Two of the five video beats are explanations (latency 40 s, Codex). A second case at 0:50 for 50 s is long.

**Improvements**
1. Play the replay through an **OBS Media Source** controlled by obs-websocket (`SetInputSettings` local_file + `speed_percent: 50`). This avoids CEF codec risk. [Tech] −1 h
2. Shorten the review: 10 s replay (last 4 s slow), 15 s vote. Call Create Clip with `duration=60`, `title="VAR: NO BASKET"`. [Des] 0 h
3. "Self-VAR" as a recurring bit: the streamer calls it on a bold claim and chat overturns them. This is the most fun Impact angle; show it as case 2. [Imp] 0 h
4. Verdict history strip: "Streamer's claims upheld 2/5 today" (counters only, under 24 h). [Imp] 0.5 h

**One-liner:** keep. **Hook:** keep; end at 0:20 with the stamp, and roll the clip link at 0:25.

**Fairness:** Fairly written. The clip-length claim is wrong (see above).

---

## 4. Raid Torch

**Verdict:** A poetic concept, and the fly-in is a nice beat. But judges see one person's two channels, so "community relay" stays imaginary. Impact depends on network adoption a judge cannot see.

**Top problems**
- The one-sided mode is over-sold. A send-off with no receiver is essentially a raid alert.
- `channel.raid` needs no authorization, so a single WebSocket can watch any channel's raids. "EventSub raid on two channels" is cheaper than 1 h. The *shared public backend* is the real cost: a tunnel from a laptop is not a believable multi-streamer service.
- `!mark <emote>` renders only Twitch-native emotes. Message fragments carry Twitch emote IDs; 7TV/BTTV emotes, which many small chats use, are just text.
- The 24 h framing is backwards. Raid trains are same-evening events, so a same-day relay is the natural design, not the fallback.

**Improvements**
1. "Torch-bearers": after a raid, a raider who added a mark and chats in channel B gets a glow ("Ana carried a mark from A"). The target streamer learns who the raiders are, which is real host value. [Imp/Inn] 1 h
2. Make it a same-day relay by default and drop the test-#12 dependency. [Tech] 0 h
3. Video: show a 3-hop journey (two rehearsal hops, labeled as such) so the map is not trivial. [Des] 0.3 h
4. Deploy the backend to a free PaaS rather than a tunnel, and say so in the video. [Tech] 0.5 h

**One-liner:** "A torch that only travels by raid: every chat that holds it leaves a mark, and the raiders who carried it light up when they arrive."

**Hook:** keep, but add the raiders' names glowing as they chat in B.

**Fairness:** The Impact section is mildly over-sold, and the demo-reality gap is under-discussed relative to the other cards.

---

## 5. Previously On

**Verdict:** The TV metaphor is instantly readable and charming; good Design. A judge's doubt is "a fancy raid alert," and the card addresses it.

**Top problems**
- "Auto-beats mean the recap is never empty" is over-sold. Small streamers rarely change title or category mid-stream.
- "Markers and VOD chapters as a by-product" is weak: Twitch already auto-creates chapters on category changes. Markers also fail without VOD storage enabled.
- The Pin risk (#1) is now resolved: Pin Chat Message is a documented endpoint, so the stretch is cheap.
- Raids are rare for small channels, so most real usage is `!recap`. Glossary footnotes (2 h) are the costliest and least-seen part.

**Improvements**
1. Auto-beats from **existing habit**: poll Get Stream Markers (`user:read:broadcast`) every 30 s. Any marker the streamer makes with Twitch's own marker shortcut or a Stream Deck becomes a beat. [Imp/Tech] 0.5 h
2. Story So Far: the bot sends the recap and pins it for 10 min with `duration_seconds=600`. Move this into MVP. [Imp] 0.5 h
3. Cut glossary footnotes to the first-mention footnote only, or drop them. [Tech] −1.5 h
4. Replace the 2:00 "markers/VOD" beat with a late viewer typing `!recap` and replying "ohh ok". [Des] 0 h

**One-liner:** keep. **Hook:** keep.

**Fairness:** Its claims are slightly over-sold, but the card is otherwise balanced.

---

## 6. Studio Audience

**Verdict:** The audio hook is the strongest sensory hook here: three viewers and a full house. But "three viewers sound like a full house" reads as fake engagement on a platform that polices it.

**Top problems**
- The framing risk is under-stated. Lead with "every laugh is a real person," not "sounds like a full house."
- The 1:30 headphone-mode beat cannot be shown: the video viewer hears the stream, not the monitor.
- Formant shift is not a Web Audio built-in. `playbackRate` changes pitch and speed together. Use a sample pool × rate × EQ per ID instead.
- Follow EventSub needs `moderator:read:followers`; Get Chatters needs `moderator:read:chatters`. Add both to the scope list.

**Improvements**
1. Reframe the one-liner around traceability: each voice is a named, real viewer, and the crowd cannot exceed the distinct reactors. [Imp/Inn] 0 h
2. Show headphone mode as a picture-in-picture labeled "what the streamer hears" with a waveform. [Des] 0.3 h
3. Make chants MVP (the word appears on screen); they are the most watchable beat. [Des] 0.5 h
4. Drop lurker seats from the video. [Des] 0 h

**One-liner:** "Chat becomes a live theater crowd you can hear — every laugh belongs to a real, named viewer, and it only gets louder when more people react."

**Hook:** keep.

**Fairness:** The Innovation section under-states KappaGen-style emote explosions (see cross-card). The technical side is fine.

---

## 7. Foley Pit

**Verdict:** It is charming if the performer is funny; the tool itself is a card UI plus a level meter. Onset detection only proves "a sound happened," so Tech and Innovation are under-sold. That is odd for an ML-engineer builder.

**Top problems**
- Onset detection is a thin technical story: the overlay reacts to *any* noise.
- The rating step ("chat rates with emotes") is vague and anticlimactic.
- The closest-existing list misses **ASMR trigger requests**, the obvious analogue and a large audience, and Whose Line's "Sound Effects" game.
- The 3-minute video has no beat showing why viewers return.

**Improvements**
1. A "Foley meter": a zero-shot audio-text model (CLAP, or YAMNet AudioSet classes such as Thunder, Rain and Footsteps) scores each performed sound against its cue: "spoon footsteps: 71% footsteps." This makes it a game and plays to the builder's ML skill. [Inn/Tech/Des] 2 h (take it from polish and rating)
2. Make the reel clip MVP: Create Clip with `duration` set to the scene length plus a title. [Imp] 0.3 h
3. Position it for ASMR and craft streams in the Impact text. [Imp] 0 h
4. Replace emote rating with the final Foley score plus a one-word chat verdict. [Des] −0.5 h

**One-liner:** "Chat writes the sound-effects score, the streamer performs it with a cup and a spoon, and an audio model judges how much the spoon sounded like footsteps."

**Hook:** keep, but end on "CUP THUNDER: 12% thunder" with chat laughing.

**Fairness:** Under-sold relative to the others; it has no Tech claim of comparable ambition.

---

## 8. Hint Jar

**Verdict:** A real, well-known pain (backseating), and "sealed tiered hints" is a clean idea. But the no-commercial-games rule forces a paper-riddle demo, which undercuts "blind playthroughs."

**Top problems**
- The demo setting fights the use case; a judge must imagine the real game.
- Jar physics at 2.5 h is the largest line, and it is decoration.
- Whisper intake is listed in both the core loop and stretch, which is inconsistent. The whisper-sending feasibility is unverified (see card 1).
- The 2:00 "why backseating matters" beat comes too late; the problem should open the video.

**Improvements**
1. Have Codex build a tiny original browser puzzle game as the demo "playthrough." It avoids trademarks and doubles as Codex footage. [Imp/Tech] 1 h
2. Physics via matter.js presets, or CSS stacking. [Tech] −1.5 h
3. Chat vote to "crack a nudge?". The streamer can open early only if chat agrees, which adds audience agency. [Des] 0.5 h

**One-liner:** keep.

**Hook:** Chat fills with "IT'S THE LEFT DOOR" backseat spam, which gets struck out, and "3 hints sealed" appears. The stuck streamer taps once; a nudge opens and the answer stays sealed.

**Fairness:** Fairly written. The demo-setting problem is under-stated.

---

## 9. Photo Booth

**Verdict:** Warm and visual; the Polaroid develop is pleasing. But a near-identical product exists: StreamUP's "Polaroid Picture" for Streamer.bot (a channel-point redeem takes a Polaroid of an OBS source). The current claimed difference does not survive that.

**Top problems**
- **The Innovation claim is invalidated** by StreamUP Polaroid Picture (https://streamup.notion.site/Polaroid-Picture-Documentation-a0f36c6cb1604ffba21ded3945a469b5).
- Links served through a tunnel on the streamer's PC die when the PC sleeps.
- "Streamer's face in shared links" is a real privacy risk, under-stated.
- The technical story is thin: one `GetSourceScreenshot` call.

**Improvements**
1. **"Photo with the viewer":** composite the viewer's Twitch avatar (Get Users `profile_image_url`) into the frame next to the streamer, like a TwitchCon meet-and-greet photo. This is the real difference, and it fits the TwitchCon theme. [Inn/Imp] 1–1.5 h
2. Make the raid group photo MVP: all raiders' avatars squeezed into the shot. [Inn/Des] 1 h (already counted)
3. A blur/consent toggle: the streamer can blur the face, or capture only a "booth" scene. [Imp] 0.3 h
4. Name StreamUP in the card and differentiate explicitly. [Inn] 0 h

**One-liner:** "Meet-and-greet for every viewer: type `!snap`, and you and the streamer pose together in a Polaroid that develops live — and the whole chat ends up on the corkboard."

**Hook:** `!snap`, then the streamer leans toward an empty spot, the flash fires, and the Polaroid develops with Ana's avatar beside them.

**Fairness:** Over-sold on Innovation because a direct competitor is missing.

---

## 10. Checkpoint

**Verdict:** Useful and honest, but the hook ("split screen, crystals") is abstract. In 20 s a judge sees "a chat queue overlay." Innovation and Design need a sharper moment.

**Top problems**
- The closest-existing list misses "feature a chat message on stream" overlays (e.g., Social Stream Ninja's featured message, StreamElements chat highlight; known, link unverified). Those overlap with the call-in card.
- The viewer gets no signal that they were answered.
- "Why it isn't a question queue" (30 s) is defensive explaining.
- Its hours (8.5 h) are the lowest of the ten, which leaves room to add a distinctive feature.

**Improvements**
1. On "next," the bot sends a threaded reply (Send Chat Message with `reply_parent_message_id`): "✓ answered on stream at 12:04." The viewer gets a ping, which is concrete Impact. [Imp] 0.5 h
2. A context thumbnail: each saved message stores an obs-websocket screenshot from when it was sent, kept locally under 24 h. The card shows "you asked this while I was inking the eyes." [Inn/Tech/Des] 1 h
3. Make the urgent lane MVP and drop the reminder from the video. [Des] 0 h

**One-liner:** "Go heads-down without ghosting chat: messages become save crystals, and at the checkpoint each one gets a call-in card, an on-stream answer, and a reply ping."

**Hook:** The streamer is inking and 6 crystals stack up. "CHECKPOINT" plays. The card reads "@ana (first time!): what pen is that?", the streamer answers, and Ana's chat shows "✓ answered."

**Fairness:** Under-sold on hook and Design compared with cards 1, 3 and 6.

---

## Cross-card

**Template consistency**
- Strengthening headers are tagged unevenly: (Impact), (Innovation), (Technical), none (#7), or prose (#5). Tag the weakest criterion on every card.
- Hours tables mix in stretch items. Cards 2, 5, 6, 9 and 10 count stretch inside the total; card 1 excludes "Call it." Give every card an MVP subtotal and a stretch subtotal.
- Risks cite filter.md test numbers that a reader of cards.md cannot see. Cards 6, 7 and 10 have no numbered day-1 test.
- Demo setup says "no hardware," yet cards 1, 3, 7, 9 and 10 need a webcam and mic in shot. List them.

**Facts appearing in several cards**
- **Create Clip:** title is supported; length is 5–60 s, default 30. Cards 1, 3 and 7 treat title as unverified, and card 3 assumes a longer clip.
- **Stream markers** need VOD storage enabled. This affects cards 1, 3 and 5; make it a day-1 checkbox.
- **Whispers:** the phone rule covers API senders. Viewer→bot whisper feasibility is a separate, untested question (cards 1, 8).
- **Missing scopes:** `moderator:read:chatters` (6), `moderator:read:followers` (6), `moderator:manage:chat_messages` for pin (5), `user:read:broadcast` for markers (5).

**Shared infrastructure, under-estimated**
- **Auth and events:** Twitch app plus 2FA, auth-code OAuth for broadcaster and bot, token refresh, EventSub WebSocket with the 10 s subscribe window and reconnect, overlay push, OBS docks, and obs-websocket auth. For a Twitch newcomer that is realistically **2–3 h** even with Codex. Cards budget 0–1 h; cards 3, 6, 7 and 10 budget zero. Every "≈9 h" card is really about 11 h.
- **Public URLs:** tunnel-based pages (1, 2, 8, 9) need a stable domain registered as an OAuth redirect URI. A free static ngrok domain or a PaaS works.
- **A shared chat simulator** (scripted accounts replaying a chat script over the real API, since the CLI cannot mock `channel.chat.message`) should be one line item. It is also the best **Codex footage**: Codex wrote the test harness, and the harness drives the demo.

**Codex story:** Every card gives a generic 25 s "Codex, close." The criterion explicitly scores Codex use, and rules require one Codex session ID. Each card should name one concrete Codex artifact (simulator, audio pipeline, overlay physics, puzzle game).

**Missing competitors**
- **#1:** stream-bingo overlays, e.g., 1up.vision Bingo (https://docs.1up.vision/bingo.md), plus the "if I say X…" streamer challenge bit.
- **#2:** Twitch Guardian, a keyword-alert Chrome extension (https://chromewebstore.google.com/detail/fcfdekecgocobpjhldifpplcifkfflme), and obs-websocket mute alerts.
- **#3:** Streamer.bot instant-replay actions (known, link unverified).
- **#4:** R3dLabs Toolbox raid-train Stream Deck plugin (https://marketplace.elgato.com/@r3dlabs) and RaidRunner raid-train scheduling.
- **#5:** Twitch's automatic VOD chapters (known).
- **#6:** KappaGen emote explosion, StreamElements (https://support.streamelements.com/hc/en-us/articles/10474578102802-How-to-Set-Up-Emote-Explosion-Widget-KappaGen).
- **#7:** ASMR trigger requests via channel points; Whose Line "Sound Effects."
- **#8:** channel-point "backseat allowed for 1 min" rewards (common pattern, unverified).
- **#9:** StreamUP Polaroid Picture (link above).
- **#10:** featured-chat-message overlays (Social Stream Ninja, StreamElements; unverified links).
