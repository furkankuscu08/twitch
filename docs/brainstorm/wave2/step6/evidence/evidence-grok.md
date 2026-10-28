You’re connected to X as **@neolight11**. Here’s what I can do from here:

- **Your account**: your profile, home timeline, your posts, and mentions
- **Posts**: open any post from a link, and see who liked, reposted, or quoted it
- **Users**: look up any account by handle, search for users, and read their posts
- **Search**: search posts across X and count post volume on a topic
- **News & trends**: search X news stories and get trends by location
- **Spaces & communities**: search live or scheduled Spaces, see who’s hosting and what was shared, and look up communities
- **Lists**: read any list’s posts and members, and create, edit, follow, pin, and manage your own lists
- **Bookmarks**: list, add, and remove bookmarks, and organize them into folders
- **Chat**: read and reply to X Chat, see what’s unread, and go through message requests (needs your Chat PIN by secret-request, never pasted here)
- **Calls**: list the X calls on your calendar, schedule or change one, and RSVP
- **Livestreams**: your stream sources and broadcasts, schedule a broadcast, summarize a past stream’s chat, and manage moderators and mutes

Posting and going live right now aren’t supported.

Below is evidence only. No scores. Category shares are the figures supplied in the brief (research dated 2026-10-26). X posts are from a full-archive search; a search for people calling sound alerts annoying returned no posts.

---

## 1. Minefield

### A. Closest existing things

- **[obs-popup-overlay](https://github.com/erfur/obs-popup-overlay)** — Local speech recognition (Vosk) pops an image when the mic hits a configured hotword. **Overlap:** Partial. Listing: 0 stars, 1 fork, last push 2022-06-29.
- **[scpedicini/swearjar](https://github.com/scpedicini/swearjar)** — Browser speech recognition beeps on a fixed censored-word list. **Overlap:** Partial. The README says it fails outside strict Chrome.
- **[Kloot swear-jar overlay](https://kloot.gg/overlays/swear-jar-overlay)** — A counter the streamer or a mod presses; it does not listen. **Overlap:** Adjacent.
- **[1up.vision Bingo layers](https://docs.1up.vision/overlays/control-panels)** — A public bingo board mods can mark live. Vision’s own site names Papaplatte, Gronkh, and others as overlay users ([1up.vision](https://www.1up.vision/en)). **Overlap:** Adjacent. **[ByteMike Bingo](https://bytemike.de/en/stream-tools/bingo-overlay/)** is the same kind of public board. **Overlap:** Adjacent.
- **[Ok Gamers](https://devpost.com/software/ok-gamers)** (TwitchCon Hackathon 2019, grand prize) — Saying “Ok gamers…” starts a chat poll. **Overlap:** Partial (streamer speech triggers a show; targets are not secret viewer words).

A 2016 Reddit post describes a Chrome mic swear jar ([r/Twitch](https://www.reddit.com/r/Twitch/comments/5haf17/some_streamer_asked_how_to_implement_a_swear_jar/)). The party game Taboo and a shipped “if I say X” tool were **not found** as Twitch products.

### B. Claimed difference

**Yes.** Speech-to-overlay and public bingo exist. A game where viewers secretly plant the words, steer talk toward them, and get named on an automatic hit was not found.

### C. Demand signals

- Streamers run manual swear jars as charity bits: [@seapickle1322, 2026-10-07](https://x.com/seapickle1322/status/2107920494351827241), [@bribeecool10, 2026-09-30](https://x.com/bribeecool10/status/2105433177758298584), [@QBallNation, 2026-10-10](https://x.com/QBallNation/status/2108730361723433306).
- People ask others to make stream bingo sheets: [@KCyuri_lover, 2026-10-06](https://x.com/KCyuri_lover/status/2107577496598364322), [@JohnSmithihep, 2026-10-05](https://x.com/JohnSmithihep/status/2106986364978004224). Others post handmade cards: [@mintmosse, 2026-10-24](https://x.com/mintmosse/status/2113937292910072245).
- A streamer asked for an on-screen jar bumped by a command or a click, and replies pointed at Streamer.bot voice commands or a death counter ([r/SmallStreamers, 2025-09-03](https://www.reddit.com/r/SmallStreamers/comments/1n77vti/is_there_an_easy_way_to_have_an_onscreen_swear/)).

**Counter-signals:** Not found for a secret word-mine game. The same thread treats a chat-triggered counter as something mods should control, so chat cannot inflate it.

Posts asking for this secret-word game: **Not found.**

### D. Audience fit

Needs the streamer to talk. Closest supplied buckets: Just Chatting (14.2%) and IRL (1.8%). It can sit on a game stream only while the streamer is talking. Silent play does not run the loop.

**Natural-setting demo: Yes.** A desk conversation is the real setting, and it needs no commercial game.

**Type-independent:** No. Tied to talk.

### E. Fact problems

Not found. A titled 30-second clip matches Twitch’s Create Clip range (5–60 seconds, default 30, optional title in the open beta; the clip is of the live broadcast, about 85 seconds before the call and 5 after on the older guide): [Clips](https://dev.twitch.tv/docs/api/clips/), [beta note](https://discuss.dev.twitch.tv/t/introducing-clip-api-improvements-and-clip-from-vod-in-open-beta/64492).

---

## 2. Tap on the Shoulder

### A. Closest existing things

- **[Muted Notification](https://github.com/univrsal/muted-notification)** (OBS resource, [forum page](https://obsproject.com/forum/resources/muted-notification.1706/), posted 2023) — Plays a sound or shows a red mark if you talk while the mic source is muted. **Overlap:** Partial.
- **[StreamNotch mic guide](https://streamnotch.com/guides/obs-mic-muted-warning)** (updated 2026-10-19) — Alerts for muted, silent, or clipping mic, including “you’re talking while muted.” **Overlap:** Partial. **[ViperVex Mic Status](https://vipervex.com/products/mic-muted-widget-obs-live-microphone-status-overlay)** reads OBS WebSocket mute state and can show “MIC MUTED.” **Overlap:** Partial.
- **[Twitch Guardian](https://chromewebstore.google.com/detail/twitch-guardian/fcfdekecgocobpjhldifpplcifkfflme)** — Desktop alert when keywords appear in an open Twitch chat tab. [chrome-stats](https://chrome-stats.com/d/fcfdekecgocobpjhldifpplcifkfflme) listed 58 users as of 2026-10-17; version 1.00.02, last updated 2026-01-18. **Overlap:** Partial.
- **[Elgato Prompter chat mode](https://help.elgato.com/hc/en-us/articles/20461145372813-Elgato-Prompter-Chat-Mode)** (help article updated 2026-06-26) — Twitch chat on the prompter in front of the camera. **Overlap:** Partial. **[Mochi the Cat](https://marketplace.elgato.com/product/mochi-the-cat-6ac71734-f507-4887-8350-10357f6e6ea0)** is an Elgato Marketplace widget, version 1 dated 2022-09-05. The page does not describe chat behavior. **Overlap:** Adjacent, details unverified.
- **[WooferBot](https://wooferbot.com/)** — On-stream mascot; [docs](https://wooferbot.com/documentation.html) map follows, raids, subs, and bits to Philips Hue, Yeelight, and Nanoleaf. **Overlap:** Adjacent (lights on Twitch events, not production faults).

### B. Claimed difference

**Partly.** Mute detection, keyword pings, and chat-in-front-of-your-face already exist. A single loop that takes viewer reports and mod cues, agrees with OBS, puts a face in the camera shot, then asks chat to confirm the fix was not found.

### C. Demand signals

- A new streamer talked for two hours on a muted mic, including through a 15-person raid ([r/Twitch, 2020-03-27](https://www.reddit.com/r/Twitch/comments/fq7woy/today_i_streamed_for_2_hours_without_noticing_my/)). A reply says chat does call out a muted mic when there is a webcam.
- [@moistnoi, 2026-10-02](https://x.com/moistnoi/status/2105843201257140278): a streamer was raided, about 10 viewers tried to interact, and the screen stayed black.
- [@Creamsyckle, 2026-10-20](https://x.com/Creamsyckle/status/2112403403301376124): canceled a stream because Twitch showed a black screen.
- StreamNotch’s guide states the usual case: OBS shows the mute, and nobody is told if the mixer is behind a fullscreen window ([guide](https://streamnotch.com/guides/obs-mic-muted-warning)).

**Counter-signals:** On the Reddit thread, one reply says to monitor your own mic in OBS instead of waiting for chat. Another says active chatters sometimes never mention a BRB screen.

### D. Audience fit

Any live show with a mic and scenes. That is most of Twitch, including Just Chatting (14.2%) and the game categories that fill the rest of the top 15. The “you can’t see chat because the game is fullscreen” case is the game majority. The desk face itself is an IRL/camera bit (IRL is 1.8%).

**Natural-setting demo: Partly.** Mute, black scene, and the desk face can be shown with no game. The fullscreen-game case cannot be shown with a commercial game.

**Type-independent:** Yes, for any broadcast with a mic.

### E. Fact problems

Not found.

---

## 3. VAR

### A. Closest existing things

- **[obs-instant-replay](https://github.com/tomaae/obs-instant-replay)** — Picture-in-picture of the OBS replay buffer, with an optional `!replay` chat command. A repository listing reported 42 stars and 9 forks, created 2018-12-24. A later fetch of the same URL did not show a star count. **Overlap:** Partial.
- **[Streamer.bot: Set Replay Buffer State](https://docs.streamer.bot/api/sub-actions/obs-studio/replay/set-replay-buffer-state)** — Start, stop, or save the OBS replay buffer from an action, which can be a chat command. **Overlap:** Partial.
- **[RTS Action Replay](https://x.com/DuhBuhHuh/status/2104466216555340065)** (post 2026-09-28) — The post says it manages clips from the OBS replay buffer, Twitch, YouTube, and Kick and plays them as a replay. The product page behind the short link was not opened. **Overlap:** Partial.
- **[Senchabot chat poll](https://extensions.senchabot.com/setup/chat-poll)** — Mods start a poll from chat; each viewer votes once; bars fill on stream. Streamer.bot’s site says it can run Twitch polls and predictions ([streamer.bot](https://streamer.bot/)). **Overlap:** Partial.
- **[Ok Gamers](https://devpost.com/software/ok-gamers)** — Speech starts a vote and shows a chart. **Overlap:** Adjacent.

A slow-motion jury, verdict stamp, and titled “VAR” clip as one ritual: **Not found.**

### B. Claimed difference

**Partly.** Replay-on-command and a chat poll are both shipping. The claimed difference is the combined broadcast ritual, and that combination was not found. Each half is common.

### C. Demand signals

- Streamers are told to use the OBS replay buffer plus a Stream Deck or a marker instead of rewatching the VOD: [@avengerUNKNOWN1, 2026-10-20](https://x.com/avengerUNKNOWN1/status/2112425245575664111), [@ClipStudiohq, 2026-10-19](https://x.com/ClipStudiohq/status/2112317980919079106), [@DaiShimaVT, 2026-10-27](https://x.com/DaiShimaVT/status/2114921683668931057).
- The obs-instant-replay README exists specifically so viewers can trigger replay with a chat command ([repo](https://github.com/tomaae/obs-instant-replay)).

Posts asking for a chat jury or a VAR verdict: **Not found.**

**Counter-signals:** Not found.

### D. Audience fit

Needs a moment people can dispute. That is the game categories (League 8.6%, Minecraft 4.5%, GTA V 3.9%, CS 3.2%, and the rest of the top 15) and Sports (#29; no share figure in the brief). Just Chatting can stage a dispute; it is not the usual setting.

**Natural-setting demo: Partly.** A desk contest can show call, replay, vote, and stamp. A real match in a top game cannot be shown.

**Type-independent:** No. Tied to arguable moments.

### E. Fact problems

Not a false claim, with a limit. Create Clip captures the live broadcast, not the replay-buffer file. Duration in the beta is 5–60 seconds, so a 60-second clip is the maximum, and the older guide describes a roughly 90-second window around the API call ([Clips](https://dev.twitch.tv/docs/api/clips/), [beta](https://discuss.dev.twitch.tv/t/introducing-clip-api-improvements-and-clip-from-vod-in-open-beta/64492)). A clip of the review works if that review is what is on the live output inside that window.

---

## 4. Raid Torch

### A. Closest existing things

- **[R3dLabs Toolbox](https://r3dlabs.com/tools/stream-deck)** — One Stream Deck key raids the next person on an R3dLabs train. Marketplace version 0.1.1.3 is dated 2024-12-18 ([listing](https://marketplace.elgato.com/product/r3dlabs-toolbox-ad81dbc6-0b57-4ef3-a5bb-c210dbd4ee1c)). The same site also lists FirePanel, R3ddyBot, and a schedule panel ([tools](https://r3dlabs.com/tools)). **Overlap:** Partial.
- **[RaidRunner](https://raidrunner.net/)** — Sign-ups, slots, waitlist, trades, reminders, a lineup API for overlays, and a Twitch extension for upcoming trains. A 2026 host guide is on the site ([guide](https://raidrunner.net/info/how-to-host-a-raid-train)). **Overlap:** Partial.
- **Raid trains as a weekly format** — DJs, VTubers, artists, and horror charity trains were being promoted in October 2026 (posts under C). **Overlap:** Adjacent. The train is the journey; nothing in these posts is a carried object.
- **WooferBot raid pose** — A mascot and lights react when a raid happens ([docs](https://wooferbot.com/documentation.html)). **Overlap:** Adjacent.
- **EventSub `channel.raid`** — Official, version 1, no auth. Payload is the two broadcasters and a viewer count, not a list of raiders ([docs](https://dev.twitch.tv/docs/eventsub/eventsub-subscription-types/)). **Overlap:** Partial (the handoff signal only).

### B. Claimed difference

**Yes.** Scheduling and one-press raids are a live product category. A torch that accumulates per-chatter marks, flies in with a journey, and lights individual raiders when they speak in the next channel was not found.

### C. Demand signals

- Organizers publicly recruit trains: [@Househeadspeakz, 2026-10-04](https://x.com/Househeadspeakz/status/2106695053393465692) (DJ train), [@rosiemallowvt, 2026-10-08](https://x.com/rosiemallowvt/status/2108244326975418408) (second-year VTuber train, 7 reposts), [@TheCryptTeam, 2026-10-21](https://x.com/TheCryptTeam/status/2112934655834161232) (40+ horror charity streamers), [@becca_mtbc, 2026-10-23](https://x.com/becca_mtbc/status/2113661185912693031) (artists and makers), [@Tequila_DJ, 2026-10-06](https://x.com/Tequila_DJ/status/2107561803441918293) (“brand new raid train concept”).
- RaidRunner’s own guide says that past a few streamers, “who do I raid?” becomes a second job ([guide](https://raidrunner.net/info/how-to-host-a-raid-train)).

Posts asking for carried state or named raiders on arrival: **Not found.**

**Counter-signals:** Not found.

### D. Audience fit

Raids are not a category. October posts show trains in DJs (#41), Art (#40), horror (brief: +6% YoY), and VTubers inside larger buckets. Any channel that raids can hold the torch. Just Chatting is 14.2% and is a common raid home; games are the rest of the top 15.

**Natural-setting demo: Yes.** Three test accounts can raid each other on desk or IRL streams. No game required.

**Type-independent:** Yes, for any channel that raids.

### E. Fact problems

Not a contradiction. `channel.raid` does not name the viewers in the raid, only `viewers` ([payload](https://dev.twitch.tv/docs/eventsub/eventsub-subscription-types/)). The card’s “glows when they first chat” path does not require that list. The card’s note that third-party emotes will not render as images matches Twitch chat carrying only native emotes; a separate 7TV/BTTV doc was not opened.

---

## 5. Previously On

### A. Closest existing things

- **Twitch video chapters** — Changing category while live creates a chapter viewers can skip to. They cannot be edited after ([VOD help](https://help.twitch.tv/s/article/video-on-demand)). **Overlap:** Partial (automatic beats, not a newcomer bumper).
- **Twitch mid-stream AI summary** — A BetterTTV pull request (2026-07) describes an AI “Mid-Stream Summary” callout for people who join late, and a setting to hide it. A comment says it is opt-out and surprised large streamers ([PR #8092](https://github.com/night/betterttv/pull/8092)). **Overlap:** Partial.
- **[CatchUp.help](https://catchup.help/twitch)** — Viewers type `!recap` and get an AI summary of the stream so far, from chat plus transcribed audio. **Overlap:** Partial. The page says raid handling pauses when you leave your own channel.
- **Pin Chat Message** — Twitch changelog: pinned-chat endpoints entered open beta 2026-05-15 and general availability 2026-05-29. Send Chat Message gained a `pin` parameter ([changelog](https://dev.twitch.tv/docs/change-log/)). **Overlap:** Partial (the pin, not the recap).
- **Get Stream Markers** — Documented. Creating a marker requires the channel to be live and past-broadcast storage to be on. With no VOD, Get returns 404 ([markers](https://dev.twitch.tv/docs/api/markers/)). **Overlap:** Partial.

Raid alerts that only greet the raider, and hand-written `!lore` commands: the pattern is described by the card; a specific product page for `!lore` was **not found**.

### B. Claimed difference

**Partly.** Late-join briefings already exist, and Twitch is shipping an AI one. A human-curated TV bumper, triggered by a raid, with no AI summary, was not found. The “no AI” half is what still separates it.

### C. Demand signals

- Viewers say they missed the stream: [@carstairsfox, 2026-10-25](https://x.com/carstairsfox/status/2114458195724738705) (“WHAT DID I MISS ON ASHS STREAM”), [@quadbunni, 2026-10-24](https://x.com/quadbunni/status/2113956464154816769), [@Liskonder, 2026-10-24](https://x.com/Liskonder/status/2114016497488068804), [@capoyaoi, 2026-10-24](https://x.com/capoyaoi/status/2114001905093333441).
- A streamer wanted a “previously on” video before the next game and had lost the VODs ([@SpectreRobin, 2026-10-20](https://x.com/SpectreRobin/status/2112355909804380394)).
- CatchUp selling `!recap` is a product-shaped demand signal ([site](https://catchup.help/twitch)).

**Counter-signals:** The BetterTTV PR exists to hide Twitch’s AI summary, and a commenter says viewers and streamers were surprised it turned on ([PR](https://github.com/night/betterttv/pull/8092)). That is dislike of an automatic summary, not of a human bumper.

### D. Audience fit

Any stream long enough to need a catch-up, plus any incoming raid. That covers Just Chatting (14.2%) and the game categories. No separate share for “people who arrive late.”

**Natural-setting demo: Yes.** Markers, a test raid, and `!recap` can all happen on a desk stream.

**Type-independent:** Yes.

### E. Fact problems

The pin endpoint claim holds ([changelog, 2026-05-29](https://dev.twitch.tv/docs/change-log/)). A pin duration of 10 minutes fits the client-documented `duration_seconds` range of 30–1800 ([twitch_api pin source](https://twitch-rs.github.io/twitch_api/src/twitch_api/helix/endpoints/chat/pin_chat_message.rs.html)); the official reference page was not opened line by line.

Constraint, not a false sentence: markers are not created, and Get Stream Markers 404s, unless past broadcasts are stored ([markers](https://dev.twitch.tv/docs/api/markers/)). The card’s “read markers every 30 s” path depends on that.

---

## 6. Studio Audience

### A. Closest existing things

- **[Sound Alerts](https://soundalerts.com/twitch-extension)** — Viewers play sounds, video, and TTS in the stream, with or without Bits. Channel Points are supported ([channel points](https://support.soundalerts.com/article/channel-points)). No user total was on the pages opened. **Overlap:** Partial.
- **[Blerp](https://blerp.com/streaming)** — A large viewer soundboard, plus per-subscriber WalkOn sounds ([walk-ons](https://blerp.com/twitch-walkon)). The FAQ has a section on stopping spam. **Overlap:** Partial.
- **[Streamer.bot walk-on sounds](https://extensions.streamer.bot/t/walkon-sounds-aka-sub-sounds/77)** (extension post, 2023-06-28) — A folder per username plays when they first speak. A starter-pack sample does the same ([docs](https://docs.streamer.bot/examples/starter-pack)). **Overlap:** Partial.
- **[Meld Emote Storm](https://meldstudio.co/gallery/emote-storm/)** — Emotes fall and pile up; “the more emotes chat sends, the bigger the storm.” Visual, not audio. **Overlap:** Partial.
- **[StreamElements KappaGen](https://support.streamelements.com/hc/en-us/articles/10474578102802-How-to-Set-Up-Emote-Explosion-Widget-KappaGen)** — Chat emotes and `!kappagen` explosions on screen. **Overlap:** Adjacent.

A mixed crowd whose volume follows the count of distinct people, with a signature laugh per user id: **Not found.**

### B. Claimed difference

**Partly.** Named sounds and visual scaling are normal. A single mixed crowd that cannot get louder than the number of real reactors, plus chants, was not found. Per-user sounds already mean “this noise belongs to that viewer,” which is half of the claim.

### C. Demand signals

- [@ghostkittenxx, 2026-10-26](https://x.com/ghostkittenxx/status/2114836246057095518) (about 129k followers): redoing all Twitch sound alerts and asking for recommendations, names Blerp.
- [@uppuzbear, 2026-10-22](https://x.com/uppuzbear/status/2113341219489353986): watching a streamer whose chat controls sound alerts.
- [@HyoumaKohaku, 2026-10-08](https://x.com/HyoumaKohaku/status/2108272023562596825): swapping donation sounds for jump scares all month.
- [@ItsLethalTTV, 2026-10-14](https://x.com/ItsLethalTTV/status/2110437986412507605): “Do you have sound alerts on stream?”
- Custom alert commissions are being sold to VTubers: [@musicbyaluna, 2026-10-22](https://x.com/musicbyaluna/status/2113282400927248806), [@OdetteAewryn, 2026-10-10](https://x.com/OdetteAewryn/status/2108841773573570982).

**Counter-signals:** An X search for sound alerts or Blerp described as annoying, spam, or too loud returned **0 posts**. Blerp’s own FAQ still treats spam as something the streamer must cap ([streaming FAQ](https://blerp.com/streaming)).

### D. Audience fit

Any chat that reacts with emotes or words. Strongest in Just Chatting (14.2%) and IRL (1.8%), and usable on game streams, which are most of viewing. Art and Music have many small channels (about 17 and 14 viewers per live channel).

**Natural-setting demo: Yes.** A desk bit that makes three test accounts laugh, gasp, and chant needs no game and no copyrighted music if the samples are CC0.

**Type-independent:** Yes.

### E. Fact problems

Not found.

---

## 7. Foley Pit

### A. Closest existing things

- **[Sound Alerts channel points](https://support.soundalerts.com/article/channel-points)** — Viewers redeem points and a pre-made sound plays. The streamer does not perform it. **Overlap:** Adjacent.
- **[Manao channel-point soundboard](https://manao.otternoon.com/en/guides/linking-channel-points-to-soundboard/)** — A reward plays a chosen audio file through an OBS overlay. **Overlap:** Adjacent.
- **Whose Line “Sound Effects”** — Audience members make the noises while performers act. Episode logs: [Salute to Whose Line](https://salutetowhoseline.wordpress.com/tag/sound-effects/). **Overlap:** Partial (the format, not a stream tool or a model score).
- **Blerp / Sound Alerts libraries** — Viewers pick from a catalog rather than writing a three-beat score ([Blerp](https://blerp.com/streaming)). **Overlap:** Adjacent.

A model that scores a spoon against the cue “footsteps,” then titles a foley reel: **Not found.**

### B. Claimed difference

**Yes.** Playback boards and the improv-show format exist. Audience-written score, live desk performance, and an automatic likeness score were not found together.

### C. Demand signals

Posts asking streamers to perform viewer-written foley, or for a model to judge it: **Not found.**

Nearby signals are people treating viewer-triggered sounds as a normal part of the stream (card 6 posts) and ASMR-style channels using sound as the content. A SmallStreamers post about an ASMR reading wanted a mistake counter, not performed foley ([thread](https://www.reddit.com/r/SmallStreamers/comments/1n77vti/is_there_an_easy_way_to_have_an_onscreen_swear/)).

**Counter-signals:** Not found.

### D. Audience fit

This is its own desk show. It fits inside Just Chatting (14.2%), IRL (1.8%), or Art (#40, about 17 viewers per live channel). It is not a layer on a normal game stream. No supplied share for “improv” or “foley.”

**Natural-setting demo: Yes.** The natural setting is a desk, a cup, and a spoon.

**Type-independent:** No. Tied to a performed bit.

### E. Fact problems

Not found.

---

## 8. Hint Jar

### A. Closest existing things

- **No-backseat / no-spoiler rules** — Used as the title of the stream, not a tool. Examples under C. **Overlap:** Partial (same problem, social rule instead of a jar).
- **Paid backseat window** — evils_presley’s titles say “NO SPOILING” and “backseating costs 5 dollars,” with `!backseat` ([TwitchMetrics channel page](https://www.twitchmetrics.net/c/750260872-evils_presley), titles dated through 2026-10-17). **Overlap:** Partial.
- **[Backseat Me](https://devpost.com/software/backseat-me)** — Twitch Channel Points hackathon entry. Spending points lets a viewer drive an on-screen character and talk to the streamer. The Devpost gallery blurb is “Because we all hate unwanted backseat” ([gallery](https://twitchchannelpoints.devpost.com/project-gallery?page=2)). **Overlap:** Partial.
- **LeagueBackseat** — [coder.social/herxayah](https://coder.social/herxayah) describes a repo as “a TwitchBot that allows viewers to Backseat the streamer.” The repository page itself was **not found**. A mod list dated the bot 2023-05-14 with 0 followers ([moddex](https://moddex.tv/channel/herxayah)). The card’s “queues messages” claim is **unverified**.
- **Channel Points custom rewards** — Official guide: streamers fulfill their own rewards, with a cooldown from 1 minute to 7 days ([help](https://help.twitch.tv/s/article/channel-points-guide)). A page that is specifically a shipped “backseat allowed for 1 minute” reward was **not found**. The mechanism to make one is documented.

### B. Claimed difference

**Partly.** Gating help (rules, a paid window, a points redemption) is already a practice. A private page of tiered sealed hints, opened one tier at a time as a show, was not found. LeagueBackseat could not be checked.

### C. Demand signals

- [@lilmochis, 2026-10-07](https://x.com/lilmochis/status/2107972459710578953): “is it so hard to stop backseating and just let the streamer stream.”
- [@Gutigwolfe, 2026-10-25](https://x.com/Gutigwolfe/status/2114289599824736664): a no-backseat rule, a polite warning, then a timeout.
- Blind runs advertised with “no spoilers”: [@D_rag_J, 2026-10-22](https://x.com/D_rag_J/status/2113401880072081584), [@SkinnyDoom, 2026-10-19](https://x.com/SkinnyDoom/status/2112295610036404595), [@thatblindman13, 2026-10-17](https://x.com/thatblindman13/status/2111605516455559619), [@offbeatslang, 2026-10-06](https://x.com/offbeatslang/status/2107458074143555929).
- [@rialVT, 2026-10-24](https://x.com/rialVT/status/2113881789500686778): a joke image about backseaters ignoring “NO HELP NO SPOILERS.”
- Chat rules written out as “No backseating” ([@DigitalDipper, 2026-10-04](https://x.com/DigitalDipper/status/2106670074547548420)).

**Counter-signals:** Some streamers invite it. [@Makarts2, 2026-10-19](https://x.com/Makarts2/status/2111998045378212185): “backseat gaming is cool just don’t be an ass.” [@Lilithra_Vtuber, 2026-10-09](https://x.com/Lilithra_Vtuber/status/2108657195000996012): puzzle-chat backseating “is going to be absolute gold.” [@MONDAYMCCLELLAN, 2026-10-08](https://x.com/MONDAYMCCLELLAN/status/2108137647554080781) advertised a backseat-gaming stream.

### D. Audience fit

Blind playthroughs and puzzle games. The brief says no usable share was found for blind playthroughs. The nearest figures are “almost all of the top 15 is games” and indie games +51% YoY. Just Chatting is a weak fit unless the puzzle is the show.

**Natural-setting demo: Partly.** An original puzzle can show the jar without a commercial game. A typical blind run of a known game cannot be shown.

**Type-independent:** No. Tied to blind or puzzle play.

### E. Fact problems

Not found. LeagueBackseat’s queue behavior could not be checked, so that competitor line is unverified rather than contradicted.

---

## 9. Photo Booth

### A. Closest existing things

- **[StreamUP Polaroid Picture](https://streamup.tips/product/polaroid-picture)** — Channel points (or a chat message, raid, sub, and other triggers) take a Polaroid of an OBS source, 3-second countdown, viewer text on the photo, optional save and Discord post. Version 3.0.3, “last updated: 10 September 2026.” Setup notes: [GitHub instructions](https://github.com/StreamUPTips/ReadMe-Files/blob/main/Product%20Instructions/FX-Polaroid%20Picture.md). The photo is of the streamer, not of the viewer beside them. **Overlap:** Partial, close to the same snap.
- **[einfloh/polaroid-obs-plugin](https://github.com/einfloh/polaroid-obs-plugin)** — A free fork of that idea: develop animation, flash, Discord upload. The README says it was inspired by the StreamUP plugin. **Overlap:** Partial.
- **Physical and digital sub printers** — [Nutty’s Printerbot video](https://youtu.be/hzOaKttqUNw) prints a receipt with name and profile picture. [MrJordilicious digital sub printer](https://www.mrjordilicious.com/streamer-resources/digital-sub-printer/) does a digital receipt with the profile picture. [Poweroverlay alert printer](https://poweroverlay.io/features/alert-printer) prints subs, follows, and raids. **Overlap:** Adjacent (avatar on a slip, not a posed photo).
- **[Senchabot end credits](https://extensions.senchabot.com/setup/chat-poll)** — “Movie-style credits for everyone who subbed, cheered, raided and chatted.” **Overlap:** Adjacent to the closing collage.
- **[Twitch Receipt](https://receipt.craftingchaosgaming.com/)** — Includes a “Polaroid Stamp” receipt design and an avatar option. **Overlap:** Adjacent.

A composite of the viewer’s avatar in frame with the streamer, plus a raid group photo: **Not found.**

### B. Claimed difference

**Yes.** The snap-a-Polaroid-of-the-streamer loop is a current StreamUP product. Putting the viewer in the photo, making the raid a group photo, and ending on a corkboard of everyone who snapped were not found.

### C. Demand signals

Posts asking to appear in a photo with the streamer: **Not found.**

Nearby: StreamUP’s product page sells the snap as “viewers spend points to take a photo of you, with their message printed underneath” ([product](https://streamup.tips/product/polaroid-picture)). The printer video’s pitch is that a physical slip gives viewers something to stay for ([YouTube](https://youtu.be/hzOaKttqUNw)). X posts about “photo booth” in this period were a Melbourne Twitch party and an in-person booth, not software: [@TwitchMelbourne, 2026-10-03](https://x.com/TwitchMelbourne/status/2106318110139597179).

**Counter-signals:** Not found.

### D. Audience fit

Any stream with a camera. Strongest on Just Chatting (14.2%) and IRL (1.8%), where the streamer is in frame. Game streams can still snap a booth scene. Art is a weaker camera format (about 17 viewers per channel).

**Natural-setting demo: Yes.** `!snap`, a raid group photo, and a corkboard can be done with test accounts at a desk.

**Type-independent:** Yes, wherever there is a camera shot.

### E. Fact problems

Not found.

---

## 10. Checkpoint

### A. Closest existing things

- **[StreamerQnA](https://github.com/chinzistor/StreamerQnA)** — Local bot. Configured commands add questions to a queue; the streamer shows them one by one. OBS resource page: [forum](https://obsproject.com/forum/resources/streamerqna.1977/). A search listing reported 2 stars; the repo was created 2024-07-01; release 1.0.3 is dated 17 Sep on the [releases page](https://github.com/chinzistor/StreamerQnA/releases). It calls itself an alternative to Featured.chat. Featured.chat’s own site was not opened. **Overlap:** Partial.
- **[Meld X AMA Question Queue](https://meldstudio.co/gallery/x-ama-question-queue/)** — Messages that end in `?`, or `!ask`, collect in an on-screen queue. Clicking one brings it to the top. Twitch, YouTube, Kick, TikTok. **Overlap:** Partial.
- **[Meld Chat Highlight](https://meldstudio.co/docs/widget/)** — “Spotlight important chat messages right on screen” so they are not lost in a busy chat. **Overlap:** Partial.
- **[Social Stream Ninja featured chat](https://socialstream.ninja/docs/dock-live-guide.html)** — Operator clicks a message in a dock; that message is what the overlay shows. **Overlap:** Partial.
- **[Senchabot Featured Message](https://extensions.senchabot.com/setup/chat-poll)** — Puts one viewer message or question on screen. **[AskMeLive](https://x.com/Leo_of_Pune/status/2112787956247494726)** (post 2026-10-21) sells a paid-question queue plus OBS overlay. **Overlap:** Adjacent.

Chatterino highlights were named on the card. A page describing that feature was **not opened** in this pass, so it stays unverified.

Context thumbnails and an in-thread “answered on stream” ping: **Not found.**

### B. Claimed difference

**Partly.** Queues and featured messages already solve “don’t lose this chat line,” usually with a command, a question mark, or a click. Saving every ordinary message during a focus window, with a screenshot of that moment and a reply ping, was not found.

### C. Demand signals

- [@Leo_of_Pune, 2026-10-21](https://x.com/Leo_of_Pune/status/2112787956247494726): “Stop losing questions in chaotic live chat,” with a queue product.
- [@TrevorTreefort, 2026-10-22](https://x.com/TrevorTreefort/status/2113287225891062223): “The Duality of Being a Streamer when Reading Chat Messages.”
- Meld’s AMA page says a fast chat scroll is the thing the queue replaces ([Meld](https://meldstudio.co/gallery/x-ama-question-queue/)).
- StreamerQnA’s pitch is the same job: show submitted questions one by one ([repo](https://github.com/chinzistor/StreamerQnA)).

Posts about missing ordinary (non-question) chat while drawing or coding: **Not found** in this pass. Several “reading chat” posts were driving-safety arguments, not a tool request.

**Counter-signals:** Not found against answering saved messages. Driving-and-reading posts are a different objection ([@DefaltEVM, 2026-10-22](https://x.com/DefaltEVM/status/2113360617168130470)).

### D. Audience fit

Any heads-down stretch. The card’s own example is drawing (“inking the eyes”), which sits in Art (#40, about 17 viewers per live channel). Software & Game Development is described as far lower. The large case is games, where the streamer cannot watch chat: that is most of the top 15.

**Natural-setting demo: Yes** for drawing or other desk work. **Partly** if the natural setting is a commercial game, which the video cannot show.

**Type-independent:** Partly. The focus window can be used on any stream; the clearest setting is heads-down work.

### E. Fact problems

Not found. OBS WebSocket screenshot and a chat reply were not checked against a doc in this pass, so they are unverified rather than contradicted.

---

## Summary

| Card | Closest thing (link) | Overlap | Difference survives | Demand signals found | Counter-signals | Natural-setting demo | Type-independent |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1. Minefield | [obs-popup-overlay](https://github.com/erfur/obs-popup-overlay) | Partial | Yes | Yes (swear jars, bingo sheets) | Not found | Yes | No |
| 2. Tap on the Shoulder | [Muted Notification](https://github.com/univrsal/muted-notification) | Partial | Partly | Yes (muted-mic raid story, black screen) | Yes (monitor your own mic) | Partly | Yes |
| 3. VAR | [obs-instant-replay](https://github.com/tomaae/obs-instant-replay) | Partial | Partly | Yes (replay-buffer workflow) | Not found | Partly | No |
| 4. Raid Torch | [RaidRunner](https://raidrunner.net/) | Partial | Yes | Yes (October raid trains) | Not found | Yes | Yes |
| 5. Previously On | [CatchUp !recap](https://catchup.help/twitch) | Partial | Partly | Yes (“what did I miss”) | Yes (hide Twitch’s AI summary) | Yes | Yes |
| 6. Studio Audience | [Sound Alerts](https://soundalerts.com/twitch-extension) | Partial | Partly | Yes (alerts in active use) | Not found on X | Yes | Yes |
| 7. Foley Pit | [Whose Line sound effects](https://salutetowhoseline.wordpress.com/tag/sound-effects/) | Partial | Yes | Not found | Not found | Yes | No |
| 8. Hint Jar | [Backseat Me](https://devpost.com/software/backseat-me) | Partial | Partly | Yes (no-backseat / no-spoiler posts) | Yes (some streams invite it) | Partly | No |
| 9. Photo Booth | [StreamUP Polaroid](https://streamup.tips/product/polaroid-picture) | Partial | Yes | Not found for viewer-in-frame | Not found | Yes | Yes |
| 10. Checkpoint | [Meld AMA queue](https://meldstudio.co/gallery/x-ama-question-queue/) | Partial | Partly | Yes (don’t lose questions) | Not found | Yes for desk work; Partly for games | Partly |