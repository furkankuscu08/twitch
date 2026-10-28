# Link check: single-source competitors and key signals

Checked 2026-10-28. Method: read README rules and the six cards (1, 2, 3, 4, 6, 8); compared names across the three reports; opened each single-source link with WebFetch (one alternative web search if it failed); ran 2-3 web searches per high-risk claim. "Well-known" follows README (major platform tool, 1,000+ users/installs, 100+ stars, or 10,000+ views on a post/video). **(snippet)** = seen only in search results, page not opened. "Blocked" = the server refused the fetch (403/402/405/429), so the page may be alive but I could not read it. Reddit cannot be fetched by this tool at all, and X got one attempt (402). Rule applied from README: a single-source link I could not open is not counted as confirmed. Overlap levels are proposals; nothing is scored.

Reading note: "found by" is A (Astra), G (Grok), C (Claude). Items found by 2+ researchers are not listed here (OK Gamers, Streamer.bot Voice Control, 1up Bingo, Twitch Guardian, Elgato Prompter, Mochi, WooferBot, Sound Alerts, Meld Emote Storm, KappaGen, R3dLabs, RaidRunner, LeagueBackseat, BackseatMe, native polls, OBS replay scripts). Two of those were still opened because they decide a card (Meld Emote Storm, tomaae replay).

**Headline: no Same-core-loop finding for any of the six cards.** The closest single-source items are all Partial or Adjacent.

---

## 1. Minefield

| Competitor | Found by | Link status | What it actually does | Activity / popularity | Well-known? | Proposed overlap |
| --- | --- | --- | --- | --- | --- | --- |
| Blabla Radar Swear Jar | A | Opens | Browser speech recognition counts words from an editable list; each hit adds 50 cents to a virtual jar. Optional ~60 MB local model (beta). Operated by the user; no viewer or audience feature mentioned. | No date, no user numbers | No | Partial (speech hit on a list, but the streamer's own list, no viewers, no on-stream explosion) |
| scpedicini/swearjar | G | Opens | Browser speech recognition beeps when a censored word is heard. README: Chrome only, no mobile. | 0 stars, 0 forks, 2 commits | No | Partial/Adjacent (beep only) |
| obs-popup-overlay (erfur) | G | Opens | OBS plugin: offline Vosk speech recognition shows an image when a hotword is heard (demo word "archlinux"). | 0 stars, 1 fork, 3 commits, no dates shown | No | Partial (speech hit becomes an on-stream effect, but one fixed word, no viewers) |
| Kloot swear-jar overlay | G | Opens | Manual +1 counter pressed by the streamer or a mod (Pro plan); does not listen. | No usage numbers (the 1,248 on the page is a mock-up) | No | Adjacent |
| Wordeous (Steam) | C | Opens | Taboo-style card game; streamer describes a word without banned words, Twitch chat types guesses. | Released 22 Aug 2022, 19 reviews (89% positive) | No | Adjacent |
| Hasbro Taboo | A | Not fetched (well-known board game) | Speaker avoids forbidden words. | n/a | n/a | Adjacent |
| AnkhbotSecretWord (Yaz12321) | C | Opens (repo found via profile) | Streamlabs Chatbot script: streamer picks a secret word, the viewer who types it in chat wins. | 6 stars, no date shown | No | Adjacent (roles reversed, chat not speech) |
| LocalVocal (OBS plugin) | C | Opens | Local Whisper captions in OBS; caption filter/replace. No word triggers listed. | 1.7k stars, 129 forks, v0.6.2 | Yes (stars) | Adjacent (building block, not a game) |
| Nightbot `$(count)` | C | Opens | Counts how often a command was used (e.g. a hug counter). | Part of Nightbot | n/a | Adjacent (manual counting) |
| ByteMike Bingo overlay | G | Not opened | Public bingo board. | n/a | n/a | Adjacent (same class as 1up Bingo) |

**Novelty re-search (Minefield):** three searches (Twitch secret words + speech, GitHub hidden-word + whisper trigger). Not found. Only chat-typed trigger overlays (Triggleh, GG Drop, goldzulu twitch-avatars, Contexto On Stream) and no speech-based viewer-word game.

**Signal links**

| Signal | Link | Status |
| --- | --- | --- |
| Reddit word-detection request (Jul 2022, mic detection to trigger a VTuber effect) | reddit.com/r/Twitch/comments/vvjk4x/ | Unverifiable (tool cannot fetch Reddit; a web search did not surface it) |
| faster-whisper hotword hallucination on silence (issue 1356) | github.com/SYSTRAN/faster-whisper/issues/1356 | Opens. Hotwords were echoed on silent audio; maintainer says known, use `vad_filter=True`; issue closed. The card already plans VAD. |
| Counter-signal: baiting streamers into saying words (Dexerto) | dexerto.com/.../korean-irl-streamers-baited-lewd-donation-prank-1045134/ | Opens. Sept 2019: a troll tip made a streamer say a phrase that sounded like a slur. Supports the blocklist rule. |
| Manual swear jar posts (X, Grok) | x.com/seapickle1322/... etc. | Unverifiable (X) |

---

## 2. Tap on the Shoulder

| Competitor | Found by | Link status | What it actually does | Activity / popularity | Well-known? | Proposed overlap |
| --- | --- | --- | --- | --- | --- | --- |
| Muted Notification (OBS plugin) | G | Opens | OBS audio filter: when the source gets audio while muted, plays a WAV to a chosen device or shows a red circle. | 12,466 downloads, 37,124 views; released 5 Apr 2023, last update 20 Jul 2024; 5.0 from 1 rating | Yes (downloads) | Partial (OBS-side "you are talking while muted", streamer-private; no viewers, no mods, no confirm loop) |
| StreamNotch mic guide | G | Opens | Promotion page for a $9 Mac notch app that warns on muted/silent/clipping mic; app also shows chat. | Page updated 19 Oct 2026; no user numbers | No | Adjacent (own-mic alerts only; Mac only) |
| ViperVex Mic Status | G | Blocked (429 twice) | Per Grok: OBS WebSocket mute state as a "MIC MUTED" overlay. Not verified by me. | n/a | Unknown | Adjacent (snippet-level; if as described, the OBS-mute part only) |
| Audio Source Mute Indicator | C | Opens | OBS Lua script: tone and emoji overlay when a source is muted/unmuted; overlay hidden from capture. | 4,561 views, no download count; released 30 Oct 2025 | No | Partial (OBS mute only) |
| Remember to Talk | C | Opens | OBS plugin: private alert if your mic is silent too long; cooldowns, hotkey. | 2,448 downloads, 5,209 views; released and last updated 5 May 2026; no ratings | Yes (downloads) | Partial (silent-mic detection, private chime; no viewers) |

Note: Remember to Talk and Muted Notification together cover the "OBS says mic muted/silent" input of the card with real installs. The viewer-report, mod-cue, phone-face and chat-confirm parts are not covered by anything found.

**Signal links**

| Signal | Link | Status |
| --- | --- | --- |
| Snoop Dogg muted stream (Kotaku) | kotaku.com/twitch-spammers-just-wanted-to-save-snoop-dogg-from-str-1847293788 | Opens. 13 Jul 2021 Madden stream had no sound; chat was emote-only, viewers spammed mute/mic icons, he did not notice; ended after a bit over an hour. |
| PC Gamer Snoop headline | pcgamer.com/uk/snoop-doggs-stream-has-been-muted-for-a-week... | Opens, headline only (body truncated) |
| OBS forum request for a streamer-only mute icon (Jan 2018) | obsproject.com/forum/threads/mic-mute-notifier-icon-main-screen.80363 | Opens. Posted 28 Jan 2018; request only, no replies visible. |
| DrDisrespect muted himself (mein-mmo) | mein-mmo.de/en/drdisrespect-...-mutes-himself,611302/ | Opens. Muted a little over 10 minutes; viewers did tell him (he said he got about $100 from people pointing it out). Shows chat does notice and tell, a mild counter-signal to "nobody tells you". |
| Reddit r/streaming "do streamers appreciate viewers telling them" (Astra, Sep 2026) | reddit.com/r/streaming/comments/1wemj7w/... | Unverifiable (Reddit) |

---

## 3. VAR

| Competitor | Found by | Link status | What it actually does | Activity / popularity | Well-known? | Proposed overlap |
| --- | --- | --- | --- | --- | --- | --- |
| PROVE IT (Devpost) | A **(snippet)** | **Blocked** (403); a web search for the slug and for the description found nothing | Cannot be confirmed. Astra's snippet only. | Unknown | No | Not counted (README: link fails, drop). If it exists as described it would be Partial, not Same core loop: no replay is mentioned in Astra's text. Re-check by hand if the user wants. |
| Fyre Instant Replay | A | Opens | Two tools: a `!clip` API command, and a StreamElements-only Instant Replay widget where viewers use `!replay` and the clip plays on the overlay. The page says "vote-to-trigger options" exist but gives no details. | Copyright 2019; no user numbers | Part of the StreamElements ecosystem, but the tool itself shows no numbers: **No** | Partial (chat triggers a replay; vote detail unknown) |
| Glitch Studios Instant Replay | A | Opens | Free OBS browser-source overlay (Twitch, Kick, YouTube). Mods trigger a branded replay with REPLAY banner and countdown; `slow` gives 0.5x. No chat voting. | (c) 2026; no user numbers | No | Partial (mod-triggered branded slow-mo replay; no call threshold, no jury, no verdict) |
| BarRaider OBS Tools, Instant Replay | C | Opens | Stream Deck action saves recent footage; with Twitch integration, chat `!replay` shows an instant replay and can create a Twitch clip posted in chat. No voting. | No count on the page; BarRaider plugins are on the Elgato marketplace (count not checked) | Unverified | Partial |
| RTS Action Replay (X post) | G | **Blocked** (X post returned 402; web search found nothing) | Per Grok: manages replay-buffer, Twitch, YouTube and Kick clips and plays them as a replay. Not verified. | n/a | Unknown | Partial at most; unverified |
| Senchabot chat poll | G | Opens | Free overlay; mods start `!poll`, each account votes once by typing a number, bars fill on stream; optional subscriber vote weight, stream-delay grace. | No numbers | No | Partial (jury half only) |
| Oddshot | C **(snippet)** | Not opened | Defunct extension, replayed last 30 s on `!shot`. | Defunct | No | Adjacent |
| tomaae obs-instant-replay (A+G+C, opened for popularity) | all | Opens | OBS picture-in-picture replay of the buffer; viewers can trigger it by chat command. | Repo 42 stars, 9 forks; OBS resource 12,642 downloads, 15,190 views, v1.1, released 26 Dec 2018, last updated 13 Oct 2019, 5.0 from 3 ratings | Yes (downloads) | Partial (chat-called replay; no review ritual) |

**Novelty re-search (VAR):** four searches. Closer than before, but still not close: **Streamer's Court** (Steam, 21 Jul 2022; the streamer rules on a viewer "crime", chat then votes guilty/not guilty, streamer reputation moves if rulings differ; no replay) is a chat-jury verdict game, Adjacent to the jury half. Nothing combines a call, a replay and a chat verdict. Not found otherwise (searched for "VAR" overlays, `!var` bots, replay-then-vote tools).

**Signal links**

| Signal | Link | Status |
| --- | --- | --- |
| OBS PiP instant replay, 12.6k downloads | obsproject.com/forum/resources/picture-in-picture-instant-replay.746/ | Opens. 12,642 downloads (matches), but last updated Oct 2019: the number shows past demand for a chat-called replay, not current activity. |
| Reddit "instant replays" request (Jan 2026) | reddit.com/r/Twitch/comments/1qq6slj/instant_replays/ | Unverifiable (Reddit) |
| X posts on replay buffer + Stream Deck (Grok) | x.com/avengerUNKNOWN1/... | Unverifiable (X) |

---

## 4. Raid Torch

| Competitor | Found by | Link status | What it actually does | Activity / popularity | Well-known? | Proposed overlap |
| --- | --- | --- | --- | --- | --- | --- |
| Raid-wheel game show = **RaidPort** | C **(snippet from gamedev.net, 403)**; raidport.tv opens | gamedev.net blog blocked (403), snippet read via search; **raidport.tv opens** | Streamers raid the always-live RaidPort channel at stream end and earn a "Portal Charge" (one wheel slice). Chat votes which category gets a bigger slice; the wheel lands on a live channel and the whole channel raids it. No login, it just sees the raid land. Beta, "portal opens Fall 2026", alpha test running. | Solo project, no user counts; copyright 2026 | No | Adjacent (a raid is the trigger and a per-raid token is earned, but it is a hub with a wheel, not a torch carried by chatters, and nothing is shown on arrival) |
| Raid Train (Devpost 2019) | A | **Blocked** (403); the Twitch 2019 hackathon recap does not list it; search found nothing | Cannot be confirmed. Astra says viewers nominate and vote on the next raid destination. | Unknown | No | Not counted (README rule). If real, Adjacent. |
| Twitch Storm (2020 relay) | C **(snippet)** | **Blocked** (BusinessWire 403) | Per snippet: about 200 streamers raided each other every 5 minutes for 24 hours, 156k+ viewers claimed. | 2020 event | A press release claims 156k viewers but it is not on a page I could read | Adjacent (an organised relay; no state carried) |
| Teams+ (TwitchCon Hackathon 2019) | C | Verified via Twitch hackathon recap | Prototype: streamers on a Team mark viewers "Trusted" and share those labels across the group. | Prototype only | No | Adjacent (state shared across channels, not tied to raids) |
| Raid Train Central | C | Opens | Discord/community running themed raid trains (2-hour slots, 36 slots over 3 days for some months; raid out at your designated time). No carried object. | Active in 2026 (rule update for Sept 2026) | No numbers | Adjacent |
| Raid Train details at R3dLabs (A+G+C, opened) | all | Opens | Six tools (Schedule panel, Glance, FirePanel, Toolbox, R3ddyBot, Flyer Studio) for scheduling and one-press raiding. | Elgato listing v0.1.1.3, 18 Dec 2024 | Via Elgato marketplace only; no count | Adjacent (logistics) |

**Signal links**

| Signal | Link | Status |
| --- | --- | --- |
| Hate raids (The PinkNews, 31 Aug 2021) | thepinknews.com/2021/08/31/twitch-hate-raids-solution-rekitraven/ | Opens. Follower bots flood channels with abuse; many marginalised streamers afraid to go live. (Counter-signal for open raid circles; the card uses an opt-in code.) |
| Raids count toward Partner (esports.gg) | esports.gg/news/streamers/twitch-now-counts-raids-towards-partner-status/ | Blocked (403) |
| Reddit "do you stay for the raid" (Dec 2025) | reddit.com/r/Twitch/comments/1pxpu4j/... | Unverifiable (Reddit) |

---

## 6. Studio Audience

| Competitor | Found by | Link status | What it actually does | Activity / popularity | Well-known? | Proposed overlap |
| --- | --- | --- | --- | --- | --- | --- |
| Twitch Sense (Devpost, 2017 TwitchCon hackathon) | A | **Blocked** (403). The Twitch recap of the first (2017) hackathon names only Audio Split Stream, Kappa Cloud and Surprise Me!; no "Twitch Sense" or sentiment-to-music project. A web search found no page. | Cannot be confirmed. | Unknown | No | Not counted (README rule). If real, Partial at most (sentiment, not a per-viewer mixed crowd). Doubtful: the 2017 recap contradicts the date. |
| Blerp walk-on sounds | G | **Blocked** (403 on blerp.com pages) | Per Grok: a large viewer soundboard plus per-subscriber walk-on sounds. Not verified by me. | n/a | Likely (large, known tool; not verified) | Partial (per-viewer sound, no crowd scaling) |
| Streamer.bot Walkon Sounds (A+G, opened) | A, G | Opens | Extension: a custom entrance sound per regular, random pick from that user's folder. | Posted 28 Jun 2023, 5 likes | Streamer.bot is on the README list | Partial (named per-viewer audio; one-shot, no crowd, no scaling) |
| VoxBooster emote-soundboard guide | C | Opens | Guide to a hand-triggered emote soundboard (KEKW laugh on F9); FAQ: "trigger these clips via hotkeys". | 12 Jun 2026 | No | Adjacent (manual, not chat-driven) |
| Plus 2 (Firefox) | C | Opens | Streamer chat tools: highlight messages, a chat-excitement gauge from keywords/emotes, yes/no polls. Visual only. | **1 user**, 0 ratings, v3.3.8, updated 24 Nov 2025 | No | Adjacent |
| Chat Decoder (Ex Machina) | C | Opens | Real-time chat analyser with a "Hype Meter" shown as a progress bar; used at Summer Game Fest/E3-type shows. No audio mentioned. | No numbers | Used at big events, no counts: unverified | Adjacent (visual) |
| Crowd Sounds app | C | Opens | Soundboard of applause, laughter, gasps, boos, chanting; mix and record loops. No chat link. | No counts | No | Adjacent (right sounds, no chat) |
| Elgato "Popular Sounds" pack | C | Opens | Stream Deck pack with Sitcom Laugh Tracks 1-3 and Applause, fired by a key press. | v1.1, 12 Mar 2026 | Yes (Elgato) | Adjacent (manual) |
| Meld Emote Storm (A+G+C, opened) | all | Opens | "The storm scales with how active chat is"; sound only via Meld Spark prompt. | No usage numbers | Meld is not on the README list | Partial (chat-scaled, visual) |

**Novelty re-search (Studio Audience):** three searches. Not found closer. Closest in spirit: Meld Bubbles/Fart Counter (chat-summoned, no scaling crowd), goldzulu twitch-avatars (a sprite per chatter with an `!audio` command), Seatlings (Etsy overlay where viewers walk in as critters and sit; no laugh audio). None mixes a crowd by distinct reactors.

**Signal links**

| Signal | Link | Status |
| --- | --- | --- |
| Sound Alerts "restrict a specific user" feedback | feedback.soundalerts.com/p/restrict-a-specific-user-from-using-sound-alerts | Opens. 3 Mar 2022, 7 votes, status Completed: a streamer wants to block one viewer who spams Sound Alerts. (A specific-user request, not a general "too annoying" post.) |
| VoxBooster counter quote | voxbooster.com/blog/soundboard-meme-audios-twitch-chat-emotes/ | Opens. Quote confirmed: "Firing KEKW audio every single time the emote appears turns a comedic tool into repetitive noise." |
| Dexerto: streamer rage-quits over lurker chat (Aug 2018) | dexerto.com/entertainment/emotional-streamer-rage-quits-... | Opens. 16 Aug 2018: a ~13k-follower partner ended a We Happy Few stream angry that viewers lurked. |
| Reddit sound-alert spam / "things you despise" | reddit.com/r/Twitch/comments/180wg5v/... | Unverifiable (Reddit) |

---

## 8. Hint Jar

| Competitor | Found by | Link status | What it actually does | Activity / popularity | Well-known? | Proposed overlap |
| --- | --- | --- | --- | --- | --- | --- |
| Universal Hint System (UHS) | C **(snippet)** | Wikipedia page not fetchable (connection refused); a search confirms the page: created by Jason Strautmann in 1988, hint files read in a reader app, hints in sequence | Offline tiered hints for games, revealed in order. Not live, not viewer-made. | Long-running format | Not by README measures (no counts) | Adjacent (the tier idea, not the live Twitch loop) |
| Chat Curtain (Chrome ext.) | C | Opens (listing site) | Client-side: "active mode" shows only mod-approved chat messages (mods add a checkmark). Only people with the extension see the effect. | **14 users**, v1.0.5, 12 May 2023 | No | Adjacent (mod gate, public chat, no tiers, no streamer-controlled reveal) |
| evils_presley paid backseat window | G | Opens (TwitchMetrics) | Channel with 2,299 followers; titles on 15, 17, 21 Oct 2026 say "NO SPOILING PLZ" and "[backseating costs 5 dollars]" on a Sekiro first playthrough. | 27-38 avg viewers | No | Adjacent (a social rule with a price, no tool) |
| nobackseating.carrd.co (C, opened for context) | C | Opens | Etiquette page: unsolicited hints are backseating; ask first; no tiers or nudges concept. | n/a | No | Adjacent |
| LeagueBackseat (A+G+C) | multiple | Opens per Claude/Astra (Grok could not find it) | Bot where viewers queue timestamped backseat messages. 0 stars, 37 commits. | tiny | No | Partial |

**No Hint Jar-like tool found.** A search for tiered-hint Twitch tools returned only Contexto On Stream (mods trigger a hint command in a word game), Battle of the Chat and Heads Up Phones Down. None has private tiered hints.

**Signal links**

| Signal | Link | Status |
| --- | --- | --- |
| Steam "Backseating problem" (Limbus Company) | steamcommunity.com/app/1973530/discussions/0/597397269594002793 | Opens. Posted 5 Apr 2025, 13 comments. Complaint is confirmed (backseating pushes people from streams; spoilers). Replies mostly say the fix is rules, timeouts, bans or member-only chat. Counter-signal confirmed. |
| StreamHub guide on spoilers/backseating | streamhub.world/streamer-blog/strategy/1199-... | Opens, dated 15 Mar 2026. Describes four play styles (blind: no hints; "gentle nudge" when stuck; collaborative; interaction fan). It does **not** state that backseating is "one of the most frequent" problems, so the summary's wording is stronger than the page. |
| Sportskeeda: Elajjaz on God of War hints | sportskeeda.com/.../i-will-legit-mute-voices-... | Blocked (405) |
| Reddit puzzle/blind-run threads (Astra) | reddit.com/r/Twitch/comments/1hrdn3o/, .../1av5gyy/, .../11rc3t7/ | Unverifiable (Reddit) |
| X posts (Grok) | x.com/lilmochis/... etc. | Unverifiable (X) |

---

## Changes to the merged picture

**Dropped / not counted (link failed or unverifiable, README rule):**
- PROVE IT (VAR, Astra snippet): Devpost blocked, nothing found elsewhere. Not counted. This was the only item that could have raised VAR's level, and it has no verified content.
- Raid Train (Raid Torch, Astra): Devpost blocked, not in the Twitch hackathon recap. Not counted.
- Twitch Sense (Studio Audience, Astra): Devpost blocked, the 2017 recap lists no such project. Not counted; the 2017 date is doubtful.
- Twitch Storm: kept only as a **(snippet)**, BusinessWire blocked.
- ViperVex (Tap) and RTS Action Replay (VAR): could not be opened (429 and X). Kept as unverified Adjacent/Partial.
- Blerp walk-on (Studio Audience): site blocked; kept as unverified Partial.

**Overlap levels:** no level was raised to Same core loop. Verified single-source items sit at Partial (Fyre, Glitch, BarRaider, Senchabot; Muted Notification, Remember to Talk, Audio Source Mute Indicator; Blabla, obs-popup-overlay; Walkon) or Adjacent.

**New or closer than before:**
- RaidPort (raidport.tv opens): the raid-wheel game show now has a real page. It is a hub-and-wheel format with a per-raid Portal Charge. I rate it Adjacent to Raid Torch (different input and output); it is in alpha/beta, not shipped.
- Streamer's Court (Steam, 2022): chat-jury verdict game, new for VAR, Adjacent, no replay.
- Muted Notification (12.4k downloads) and Remember to Talk (2.4k downloads) are well-known, partial coverage of Tap's OBS-mute input. Neither involves viewers, mods or a confirm loop.
- tomaae replay (12.6k downloads, but last updated 2019) is the well-known chat-called replay for VAR; it is Partial.

**Summary statement for the user:** the six remaining cards have no Same-core-loop competitor after the check. The cards' claimed differences stand as written. For Hint Jar, the demand source "backseating is the most frequent problem" is not supported by the one guide page I could read, and the Limbus Steam thread's replies lean towards rules and bans rather than a tool.

**Unverifiable in this check:** all Reddit links (the tool cannot fetch reddit.com), all X posts, Devpost (403), BusinessWire, GameDev.net (403), Sportskeeda (405), esports.gg (403), Blerp (403). They should not be treated as dead.
