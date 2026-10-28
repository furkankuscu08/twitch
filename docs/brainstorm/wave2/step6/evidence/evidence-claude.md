# Evidence report: 10 idea cards (researcher: Claude)

Date of research: 2026-10-28. Method: web search plus opening pages. Items marked **(snippet)** were seen only in search-result text and not opened, or the page refused the fetch (403). Everything else was opened and checked. Stream-type shares come from the stream-type data in the brief. I did not add percentages the brief does not give.

---

## 1. Minefield

### A. Closest existing things
| # | Name and link | What it does | Overlap | Activity / popularity |
|---|---|---|---|---|
| 1 | **OK Gamers** (TwitchCon Hackathon 2019 grand prize): https://github.com/twitchcon/ok-gamers-frontend · https://blog.twitch.tv/en/2019/10/31/highlights-from-the-twitchcon-hackathon-2019 | The streamer says "Ok gamers" plus a question. Azure speech-to-text parses it and starts a chat poll. | Partial (live streamer speech-to-text starts an on-stream event) | Archived May 2020, 3 stars. Won the grand prize in 2019. |
| 2 | **Streamer.bot Voice Control**: https://docs.streamer.bot/guide/voice-control | Windows speech recognition fires actions on spoken phrases. "Anywhere" mode matches mid-sentence. | Partial (automatic spoken-word trigger; the streamer sets the phrases, not viewers) | Part of a widely used free tool. The docs do not say whether phrases can be added while live. |
| 3 | **AnkhbotSecretWord** (Streamlabs Chatbot script) by Yaz12321: https://www.github.com/Yaz12321 **(snippet)** | The streamer picks a secret word. The first viewer to type it in chat wins. | Adjacent (secret word, but the roles are reversed and it runs in chat, not speech) | Old Ankhbot-era script. |
| 4 | **Wordeous** (Steam): https://store.steampowered.com/app/1507150/ | A Taboo-style game. The streamer describes a word without using banned words while Twitch chat guesses. | Adjacent (forbidden-word talk game) | Released Aug 2022, 19 reviews (89% positive). |
| 5 | **1up.vision Bingo layer**: https://docs.1up.vision/bingo **(snippet)** | A bingo-grid overlay. The streamer or mods click squares to mark them. | Adjacent (catchphrase-bingo bit, marked by hand) | Commercial overlay. Multi-layer overlays need a paid tier. |

Also relevant: **LocalVocal**, an OBS plugin that runs local Whisper captions with word filter/replace and output to a file (https://github.com/locaal-ai/obs-localvocal, ~1.7k stars). It is a ready-made local speech-to-text building block, but it has no word-trigger game. **Nightbot counters** (https://docs.nightbot.tv/variables/count, snippet) are how communities count streamer catchphrases by hand today.

### B. Claimed difference
**Yes.** I found nothing where viewers secretly choose the words and the streamer's live speech triggers them. Every speech trigger I found uses words the streamer chose (Streamer.bot, OK Gamers). Every viewer-chosen secret-word game runs in chat (AnkhbotSecretWord), and bingo is marked by hand.

### C. Demand signals
- Indirect: communities track streamer catchphrases by hand with counter commands that mods run. The Nightbot `$(count)` variable exists for this (https://docs.nightbot.tv/variables/count, snippet). This is not a request for Minefield itself.
- Indirect: the streamer Taboo game Wordeous exists and has a small user base (19 Steam reviews): https://store.steampowered.com/app/1507150/
- No direct request ("I wish viewers could plant words…") found: **Not found.**
- **Counter-signal:** trolls already try to make streamers say things on air, for example by baiting through donation messages (https://www.dexerto.com/entertainment/korean-irl-streamers-baited-lewd-donation-prank-1045134/, snippet). Guides warn that baiting can get a streamer suspended (https://www.streamscheme.com/what-you-cant-say-on-twitch/, snippet). A tool that rewards steering the streamer into saying a word may need strong word filters. The card already plans a blocklist.

### D. Audience fit
- **Works in:** any stream where the streamer talks a lot. That is mainly Just Chatting (14.2%), IRL (1.8%), Talk Shows & Podcasts and Sports, plus talkative facecam game streams. As specified (`base.en`/`small.en`), it is English-only.
- **Share:** Just Chatting plus IRL alone is about 16%. Talkative game streams would add more, but the data does not measure that.
- **Natural-setting demo:** **Yes.** Desk talk is Just Chatting, the #1 category, so the demo shows it in its real setting.
- **Type-independent?** Mostly. It works on any stream where the streamer talks, but it depends on the speech language and on how much the streamer talks.

### E. Fact problems
None found. faster-whisper's `transcribe()` does accept a `hotwords` parameter ("Hotwords/hint phrases to the model. Has no effect if prefix is not None."): https://github.com/SYSTRAN/faster-whisper/blob/master/faster_whisper/transcribe.py. The Twitch Create Clip endpoint accepts optional `title` and `duration` (5–60 s, default 30), so a "titled 30 s clip" is supported: https://dev.twitch.tv/docs/api/reference/ (Create Clip) and https://dev.twitch.tv/docs/change-log/ (2025-12-19). Stream markers need VOD storage enabled (see card 5 E).

---

## 2. Tap on the Shoulder

### A. Closest existing things
| # | Name and link | What it does | Overlap | Activity / popularity |
|---|---|---|---|---|
| 1 | **Audio Source Mute Indicator** (OBS Lua script): https://obsproject.com/forum/resources/audio-waves-visualizer.2247/ | Plays a tone and shows an overlay when a source is muted or unmuted. The overlay can be hidden from display capture. | Partial (covers the OBS-mute part only) | Released Oct 30, 2025. 4,558 views. The author calls it a work in progress. |
| 2 | **Remember to Talk** (OBS plugin): https://obsproject.com/forum/resources/remember-to-talk.2484/ | Plays a private, monitor-only alert when the mic has been silent too long while live. | Partial (silent-mic detection, private chime) | May 5, 2026. 2,446 downloads, no ratings. |
| 3 | **Twitch Guardian** (Chrome extension): https://chromewebstore.google.com/detail/fcfdekecgocobpjhldifpplcifkfflme **(snippet)** | Watches open Twitch chats for up to 3 keywords and sends desktop alerts with sound. | Partial (keyword detection in chat leading to an alert) | About 38–44 users according to listing sites (snippet). |
| 4 | **Elgato Prompter, Chat Mode**: https://help.elgato.com/hc/en-us/articles/20461145372813-Elgato-Prompter-Chat-Mode **(snippet, page returned 403)** | Shows Twitch chat on a screen behind the camera lens. | Adjacent (puts chat in the streamer's eyeline; no detection of problems) | Commercial hardware (2023). |
| 5 | **WooferBot**: https://obsproject.com/forum/resources/wooferbot.858 **(snippet)** · **Elgato Mochi the Cat**: https://marketplace.elgato.com/product/mochi-the-cat-6ac71734-f507-4887-8350-10357f6e6ea0 **(snippet)** | Mascot widgets that react to chat and alerts. WooferBot also drives Hue and Nanoleaf lights. | Adjacent (a "face" or signal that reacts to stream events, not to problem reports) | Free. Mochi is on the Elgato marketplace. |

### B. Claimed difference
**Yes, partly established.** Each part exists on its own: OBS mute/silence alerts (1, 2), chat keyword alerts (3), and reactive mascots (5). I found nothing that combines viewer reports, mod cues and OBS state into one in-room signal, and nothing with the "fixed → chat confirms" loop. The one feature that would be new on its own is cross-checking chat reports against OBS.

### C. Demand signals
- **Snoop Dogg, July 13, 2021:** he streamed Madden with no audio for over an hour. Chat was in emote-only mode and could not tell him, so viewers spammed mute and mic symbols that he never noticed. https://kotaku.com/twitch-spammers-just-wanted-to-save-snoop-dogg-from-str-1847293788. A related PC Gamer headline says "Snoop Dogg's stream has been muted for a week and his fans can't tell him": https://www.pcgamer.com/uk/snoop-doggs-stream-has-been-muted-for-a-week-and-his-fans-cant-tell-him/ (headline only verified).
- OBS forum request (Jan 28, 2018) for a mute icon visible to the streamer, because "streamers often forget they've muted and speak anyway". It has no replies: https://obsproject.com/forum/threads/mic-mute-notifier-icon-main-screen.80363
- OBS forum thread asking for a MUTE sign that only the streamer can see: https://obsproject.com/forum/threads/is-it-possible-to-put-up-content-like-a-video-that-only-you-can-see-that-doesnt-get-streamed-or-recorded.154430/ **(snippet)**
- A small streamer reported their mic was dead for about 10 minutes before a viewer told them: https://obsproject.com/forum/threads/audio-issues-during-live-stream.56656 **(snippet)**
- DrDisrespect muted himself during a Warzone rage moment and did not notice for about 10 minutes: https://mein-mmo.de/en/drdisrespect-experiences-an-outburst-in-cod-warzone-accidentally-mutes-himself,611302/ **(snippet)**
- **Counter-signals:** none found specifically. One indirect point: the fact that new OBS-only tools (1, 2) exist suggests some streamers solve the mute case without involving chat.

### D. Audience fit
- **Works in:** any stream. It matters most when the streamer is heads-down or in a fullscreen game (most of the top 15 are games), and in IRL (1.8%), where audio problems are common.
- **Share:** potentially almost all of Twitch viewing.
- **Natural-setting demo:** **Partly.** The strongest setting, a fullscreen commercial game, cannot be shown. A heads-down desk task (drawing, building) can stand in for it, and the mic-muted failure itself is natural in any setting.
- **Type-independent?** **Type-independent.**

### E. Fact problems
None. obs-websocket has an `InputMuteStateChanged` event ("An input's mute state has changed") and an `InputVolumeMeters` event (levels every 50 ms) to detect silence: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md

---

## 3. VAR

### A. Closest existing things
| # | Name and link | What it does | Overlap | Activity / popularity |
|---|---|---|---|---|
| 1 | **OBS Instant Replay (Picture-in-Picture)** Lua script by Tomaae: https://obsproject.com/forum/resources/picture-in-picture-instant-replay.746/ | Shows the replay buffer as picture-in-picture. Viewers can trigger it with a chat command (Streamlabs Chatbot script, or standalone since v1.1). | Partial (chat-called replay) | v1.1, last updated Oct 13, 2019. 12,641 downloads, 5.0 stars (3 ratings). |
| 2 | **BarRaider OBS Tools, Instant Replay** (Stream Deck): https://docs.barraider.com/faqs/obs-tools/actions/ | Viewers type `!replay` to show an instant replay on stream. It can also create a Twitch clip and post it to chat. | Partial (chat-called replay plus clip) | Popular Stream Deck plugin family. |
| 3 | **Twitch native Polls** / any chat vote | Votes over a fixed time. | Partial (the jury part only) | Built in. |
| 4 | **Oddshot** (defunct Chrome extension): https://www.producthunt.com/products/oddshot **(snippet)** | Replayed about the last 30 s when someone typed `!shot`. | Adjacent | Defunct. |
| 5 | **Sound Alerts / Blerp meme sounds**: https://soundalerts.com/blog/funny-alert-sounds-for-your-stream-guide-and-setup **(snippet)** | Viewer-triggered meme stingers. A "VAR check"-style sound would fit, but I found no specific VAR product. | Adjacent | Large commercial tools. |

### B. Claimed difference
**Yes.** Chat-triggered replay exists (1, 2) and so do polls, but I found no tool or bit that chains a call threshold, replay, timed jury, verdict and titled clip into one ritual. Searches for "VAR" or "chat jury" overlays on Twitch found nothing.

### C. Demand signals
- Indirect: the chat-triggered replay script has 12.6k downloads, which shows streamers want chat to be able to call replays: https://obsproject.com/forum/resources/picture-in-picture-instant-replay.746/
- Indirect: Twitch has tested and, per secondary sources, shipped a live "rewind" so viewers can re-check moments: https://wwwhatsnew.com/2021/10/21/twitch-prueba-un-boton-para-retroceder-transmisiones-en-directo/ **(snippet)**. Per the snippet, it is limited to subs/Turbo on channels that enable it.
- Direct requests for a chat-jury or VAR review: **Not found.**
- Counter-signals: **Not found.**

### D. Audience fit
- **Works in:** moments where the outcome can be disputed. That means games (most of the top 15, but they cannot be shown in the demo), Sports (#29), IRL challenges and trick shots, and Just Chatting challenge segments.
- **Share:** games are the bulk of viewing, but the demo-able part is Just Chatting/IRL challenge segments (≤16%, and only some of those streams).
- **Natural-setting demo:** **Partly.** A desk trick shot or IRL challenge is a real setting, but the most common setting for disputes (competitive games) cannot be shown.
- **Type-independent?** **Tied** to streams with disputed moments, though those occur across many formats.

### E. Fact problems
None. Create Clip accepts `title` and `duration` up to 60 s, and the clip covers the 90 s window before the call: https://dev.twitch.tv/docs/api/reference/ (Create Clip). obs-websocket has `SaveReplayBuffer` and `GetLastReplayBufferReplay`: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md. One timing note: the clip is taken at verdict time from the last ≤60 s. If stinger + replay + 15 s jury runs long, the original moment may fall outside the clip. The card's own description, where the clip holds the review and the review holds the replay, is consistent with this.

---

## 4. Raid Torch

### A. Closest existing things
| # | Name and link | What it does | Overlap | Activity / popularity |
|---|---|---|---|---|
| 1 | **R3dLabs Toolbox** (Stream Deck plugin): https://marketplace.elgato.com/product/r3dlabs-toolbox-ad81dbc6-0b57-4ef3-a5bb-c210dbd4ee1c | Raid-train helper: one-button raid to the next slot, shows the next streamer's name, and has a 10-min grace cache. | Adjacent (logistics only; no object is carried) | v0.1.1.3, last update Dec 18, 2024. No download count shown. |
| 2 | **RaidRunner** (raid-train scheduling): https://smithery.ai/servers/squidcode/raidrunner **(snippet)** | Claims, trades and waitlists raid-train slots. Has an MCP connector. | Adjacent | Listing published Jun 25, 2026 (snippet). |
| 3 | **Twitch Storm** (2020 24-hour relay): https://www.businesswire.com/news/home/20201125005935/en/Live-Streaming-Influencers-Attract-150000-Plus-Viewers-with-24-Hour-Relay-on-Twitch **(snippet, 403)** | About 200 streamers raided each other every 5 minutes for 24 hours. Followers were called "Storm Chasers". | Partial (an organised relay with a named audience; no state carried on stream) | Claimed 156k+ viewers in Nov 2020 (snippet). |
| 4 | **Teams+** (TwitchCon Hackathon 2019): https://blog.twitch.tv/en/2019/10/31/highlights-from-the-twitchcon-hackathon-2019 | Streamers in a Team share viewer roles and trusted-user marks across channels. | Adjacent (state shared across channels) | Prototype only. |
| 5 | **Raid-wheel game show** (solo dev, GameDev.net): https://gamedev.net/blogs/entry/2298474-i-built-a-live-gameshow-for-twitch-raids-for-small-streamers **(snippet, 403)** | Uses EventSub to see a raid land and Helix to send the next raid, as a game show for small streamers. | Partial (raid-chain mechanics with state) | Portal "slated for fall 2026" (snippet). |

Raid-train communities exist, for example Raid Train Central with themed 36-slot trains over 3 days (https://raidtraincentral.carrd.co/) and the Ace Week raid train (https://aceweek.org/events/fruities-ace-week-raid-train-twitch, snippet).

### B. Claimed difference
**Yes.** Raid-train tools handle scheduling and the button press (1, 2), and relays like Twitch Storm moved audiences, but I found no tool where a visible object with per-chatter marks travels by raid and recognises raiders on arrival. The closest is the raid-wheel game show (5), which I could not open.

### C. Demand signals
- Organised raid trains are an active practice (Raid Train Central, Ace Week, the RaidRunner and R3dLabs tooling). This shows streamers invest effort in raid chains: https://raidtraincentral.carrd.co/
- Since October 2024, raid viewership counts toward Partner status, which gives raiding more weight: https://esports.gg/news/streamers/twitch-now-counts-raids-towards-partner-status/ **(snippet)**
- Retention problem: guides say very few raiders stay or return: https://www.streamscheme.com/?p=8679 **(snippet)**. Raider recognition addresses this, but nobody asks for this exact feature.
- **Counter-signals:** hate raids (2021) made many small streamers wary of raids, and some post "DM before raiding" notices: https://thepinknews.com/2021/08/31/twitch-hate-raids-solution-rekitraven/ **(snippet)**, https://indiecator.org/2021/02/17/twitch-raids-and-safety-measures/ **(snippet)**. There is also a Chrome "Twitch Raid Blocker" that auto-cancels raids: https://www.chromeboard.com/extension/twitch-raid-blocker-kliahaenmgcepgnbomgbjfgfefojdknh **(snippet)**.

### D. Audience fit
- **Works in:** any category, since every channel can raid. It is most relevant to small and mid streamers in raid-train or team communities.
- **Share:** type-independent in principle. In practice it is limited to channels that join a circle; the data does not measure this.
- **Natural-setting demo:** **Partly.** A real raid between test accounts is genuine, but the natural setting is several live communities, while the demo has one streamer and three test accounts.
- **Type-independent?** **Type-independent** (needs a circle of participating channels).

### E. Fact problems
- The EventSub `channel.raid` payload contains only from/to broadcaster IDs and a `viewers` count, **not** the list of raiders: https://dev.twitch.tv/docs/eventsub/eventsub-reference/. "The target streamer sees who the raiders are" therefore only works for raiders the app already knows from their source-channel marks once they chat in the new channel. It cannot cover all raiders. The card's torch-bearer design is consistent with this, but the line "sees who the raiders are" overstates it.
- Raids have a 90 s countdown (or "Raid Now"), and API-started raids can be cancelled until then: https://dev.twitch.tv/docs/api/raids

---

## 5. Previously On

### A. Closest existing things
| # | Name and link | What it does | Overlap | Activity / popularity |
|---|---|---|---|---|
| 1 | **Twitch's native AI stream summaries** (announced TwitchCon Europe, May 30, 2026): https://players.com.ua/en/news/twitch-launches-ai-powered-stream-recaps-for-viewers-who-miss-the-beginning-of-broadcasts/ | A short AI text summary of the stream so far, for viewers who join late. | Same core loop (catch-up for late viewers), but AI-written and not tied to arrival | Labelled an experiment. Rollout details unclear. |
| 2 | **Twitch Recaps (relaunched Oct 22, 2026)**: https://www.netinfluencer.com/twitch-relaunches-stream-recaps-with-permanent-home-automatic-publishing/ | A clip-based recap shelf per broadcast on the channel page. "Twitch Clip That" adds a clip to the Recap live. Auto-publishes about 1 h after the stream. | Partial (curated recap made of clips, mostly after the stream) | Native, just relaunched. |
| 3 | **The Rundown** (TwitchCon Hackathon 2019, Honorable Mention): https://blog.twitch.tv/en/2019/10/31/highlights-from-the-twitchcon-hackathon-2019 · https://devpost.com/software/the-rundown-s5zu4y **(Devpost: snippet)** | An overlay for first-time viewers with community info (rules, commands, memes, clips). | Partial (newcomer briefing triggered by arrival; static content, not a stream-so-far recap) | 2019 hackathon entry. |
| 4 | **Twitch Chat History** (Feb 2023): https://www.tubefilter.com/2023/02/07/twitch-chat-history-replay-conversation-streaming-platform/ | Newcomers see the last 50 messages or last hour of chat, to "catch up with what's happening on the channel". | Adjacent | Native. |
| 5 | **StreamUP Chapter Marker Manager**: https://obsproject.com/forum/resources/streamup-chapter-marker-manager.1962/ | Creates chapter markers from docks, hotkeys or scene changes and puts them into recordings. Not shown to viewers. | Adjacent (the marker-as-beat habit) | 60,499 downloads, v1.3.0 (Apr 14, 2026), 3.63★. |

Third-party VOD summarizers (memories.ai, ScreenApp) only work after the stream: https://memories.ai/tools/twitch-stream-summarizer **(snippet)**.

### B. Claimed difference
**Partly.** Twitch now ships a native "catch up on what you missed" summary (1), and a curated recap shelf (2), so catching up is no longer new. What remains different: the recap is written by humans (markers and mod beats), uses a TV-bumper format, and is triggered by a raid arriving or by `!recap`. Twitch's summary is AI-written and passive.

### C. Demand signals
- Twitch itself built late-joiner catch-up twice in 2026 (AI summaries and Recaps). This is a platform-level signal that the problem is real: links above.
- **Counter-signal to AI summaries, which supports the no-AI angle:** streamers objected to Twitch's AI summaries. They did not want content "fed to an AI bot", worried about misstatements and missed inside jokes, and some "prefer to greet late arrivals and recap the stream themselves": https://gamingpromax.com/twitch-ai-stream-summary-feature-streamer-backlash-twitchcon-rotterdam/
- Raid etiquette guides tell streamers to welcome raiders: https://www.own3d.tv/en/blog/tips/how-to-raid-on-twitch. One guide says to introduce yourself and what you are doing: https://streamlabs.com/content-hub/post/twitch-raids-what-they-are-and-how-to-raid **(snippet)**.
- **Counter-signal to the whole category:** if Twitch's native summary rolls out widely, viewers may not need a channel-side recap. Not measured.

### D. Audience fit
- **Works in:** long streams with a storyline or goal, such as playthroughs (games; cannot be shown), maker, art and dev projects, marathons and events (which the data says cause spikes), and Just Chatting with segments.
- **Share:** type-independent in principle. It is strongest in long narrative streams; no share data.
- **Natural-setting demo:** **Partly.** A desk project stream with markers and a raid from a test account is a real setting, but the strongest setting (a long game playthrough) cannot be shown.
- **Type-independent?** **Type-independent** (works best on long, goal-driven streams).

### E. Fact problems
- **Pin Chat Message** is a documented endpoint and has been generally available since 2026-05-29: https://dev.twitch.tv/docs/change-log/. Constraints: `duration_seconds` 30–1800 (so 10 minutes is fine), only **one mod-pinned message per channel at a time** (a new pin replaces the old one), and it needs `moderator:manage:chat_messages`: https://dev.twitch.tv/docs/api/reference/ (Pin Chat Message). So a `!recap` pin would replace any other mod pin.
- **Stream markers cannot be created if the channel has not enabled VOD storage**, and Get Stream Markers reads markers from the user's most recent video: https://dev.twitch.tv/docs/api/reference/ (Create Stream Marker / Get Stream Markers). A channel without VODs gets no marker-based beats. This is a dependency the card does not mention.
- "Twitch's automatic VOD chapters on category changes": I could not verify this from a Twitch source (unverified, not contradicted).

---

## 6. Studio Audience

### A. Closest existing things
| # | Name and link | What it does | Overlap | Activity / popularity |
|---|---|---|---|---|
| 1 | **StreamElements KappaGen**: https://support.streamelements.com/hc/en-us/articles/10474578102802-How-to-Set-Up-Emote-Explosion-Widget-KappaGen **(snippet)** | An emote-explosion overlay driven by chat emotes and combos. | Partial (chat reactions scaled into spectacle, but visual) | Widely used StreamElements widget. |
| 2 | **Meld Studio Emote Storm**: https://meldstudio.co/gallery/emote-storm/ **(snippet)** | Chat emotes fall and pile up. The amount scales with chat activity. | Partial (scaling with chat; visual, no audio) | Free Meld/OBS widget. |
| 3 | **Sound Alerts**: https://soundalerts.com | Viewers trigger sounds (Bits or channel points). | Adjacent (viewer-triggered audio, one sound per redeem, no crowd) | Large commercial tool. |
| 4 | **Emote soundboard practice** (VoxBooster guide, Jun 12, 2026): https://voxbooster.com/blog/soundboard-meme-audios-twitch-chat-emotes/ | The streamer fires KEKW/LUL laugh clips by hand with hotkeys. | Adjacent (laugh audio for chat emotes, triggered manually) | Guide. |
| 5 | **Plus 2** (Firefox) / **Chat Decoder hype meter**: https://addons.mozilla.org/fr/firefox/addon/plus2/ **(snippet)** · https://www.exmachinagroup.com/case-study/twitch-chat-decoder **(snippet)** | A bar showing chat excitement from keywords and emotes. | Adjacent (chat-energy measurement, visual) | Small. |

Also: **Crowd Sounds** app (applause/laughter/boo soundboard, not chat-linked): https://apps.ape-apps.com/crowd-sounds **(snippet)**. **Elgato "Popular Sounds"** includes sitcom laugh tracks for Stream Deck: https://marketplace.elgato.com/product/popular-02b0b7e6-b3f6-4a4d-a8e6-8e4480aedd80 **(snippet)**.

### B. Claimed difference
**Yes.** Visual chat-scaled reactions exist (1, 2) and manual laugh soundboards exist (4), but I found no tool that mixes a crowd you can hear, scales by distinct reactors, and gives each viewer a signature voice. Searches for chat-driven laugh tracks or crowd audio found nothing.

### C. Demand signals
- Small streamers describe streaming to silence or lurkers as demoralising. Example: the r/Twitch thread "How do you stream with no one watching" (Dec 2023): https://reddit.rtrace.io/r/Twitch/comments/18d4o85/how_do_you_stream_with_no_one_watching/kcf62ri/?context=3 **(snippet, Reddit mirror)**. Also a partnered streamer (~13k followers) who ended a stream in anger because chat was all lurkers (Aug 2018): https://www.dexerto.com/entertainment/emotional-streamer-rage-quits-his-broadcast-because-no-one-was-putting-anything-in-the-chat-141564/
- Streamers already build emote-to-laugh soundboards by hand (VoxBooster guide above).
- **Counter-signal:** the same guide warns that "triggering KEKW audio every time the emote appears turns a comedic tool into repetitive noise": https://voxbooster.com/blog/soundboard-meme-audios-twitch-chat-emotes/
- **Counter-signal:** streamers complain about viewers spamming sound alerts and ask for per-user blocks, for example "a particular viewer quite over uses/spams the Sound Alerts" (Mar 3, 2022): https://feedback.soundalerts.com/p/restrict-a-specific-user-from-using-sound-alerts
- **Counter-signal (inference, not a source):** in channels with 0–3 chatters, a crowd scaled to distinct reactors stays very small. This is the 61%-under-10-viewers segment from the brief.

### D. Audience fit
- **Works in:** comedy, Just Chatting (14.2%), Talk Shows & Podcasts, IRL (1.8%), and game streams with an active chat (audio must not clash with game sound).
- **Share:** Just Chatting plus IRL is about 16%. Talk shows are small (rank ~#66–71).
- **Natural-setting demo:** **Partly.** Desk talk is the natural setting, but with 3 test accounts the crowd is, by design, at most 3 voices. The "louder when more react" claim cannot be shown at scale.
- **Type-independent?** Mostly type-independent. Best on talk-heavy streams.

### E. Fact problems
None found.

---

## 7. Foley Pit

### A. Closest existing things
| # | Name and link | What it does | Overlap | Activity / popularity |
|---|---|---|---|---|
| 1 | **"Sound Effects" improv game** (Whose Line; improv standard): https://improwiki.com/en/wiki/sound-effects | Performers act a scene while others, often audience volunteers, make the sound effects live. | Partial (live performed sound for a scene; no scoring, and the roles differ) | Long-standing TV and improv format. |
| 2 | **Mimic Party** (FoliesApp, Steam Aug 27, 2026): https://www.stork.ai/en/mimic-party | Players imitate a reference sound and a local AI scores it (melody, rhythm, attacks) out of 100. | Partial (an AI judges imitated sounds; no Twitch, voice not props) | 44% positive Steam reviews as of Sep 3, 2026 (per the listing). |
| 3 | **Echotations** (mobile party game): https://www.pocketgamer.fr/games/033298/echotations/ **(snippet)** | Players compete to imitate sounds. | Adjacent | Unknown. |
| 4 | **Chat-triggered sound commands** (e.g. screm, AoE taunts extension): https://github.com/skynewz/screm **(snippet)** | Viewers trigger pre-recorded sounds. | Adjacent (chat chooses sound; playback, not performance) | Small. |
| 5 | **Sound Alerts channel-point sounds**: https://support.soundalerts.com/article/channel-points-alerts **(snippet)** | Viewers spend points to play a sound. | Adjacent | Large tool. |

### B. Claimed difference
**Yes.** No Twitch tool or bit was found where chat writes a sound score, the streamer performs it with props, and a model scores it. AI imitation scoring exists in a non-Twitch party game (2), and live audience sound effects exist in improv (1).

### C. Demand signals
- Direct: **Not found.** No posts asking for a foley or sound-performance game on stream.
- Indirect: Just Chatting advice says structured on-screen activities work better than plain talk: https://www.jeffbullas.com/thread/what-are-some-good-just-chatting-content-ideas-for-when-i-dont-want-to-play-a-game/ **(snippet)**
- **Counter-signal (technical):** CLAP-style text-audio relevance scores ("CLAPScore") have "a low correlation with human subjective evaluation scores" (Human-CLAP paper, 2025): https://arxiv.org/abs/2506.23553v2. The Foley meter's percentages may not match what viewers hear.
- **Counter-signal:** Mimic Party, the closest AI-judged imitation game, has 44% positive Steam reviews (per stork.ai listing above). The reason for the rating is not given.

### D. Audience fit
- **Works in:** Just Chatting (14.2%), ASMR (#34), IRL, and creative or Art streams, as a segment rather than a whole stream.
- **Share:** Just Chatting is the main pool, but this would be one segment within it.
- **Natural-setting demo:** **Yes.** A desk with props is the natural setting, and no commercial content is needed.
- **Type-independent?** **Tied** to a performance segment (a format the streamer has to adopt).

### E. Fact problems
None in Twitch facts. See the CLAPScore reliability note in C.

---

## 8. Hint Jar

### A. Closest existing things
| # | Name and link | What it does | Overlap | Activity / popularity |
|---|---|---|---|---|
| 1 | **LeagueBackseat**: https://github.com/HerXayah/LeagueBackseat | A Twitch bot where viewers queue timestamped "backseat" messages (`!add <timestamp> <msg>`) for the streamer to look up later. | Partial (queues help instead of posting it; no tiers or reveal show) | 0 stars, 37 commits, no releases. |
| 2 | **Universal Hint System (UHS)**: https://en.wikipedia.org/wiki/Universal_Hint_System **(snippet)** | Tiered hints from nudge to answer, revealed one by one (since 1988). | Partial (the same tiered-hint idea; not live and not from viewers) | Long-running. |
| 3 | **Chat Curtain** (Chrome extension): https://chromeboard.com/extension/chat-curtain-ofdmpokiehfdakmadncelpmnnhmbgabp **(snippet)** | "Active mode" shows only mod-approved chat messages. | Adjacent (mod-gated messages) | Small. |
| 4 | **Channel-point rewards with text input**: https://docs.streamchatai.com/guides/twitch-channel-point-guide/ **(snippet)** | Rewards can require text, with cooldowns and per-user limits, which could carry a hint by hand. | Adjacent | Native Twitch. |
| 5 | **No-backseating rules and `!backseat` / `!spoilers` commands**: https://nobackseating.carrd.co/ · https://streamhub.world/streamer-blog/strategy/1199-how-to-handle-viewer-spoilers-and-backseating-on-stream/ | Etiquette: ask before hinting. Some streamers accept a "gentle nudge" after being stuck. | Adjacent (the manual practice) | Common. |

I did not find the "backseat allowed for 1 min" channel-point reward as a documented example (**Not found**).

### B. Claimed difference
**Yes.** Help is queued elsewhere (1) and tiered hints exist offline (2), but I found no live tool where viewers submit tiered, sealed hints that the streamer opens on screen one tier at a time.

### C. Demand signals
- Backseating is described as one of the most frequent and frustrating problems for streamers. Guides recommend asking before giving a hint and a "gentle nudge" when the streamer is stuck: https://streamhub.world/streamer-blog/strategy/1199-how-to-handle-viewer-spoilers-and-backseating-on-stream/ (2026-03-15), https://nobackseating.carrd.co/
- Steam thread "Backseating problem" (Limbus Company, Apr 5, 2025): constant backseating "pushes people away" from the games' streams. Replies cite a streamer who left a game because of it: https://steamcommunity.com/app/1973530/discussions/0/597397269594002793
- Streamer outbursts at backseating: Elajjaz on God of War Ragnarök's hints (https://www.sportskeeda.com/esports/news-i-will-legit-mute-voices-twitch-streamer-lashes-god-war-ragnarok-s-backseat-gaming, **snippet**) and 39daph (https://www.dexerto.com/entertainment/39daph-rages-at-greekgodx-for-infuriating-backseat-gaming-1316602/, **snippet**).
- **Counter-signal:** in the same Steam thread, several replies say the fix is simply rules, timeouts and bans ("those who set hard rules have few problems"), so a tool may not be needed: link above. Some streamers want no hints at all (blind/no-spoiler purists): https://nobackseating.carrd.co/

### D. Audience fit
- **Works in:** first or blind playthroughs of puzzle, adventure, horror and indie games. Indie games are +51% YoY and horror +6% (from the brief). It could also fit puzzle-hunt or escape-room IRL streams.
- **Share:** a subset of game viewing. The brief has no data on blind playthroughs.
- **Natural-setting demo:** **Partly.** It has to use an original puzzle game built for the demo. The real setting is a commercial game, which cannot be shown.
- **Type-independent?** **Tied** to blind or first playthroughs.

### E. Fact problems
None. Note that Twitch removed the "Blind Playthrough" tag in Dec 2020. "First Playthrough" plus "No Spoilers" is the suggested wording: https://www.pocketgamer.biz/twitch-removes-blind-playthrough-tag-to-use-inclusive-language **(snippet)**. This only matters for wording in the video.

---

## 9. Photo Booth

### A. Closest existing things
| # | Name and link | What it does | Overlap | Activity / popularity |
|---|---|---|---|---|
| 1 | **StreamUP Polaroid Picture** (OBS + Streamer.bot add-on): https://streamup.tips/product/polaroid-picture | "Viewers spend points to take a photo of you, with their message printed underneath." 3-s countdown, photo of any OBS source, animated Polaroid on stream, saved locally or posted to Discord. Also triggers on cheers, follows, subs and **raids**. | **Same core loop** (viewer-triggered countdown photo of the streamer as a Polaroid) | v3.0.3, page updated Sep 10, 2026, £15. Docs: https://streamup.notion.site/Polaroid-Picture-Documentation-a0f36c6cb1604ffba21ded3945a469b5 (snippet). |
| 2 | **Movie Poster (Channel Point Reward)** for Streamer.bot: https://extensions.streamer.bot/t/movie-poster-channel-point-reward/135 | The redeemer's profile picture and username appear on stream in a movie poster. | Partial (viewer avatar composited into a framed picture) | Jun 30, 2023, 6 likes. |
| 3 | **Streamlabs End Credits**: https://streamlabs.com/content-hub/post/the-credits-widget **(snippet)** | A scrolling list of the session's followers, subs, donors, mods and raids at the end of the stream. | Partial (end-of-stream "who was here", text only) | Widely used. |
| 4 | **Chat-avatar overlays** (e.g. Meld Pixel Art Avatars): https://meldstudio.co/gallery/pixel-art-avatars/ **(snippet)** | Every chatter appears as an avatar on stream. | Adjacent (the whole chat on screen) | Free and popular category. |
| 5 | **In-person meet & greet photos** (TwitchCon): https://streamscharts.com/news/meet-greet-twitch-con-las-vegas-2023 | Streamers take photos with fans at TwitchCon. | Adjacent (the bit being made virtual) | Official TwitchCon programme. |

### B. Claimed difference
**Partly.** StreamUP Polaroid already does the core loop: a viewer triggers a countdown, the streamer is photographed, and it shows as a Polaroid (with raid triggers too). The parts not found elsewhere are compositing the viewer's avatar into the photo next to the streamer, a group photo with every raider's avatar, the 24 h viewer link, and the end-of-stream corkboard collage. Movie Poster (2) shows avatar compositing exists in a simpler form.

### C. Demand signals
- Twitch's own extension guide (2019): "getting a callout from a streamer is a big reason why viewers subscribe or cheer with Bits on stream": https://blog.twitch.tv/en/2019/05/30/nine-must-have-twitch-extension-features-5bb1f1ff45ca
- Meet-and-greet photos are a core TwitchCon activity: https://streamscharts.com/news/meet-greet-twitch-con-las-vegas-2023
- A commercial product sells this exact bit (StreamUP Polaroid, £15), which shows streamers pay for it: link above.
- **Counter-signal:** guides warn against singling out lurkers, saying recognition should be opt-in: https://frostytools.com/blog/how-to-welcome-new-followers-on-twitch/ **(snippet)**, https://indiecator.org/2022/03/20/creating-a-lurker-friendly-environment/ **(snippet)**. A raid group photo that includes everyone could conflict with this. Note that the card can only include raiders it knows (see card 4 E).

### D. Audience fit
- **Works in:** any stream with a facecam. It suits Just Chatting (14.2%) and IRL (1.8%) best, and facecam game streams too.
- **Share:** broad, as most streams with a camera.
- **Natural-setting demo:** **Yes.** A desk facecam is the natural setting.
- **Type-independent?** **Type-independent** (needs a camera).

### E. Fact problems
- Raid group photo: EventSub `channel.raid` gives only a viewer count, not raider identities (https://dev.twitch.tv/docs/eventsub/eventsub-reference/). "All raiders' avatars" can only include raiders who identify themselves, for example by chatting. It cannot be the whole raid party.
- obs-websocket `SaveSourceScreenshot` / `GetSourceScreenshot` exist for the frame grab: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md

---

## 10. Checkpoint

### A. Closest existing things
| # | Name and link | What it does | Overlap | Activity / popularity |
|---|---|---|---|---|
| 1 | **Meld Studio X AMA Question Queue**: https://meldstudio.co/gallery/x-ama-question-queue/ | Messages ending in "?" are gathered into an on-screen queue automatically, or viewers use `!ask`. The streamer clicks the next question to bring it to the top. | Partial (captures without a command, queues to answer later; no focus window, context or reply ping found) | Free Meld/OBS widget. |
| 2 | **StreamerQnA** (OBS dock + browser source): https://obsproject.com/forum/resources/streamerqna.1977 | Viewers submit questions with commands. Questions are shown one at a time, with duplicate detection. | Partial (command-based queue) | v1.0.3, Jul–Sep 2024, 9,543 downloads. |
| 3 | **Social Stream Ninja featured message**: https://socialstream.ninja/docs/commands.html **(snippet)** | Feature one message on stream from a dock. Has queue advance and auto-show. | Partial (lower-third featured message, manual) | Popular open-source tool. |
| 4 | **Twitch Chat History** (native, Feb 2023): https://www.tubefilter.com/2023/02/07/twitch-chat-history-replay-conversation-streaming-platform/ | Shows the last 50 messages or last hour. | Adjacent | Native. |
| 5 | **Chatterino highlight phrases**: https://chatterino.com/ **(snippet)** · https://doxygen.chatterino.com/classchatterino_1_1_highlight_phrase.html **(snippet)** | Highlights or sounds on keywords, plus a mentions panel. | Adjacent | Popular desktop chat client. |

Twitch's AI catch-up summary (card 5, item 1) is also adjacent.

### B. Claimed difference
**Partly.** Auto-capturing questions without a command already exists (Meld AMA queue). What I did not find elsewhere: a time-boxed focus mode that captures all normal messages, a context screenshot for each message, an in-thread "answered on stream" reply to the viewer, and an "N answered" summary.

### C. Demand signals
- Streamlabs guide: "the chat flies by so fast, it's basically impossible for the streamer to respond to most comments". It recommends scheduled breaks to read chat, a disclaimer "that you're not ignoring them", and mods keeping "a running list of questions … and give you a quick recap during your break". That is essentially the manual version of Checkpoint: https://streamlabs.com/content-hub/post/how-to-maintain-game-concentration-while-streaming
- Twitch built Chat History so newcomers can catch up on chat, which shows the platform sees missed chat as a problem: link in A4.
- A streamer missed a Kai Cenat invitation because he did not see it in chat: https://www.sportskeeda.com/us/streamers/news-twitch-streamer-misses-streamer-university-seeing-kai-cenat-s-invitation-chat **(snippet)**
- "Missing messages makes viewers feel ignored" (IRL-focused vendor blog, 2026): https://streamchatai.com/blog/irl-streaming-tips-chat-engagement **(snippet)**
- Counter-signals: **Not found.**

### D. Audience fit
- **Works in:** heads-down formats such as Art (#40), Software & Game Development, Makers & Crafting, Food & Drink, and focus-heavy games (which cannot be shown).
- **Share:** the demo-able categories are small. Art has only ~17 viewers per channel, and the others are "far lower" in the data. Focused gameplay is a large pool but cannot be shown.
- **Natural-setting demo:** **Yes.** Drawing or building at a desk is the natural setting.
- **Type-independent?** Partly. It works on any stream with focus stretches, but it is aimed at focus-heavy formats.

### E. Fact problems
None. Send Chat Message supports `reply_parent_message_id` for threaded replies (https://dev.twitch.tv/docs/api/reference/, Send Chat Message). obs-websocket `SaveSourceScreenshot` exists (https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md).

---

## Final summary table

| Card | Closest thing (link) | Overlap | Difference survives | Demand signals found | Counter-signals | Natural-setting demo | Type-independent |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1. Minefield | OK Gamers, TwitchCon Hackathon 2019 (https://github.com/twitchcon/ok-gamers-frontend); Streamer.bot Voice Control (https://docs.streamer.bot/guide/voice-control) | Partial | Yes | Weak/indirect (manual catchphrase counters, Wordeous); no direct request | Yes: bait-to-say trolling and suspension risk | Yes | Mostly (any talking stream; English STT) |
| 2. Tap on the Shoulder | Audio Source Mute Indicator (https://obsproject.com/forum/resources/audio-waves-visualizer.2247/); Remember to Talk (https://obsproject.com/forum/resources/remember-to-talk.2484/) | Partial | Yes (combination and confirm loop new; parts exist) | Strong anecdotal (Snoop Dogg muted for over 1 h, chat couldn't tell him; OBS forum mute-icon requests) | None found | Partly | Yes |
| 3. VAR | OBS Instant Replay PiP with chat trigger (https://obsproject.com/forum/resources/picture-in-picture-instant-replay.746/) | Partial | Yes | Indirect only (12.6k downloads of chat-replay script) | None found | Partly | Tied (disputed moments) |
| 4. Raid Torch | R3dLabs Toolbox (https://marketplace.elgato.com/product/r3dlabs-toolbox-ad81dbc6-0b57-4ef3-a5bb-c210dbd4ee1c); Twitch Storm relay (snippet) | Adjacent / Partial | Yes | Indirect (active raid-train communities; raids count for Partner) | Yes: hate-raid wariness, raid blockers | Partly | Yes (needs a circle of channels) |
| 5. Previously On | Twitch native AI stream summaries (https://players.com.ua/en/news/twitch-launches-ai-powered-stream-recaps-for-viewers-who-miss-the-beginning-of-broadcasts/) | Same core loop (catch-up) | Partly (human-curated, arrival-triggered TV format) | Strong (Twitch built catch-up twice in 2026; streamer backlash against AI summaries) | Yes: native feature may make it redundant | Partly | Yes |
| 6. Studio Audience | KappaGen / Meld Emote Storm (https://meldstudio.co/gallery/emote-storm/) | Partial | Yes | Indirect (streaming-to-silence complaints; manual laugh soundboards) | Yes: "repetitive noise" warning; sound-alert spam complaints | Partly (3 test accounts = tiny crowd) | Mostly |
| 7. Foley Pit | Improv "Sound Effects" game (https://improwiki.com/en/wiki/sound-effects); Mimic Party AI imitation scoring (https://www.stork.ai/en/mimic-party) | Partial | Yes | Not found | Yes: CLAPScore correlates poorly with humans; Mimic Party 44% positive | Yes | Tied (performance segment) |
| 8. Hint Jar | LeagueBackseat (https://github.com/HerXayah/LeagueBackseat) | Partial | Yes | Moderate (backseating widely called a top frustration; Limbus thread) | Yes: rules/bans seen as enough; no-hint purists | Partly (original game only) | Tied (blind/first playthroughs) |
| 9. Photo Booth | StreamUP Polaroid Picture (https://streamup.tips/product/polaroid-picture) | Same core loop | Partly (avatar compositing, raid group photo, collage) | Moderate (paid product exists; callouts drive support; meet-and-greet photos) | Yes: don't single out lurkers | Yes | Yes (needs camera) |
| 10. Checkpoint | Meld X AMA Question Queue (https://meldstudio.co/gallery/x-ama-question-queue/); StreamerQnA (https://obsproject.com/forum/resources/streamerqna.1977) | Partial | Partly (focus window, context thumbnail, reply ping new) | Moderate (Streamlabs guide describes the manual version; Twitch Chat History) | None found | Yes | Partly (focus-heavy formats) |
