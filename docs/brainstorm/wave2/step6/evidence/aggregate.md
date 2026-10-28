# Evidence: merged picture for the 7 remaining cards

Merged 2026-10-28 from three independent research reports ([evidence-astra.md](evidence-astra.md), [evidence-grok.md](evidence-grok.md), [evidence-claude.md](evidence-claude.md)), a targeted link check ([linkcheck.md](linkcheck.md)) and, for Checkpoint only, the pivot draft ([../pivots/checkpoint-draft.md](../pivots/checkpoint-draft.md)). Rules: [README.md](README.md). No scores in this file.

Researcher codes: **A** Astra, **G** Grok, **C** Claude, **L** link check, **P** pivot draft.

How to read the status column:
- **Confirmed**: found by two or more researchers.
- **Verified**: found by one researcher, and the link check opened the page.
- **Unverified**: the page could not be opened (blocked site, Reddit, X, or snippet only). It may well exist; it is not counted as confirmed.

"Well-known" follows README: a major platform or tool (Twitch, StreamElements, Streamlabs, Streamer.bot, Elgato, OBS, Meld, Sound Alerts, StreamUP), ≥1,000 users or installs, ≥100 GitHub stars, or a post with ≥10,000 views.

## Decisions taken in this step

- **Eliminated by the user:** Previously On, Photo Booth, Foley Pit (see the end of this file).
- **Demo games:** a commercial game is not needed. Where a card's natural setting is a game, the demo uses a small original game built with Codex (about 1 h) or an MIT-licensed open-source game. "Natural-setting demo" below already reflects this.
- **Checkpoint pivot:** the user ruled Checkpoint the same core loop as the Meld X AMA Question Queue (well-known), and approved its one pivot: spoken answers with answer receipts. Its post-pivot evidence comes from one source (P), not three.
- **Dropped under the link rule:** PROVE IT (VAR), Raid Train (Raid Torch), Twitch Sense (Studio Audience). All three are Devpost pages that refused the fetch, and no other trace was found; the Twitch 2017 hackathon recap does not list Twitch Sense.

## Summary table

| Card | Highest overlap | Closest well-known thing | Difference survives (A / G / C) | Demand evidence | Counter-signals | Natural-setting demo | Type-independent |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1. Minefield | Partial | Streamer.bot Voice Control | Yes / Yes / Yes | Indirect only | Baiting trolls; speech recognition errors | Yes | Needs a talking streamer |
| 2. Tap on the Shoulder | Partial | Muted Notification (12.4k downloads), Remember to Talk (2.4k) | Yes, narrowly / Partly / Yes | Strong, anecdotal (problem) | "Monitor your own mic"; viewers do sometimes tell | Yes (own game for the fullscreen case) | Yes |
| 3. VAR | Partial | tomaae OBS instant replay (12.6k downloads, last update 2019); Streamer.bot replay actions | Partly / Partly / Yes | Indirect only | Replay interrupts the stream | Yes (own game built for close calls) | No: needs disputed moments |
| 4. Raid Torch | Partial | None well-known in the raid category | Partly / Yes / Yes | Indirect (raid trains are active) | Hate raids; raiders leave quickly | Partly (needs a second live channel) | Disputed |
| 6. Studio Audience | Partial | Sound Alerts, Meld Emote Storm, KappaGen, Streamer.bot walk-on sounds | Partly / Partly / Yes | Indirect (sound features widely used) | Sound spam and noise | Yes, but only 3 voices | Mostly; weaker where source audio matters |
| 8. Hint Jar | Partial | None well-known | Yes, narrowly / Partly / Yes | Strong (problem) | Rules and bans seen as enough; no-hint purists | Yes (own puzzle game) | No: blind or first playthroughs |
| 10. Checkpoint (pivoted) | Partial after pivot | StreamerQnA (9.5k downloads); Meld AMA queue (pre-pivot same loop) | One source (P): no tool listens to the streamer or replies after an answer | Moderate (problem) | Viewers may not wait | Yes | Partly: focus stretches |

---

## 1. Minefield

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

---

## 2. Tap on the Shoulder

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

---

## 3. VAR

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

---

## 4. Raid Torch

**Card in one line:** a torch travels between channels by raid; chatters add marks to it, and when it arrives, torch-bearers who chat in the new channel light up.

**Competitors**

| Name | What it does | Found by / status | Overlap | Well-known |
| --- | --- | --- | --- | --- |
| [R3dLabs Toolbox](https://r3dlabs.com/tools) | Raid-train scheduling and one-press raid to the next slot | A, G, C / confirmed | Partial–Adjacent | No counts (Elgato marketplace listing, v0.1.1.3, Dec 2024) |
| [RaidRunner](https://raidrunner.net/) | Raid-train sign-ups, slots, lineup API, Twitch extension | A, G, C / confirmed | Partial–Adjacent | No counts |
| [RaidPort](https://raidport.tv) | Streamers raid a hub channel and earn a wheel slice; chat votes; the wheel picks a live channel to raid. Beta | C (snippet) → L / verified | Adjacent | No |
| [Teams+](https://blog.twitch.tv/en/2019/10/31/highlights-from-the-twitchcon-hackathon-2019) (TwitchCon Hackathon 2019) | Trusted-viewer labels shared across a Team | C / verified | Adjacent | No |
| [Raid Train Central](https://raidtraincentral.carrd.co/), raid trains as a format | Organised themed trains | C, G / confirmed | Adjacent | No counts |
| WooferBot raid pose | Mascot and lights react to raids | G | Adjacent | No |
| Twitch Storm (2020 relay, ~200 streamers) | Organised 24 h relay | C / snippet | Adjacent | Claimed 156k viewers (unverified) |
| Native highlighting of arriving raiders | Users report Twitch marking raiders' messages | A / Reddit, unverified | Partial | Twitch |

Dropped: Raid Train (Devpost, unverifiable).

**Difference:** tools handle scheduling and the raid itself; none carries a visible object with per-chatter marks from channel to channel. A: "partly" (the difference rests on the shared object and its history); G and C: "yes".

**Demand**
- Raid trains are an active practice in October 2026: DJ, VTuber, artist and horror charity trains (G, X, unverified); [Raid Train Central](https://raidtraincentral.carrd.co/) active in 2026 (L / verified); RaidRunner's guide says picking the next raid becomes "a second job" (G).
- Raids count toward Partner status since Oct 2024 (C, snippet; page blocked).
- No request for a carried object or named raiders on arrival (A, G, C).

**Counter-signals**
- Hate raids made small streamers wary of raids ([PinkNews, 2021](https://thepinknews.com/2021/08/31/twitch-hate-raids-solution-rekitraven/), L / verified); a raid-blocker extension exists (C, snippet).
- Many raiders leave right away (A, Reddit, unverified; C, snippet).

**Audience fit:** any category that raids; in practice small and mid streamers in raid circles. Type-independent: G and C yes (needs a circle of channels), A no (needs an opted-in relay format). Natural-setting demo: G yes; A and C partly: a real raid between our own channels works, but a real multi-community relay cannot be shown with one streamer and three viewer accounts.

**Fact issues**
- `channel.raid` gives the two channels and a viewer count, **not** the list of raiders (A, G, C). The torch can only recognise people it already knows (torch-bearers with marks) when they chat in the new channel.
- Raids have a 90 s countdown and can be cancelled (C).

---

## 6. Studio Audience

**Card in one line:** chat reactions become a live studio-audience soundtrack: laughs, gasps and chants mixed from real, named viewers, never louder than the number of people actually reacting.

**Competitors**

| Name | What it does | Found by / status | Overlap | Well-known |
| --- | --- | --- | --- | --- |
| [Sound Alerts](https://soundalerts.com/) | Viewers trigger sounds with Bits or channel points | A, G, C / confirmed | Partial–Adjacent | Yes |
| [Meld Emote Storm](https://meldstudio.co/gallery/emote-storm/) | Emote storm that grows with chat activity; visual | A, G, C / confirmed | Partial | Yes (Meld) |
| [StreamElements KappaGen](https://docs.streamelements.com/chatbot/commands/default/kappagen) | Emote explosions on screen | A, G, C / confirmed | Partial–Adjacent | Yes (StreamElements) |
| [Streamer.bot Walkon Sounds](https://extensions.streamer.bot/t/walkon-sounds-aka-sub-sounds/77) | A personal entrance sound when a viewer first chats | A, G / confirmed | Partial | Yes (Streamer.bot) |
| [Blerp](https://blerp.com/streaming) walk-ons and soundboard | Viewer soundboard plus per-subscriber walk-on sounds | G / unverified (site blocked) | Partial | Likely |
| VoxBooster emote-laugh soundboard guide; Elgato "Popular Sounds" (sitcom laugh tracks); Crowd Sounds app | Laugh and crowd sounds fired by hand | C / verified | Adjacent | Elgato |
| Plus 2 (1 user), Chat Decoder hype meter | Visual chat-excitement gauges | C / verified | Adjacent | No |

Dropped: Twitch Sense (unverifiable).

**Difference:** chat-scaled visuals, viewer-triggered sounds and per-viewer entrance sounds all exist; G notes per-viewer sounds already cover "this noise belongs to that viewer". Not found: one mixed crowd whose loudness follows the number of distinct reactors, with recurring voices tied to named viewers and chants. A and G: "partly"; C: "yes". A re-search found nothing closer.

**Demand**
- Sound features are in wide, current use: streamers redoing sound alerts, chat-controlled alerts, custom alert commissions (G, X, unverified); a streamer added Sound Alerts after viewers asked (A, Reddit, unverified); requests for personal entrance sounds (A, Reddit, unverified).
- Streamers build emote-to-laugh soundboards by hand ([VoxBooster](https://voxbooster.com/blog/soundboard-meme-audios-twitch-chat-emotes/), L / verified).
- Streaming to a silent or lurking chat is demoralising ([Dexerto, 2018](https://www.dexerto.com/entertainment/emotional-streamer-rage-quits-his-broadcast-because-no-one-was-putting-anything-in-the-chat-141564/), L / verified).

**Counter-signals**
- Sound spam: a streamer asks to block one viewer who over-uses Sound Alerts ([feedback board, 2022, 7 votes](https://feedback.soundalerts.com/p/restrict-a-specific-user-from-using-sound-alerts), L / verified); "firing KEKW audio every time the emote appears turns a comedic tool into repetitive noise" (VoxBooster, verified); viewers list excessive sound effects among things they dislike (A, Reddit, unverified).
- G's X search for sound alerts described as annoying returned 0 posts.
- With 0–3 chatters the crowd stays tiny (C, inference).

**Audience fit:** talk, comedy and variety streams first (Just Chatting 14.2%, IRL 1.8%); usable on game streams with an active chat if the audio doesn't clash. Mostly type-independent. Natural-setting demo: A and G yes; C partly: three test accounts make at most three voices, so the scaling cannot be shown with real viewers.

**Fact issues:** none. Samples must be CC0 or self-recorded (no commercial audio).

---

## 8. Hint Jar

**Card in one line:** viewers drop tiered hints into a sealed jar instead of backseating in chat; the streamer opens one tier at a time on stream, only when stuck.

**Competitors**

| Name | What it does | Found by / status | Overlap | Well-known |
| --- | --- | --- | --- | --- |
| [LeagueBackseat](https://github.com/HerXayah/LeagueBackseat) | Viewers queue timestamped backseat messages for later | A, C / confirmed (G could not find it) | Partial | No (0 stars) |
| [Backseat Me](https://devpost.com/software/backseat-me) (Channel Points Hackathon 2021) | Channel points let a viewer temporarily control or talk to the streamer | A, G / confirmed | Adjacent–Partial | No |
| No-backseat rules, help safe words, `!backseat` | Manual practice: ask before hinting | A, G, C / confirmed | Partial | n/a |
| Channel-point "backseat" rewards | Temporary permission to backseat | A, G / confirmed | Partial | Twitch mechanism |
| evils_presley "backseating costs 5 dollars" | A paid backseat window in stream titles | G / verified | Adjacent | No |
| Universal Hint System (1988) | Offline tiered hints revealed in order | C / verified by search | Adjacent | No counts |
| [Chat Curtain](https://chromeboard.com/extension/chat-curtain-ofdmpokiehfdakmadncelpmnnhmbgabp) | Shows only mod-approved chat messages to extension users | C / verified | Adjacent | No (14 users) |

**Difference:** queued help and streamer permission exist; tiered hints exist offline. Not found: private submission, tiered sealed hints, streamer-controlled reveal one tier at a time. A: "yes, narrowly"; G: "partly"; C: "yes". The link check's search for tiered-hint Twitch tools found none.

**Demand**
- Backseating complaints: a Steam thread says constant backseating pushes people away from a game's streams ([Limbus Company, 2025](https://steamcommunity.com/app/1973530/discussions/0/597397269594002793), L / verified); many "no backseating / no spoilers" stream titles and rules (G, X, unverified); puzzle and blind-run discussions separating nudges from spoilers (A, Reddit, unverified); streamer outbursts at backseaters (C, snippets).
- A streamer guide describes the "gentle nudge when stuck" play style ([StreamHub, 2026](https://streamhub.world/streamer-blog/strategy/1199-how-to-handle-viewer-spoilers-and-backseating-on-stream/), L / verified). Correction: it does **not** say backseating is "one of the most frequent" problems.

**Counter-signals**
- Most replies in the Limbus thread say rules, timeouts and bans fix it (L / verified).
- Some viewers and streamers want no hints at all (A, C); some streamers invite backseating as content (G, X, unverified).

**Audience fit:** blind or first playthroughs of puzzle, adventure, horror and indie games (indie +51% YoY, horror +6%); no share data for blind runs. Natural-setting demo: Yes with an original Codex-built puzzle game (already in the card).

**Fact issues:** Twitch removed the "Blind Playthrough" tag in 2020; "First Playthrough" and "No Spoilers" are the current wording (C, snippet).

---

## 10. Checkpoint (pivoted)

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

---

## Eliminated after the evidence step (user decision, 2026-10-28)

README says evidence alone does not eliminate a card; the user chose to eliminate these three after reading the merged evidence.

| Card | Main reason in the evidence |
| --- | --- |
| Previously On | Twitch announced mid-stream AI summaries (May 2026) and relaunched Recaps (Oct 2026); all three researchers found the native summary. |
| Photo Booth | StreamUP Polaroid Picture (well-known, all three researchers) already does the viewer-triggered countdown Polaroid, including raid triggers; two of three rated the avatar version the same core loop. |
| Foley Pit | No demand found by any researcher; CLAP text-audio scores correlate poorly with human judgment (A, C). |
