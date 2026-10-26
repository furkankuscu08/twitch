# B: Twitch culture and needs (wave 1)

Researched 2026-10-25. No product ideas here, by design.

**Labels:** [V] verified (I read the source, or a primary doc) | [S] search snippet only (not opened) | [I] inference | [U] unknown.

**Access limits, read these first:**
- reddit.com and old.reddit.com are blocked for my tools. Mirrors 404'd. **I read zero r/Twitch, r/Twitch_Startup or r/streaming threads.**
- twitch.uservoice.com returned 403. web.archive.org is blocked.
- The TwitchDev forum is snippet-only.
- Several academic pages (par.nsf.gov) refused connections. I saw abstracts only.
- So the evidence below is peer-reviewed abstracts, press, Twitch docs, and vendor blogs. Vendor blogs sell tools, so I discount them.
- "Not found" is not "does not exist". The Reddit gap matters most for the pain-point rows.

## 1. Primer

### Scale (who we resemble)
- [S] Secondary sites say about 95% of channels average 0-5 concurrent viewers. They conflict with each other and trace to old data. Never traced to a primary source: https://www.streamscheme.com/twitch-statistics/ [V] says only that the average is 26 viewers per channel and "the large majority" sit below it (Jan 2026 data). Treat "most channels are tiny" as likely [I]; treat 95% as unverified.
- [V] Our demo (one streamer plus a few accounts) looks like a typical channel. It does not look like the channels judges watch.

### Roles
Motivations are mostly [I] from domain knowledge. Sources are cited where they exist.
- **Streamer:** wants an audience, income, or just company. Small streamers split between "career" and "for fun" [V] (https://www.boardtownunbound.msstate.edu/entries/2025/09/inside-world-twitchs-small-streamers-emily-kellum, 2025, n=3 student interviews, anecdotal). Also cares about safety: doxxing and swatting fears appear in the same piece.
- **Moderators:** volunteers, usually friends or regulars. Reasons given: loyalty to the streamer and community. The work blends emotional labor and fun. Much of it is invisible: coordinating, quietly applying sanctions [S] (Wohn CHI 2019, n=20; Cai/Wohn/Almoqbel 2021, n=21 [V abstract]; Cai/Wohn CHI 2022, n=40 [V abstract]).
- **VIPs / subscribers / regulars:** status and belonging. Badges, emotes and in-jokes mark membership. Roles differ in chat limits: the IRC rate limit is higher for broadcaster, mod and VIP [S] (dev.twitch.tv chat docs). I could not open Twitch's roles help page (404).
- **Lurkers:** the majority of viewers. They watch without chatting, often as background while working or cooking [V] (https://indiecator.org/2021/03/02/lurking-on-twitch/, an opinion post). Twitch has said lurkers are legitimate viewers [V] (Dexerto, below).
- **New viewers:** Twitch's own claim is that people who chat on a first visit are 50% more likely to return, and viewers are most engaged in the first and last 15 minutes [V, but Twitch's self-reported stat] (https://www.twitch.tv/creatorcamp/en/level1/establish-your-brand/engaging-viewers).

### Small versus large
- [V] Large chats move too fast to read; users coordinate through repeated emotes and acronyms ("crowdspeak") [S] (Ford et al., CHI EA 2017, 10k+ concurrent viewers).
- [V] Shroud, 2026-09-30: channels of 200-400 viewers get much less chat than a decade ago; a silent chat is "very depressing"; larger streamers are less affected (https://www.dexerto.com/twitch/shroud-says-streaming-in-2026-is-depressing-as-fewer-viewers-interact-in-chat-3414260/). One prominent streamer, not a survey.
- [S] Lurkers feel more conspicuous in a 5-viewer channel, so calling them out backfires (creatorhandbook snippet; indiecator [V] agrees).
- [I] At 0-50 viewers the problem is scarcity of participation. At large scale it is volume and moderation.

### Rituals and conventions
- **Emotes:** a shared language. Third-party emote sets (BTTV/7TV) exist [I, not sourced]. Twitch removed PogChamp on 2021-01-06 and viewers elected a replacement [V] (Wikipedia).
- **Commands:** `!` commands from bots such as Nightbot or Moobot answer FAQs and run minigames [I].
- **Raids:** at stream end, a streamer sends viewers to another channel. Hosting was removed May 2022, so raids are now the only native audience-sharing [S]. Etiquette: raid same-size or smaller channels; never beg for raids [S, vendor guides]. Raids can be abused ("hate raids"), so streamers use follower-only chat during raids [S].
- **Hype trains / channel points / predictions / polls:** Hype Train celebrates sub/bit contributions; predictions let viewers wager channel points; Twitch markets these as engagement features [S] (Twitch Creator Camp, 2021 dev blog). Twitch claims up to a 13% chat-participation lift from channel points; self-reported [V].
- **Clips:** short highlights, increasingly re-edited vertically for TikTok [S] (Twitch Clip Editor, May 2023).
- **"Chat plays":** Twitch Plays Pokemon (Feb 2014, 60-70k concurrent) is the archetype [V] (Wikipedia). Known failure modes: trolls, 20-40s input lag, and chat-system overload [S].
- **Backseating:** unsolicited gameplay advice. Many channels ban it by rule. Gray area: warning about an imminent mistake [S] (community guides, not Twitch policy).
- **Copypasta:** a chat-wide pasted joke. [U] I found no sourced treatment.

### Categories
Direct cross-category comparisons of chat rate or retention were not found [U]. The below is mostly [I].
- **Just Chatting:** biggest category by hours since 2020 [S]. The talk itself is the content, so chat is the main show.
- **Games:** chat reacts to gameplay. Backseating and spoilers are the friction. Many games offer no way for chat to influence play [S] (Saarland "StreamersHell" paper).
- **Music:** copyright dominates. 2020 terms barred DJ sets/covers; enforcement moved from muting to removal [S]. Audible Magic mutes VOD segments [S].
- **Art/Creative:** copyright also applies to art [S]. [U] No engagement evidence found.
- **TTRPG:** D&D Beyond ran a Twitch overlay extension in 2018 [V]. DougDoug ran a 6-hour chat-controlled D&D-like game [S]. Chat-vote and chat-XP D&D formats exist but are niche or forum-sourced [S].
- **IRL, Science/Education:** [U] no sources found. IRL's known concerns (safety, TOS) are [I] only.

## 2. Needs table

Evidence strength: strong = multiple independent sources or peer-reviewed; medium = one credible source or dated; weak = vendor/anecdote/snippet. "Solvable by us" means via chat, overlay, API or EventSub.

| # | Need | Who | Context | Evidence strength | Solvable by us? | Source |
|---|---|---|---|---|---|---|
| 1 | Quiet or empty chat demoralizes the streamer; pressure to "perform" | Streamer, small to mid | 0-400 viewers, all categories | medium: one prominent streamer, 2026 [V]; opinion posts | Partly. Can lower the friction to join in. Cannot create viewers. Workaround today: narrate aloud, address "chat" as a whole | Dexerto 2026-09-30 [V]; indiecator [V] |
| 2 | Small channels are hard to discover; directory is "top heavy" | Streamer, new | Directory sorted by viewers | weak-medium: 2022 press [V]; Substack n=1 unverified (2025-04-15); stats conflict | No: Twitch must change. Workaround: post clips to TikTok/Shorts (vendor-claimed, [S]) | https://www.invenglobal.com/streamers_ent/articles/17521/this-twitch-update-that-could-dramatically-improve-discoverability-for-smaller-streamers [V]; https://drmandisa.substack.com/p/twitch-is-suppressing-small-streamers [V] |
| 3 | Moderation load: spam, harassment, hate raids | Streamer (esp. LGBTQ+/Black), mods | Any size; spikes during raids | strong that it exists (CSCW 2023 hate raids; studies of 20-240 mods) [S/V abstracts] | Partly. Twitch ships AutoMod, Shield Mode, Shared Ban Info, Suspicious User detection [V: API list]. Workaround: 6s delay, links off, dedicated report mods [S]. Hard to demo without real attackers | https://dspace.kaist.ac.kr/handle/10203/314820 [S]; https://www.pcgamer.com/uk/after-a-flood-of-hate-raiding-twitch-responds-to-calls-to-do-more-for-marginalized-streamers [S] |
| 4 | Mods' work is invisible and needs coordination and shared standards with streamers | Moderators | Teams of volunteers | strong (several peer-reviewed studies, abstract-only) | Possibly. Tooling for notes/handoffs is not found in my sources. The need is inferred from abstracts [I] | https://digitalcommons.njit.edu/fac_pubs/2997 [V]; https://digitalcommons.njit.edu/fac_pubs/4032 [V] |
| 5 | Streamer cannot read or answer chat while playing or performing | Streamer | Games, music, art, any multitasking | medium-weak: old forum threads, Streamlabs guide [S] | Yes in principle (overlay/chat/EventSub). Workarounds: second monitor, phone, a mod reading chat, narrating. They fall short with one monitor or no mod | OBS forum threads [S]; Streamlabs content hub [S] |
| 6 | Large chat is unreadable | Viewer | 1k+ viewers | weak: student survey of 49 [S]; academic "crowdspeak" [S] | Mostly no: chat rendering is Twitch's. Viewers use third-party browser tools [I] | https://mlenguaespejo1398.myportfolio.com/readability-for-twitch-chats [S] |
| 7 | New viewers lack context (lore, in-jokes, running bits) | New viewer, streamer | Channels with long history | weak: blog guidance [S]; Twitch's retention claim [V, self-reported] | Yes, on-stream. Workaround: panels, pinned message, explain in speech. Short of what is needed because regulars repeat jokes | https://streamhub.world/streamer-blog/strategy/3558-turning-one-time-viewers-into-recurring-subscribers-best-engagement-practices/ [S]; Creator Camp [V] |
| 8 | Low-effort participation for viewers who won't type or pay | Lurker | Any size | weak-medium: Tampere survey n=28 [S]; Twitch stats [V, self-reported] | Yes via chat commands and overlays. Channel points are gated (see 9) | trepo.tuni.fi/handle/10024/238676 [S] |
| 9 | Channel-points-based mechanics are unavailable to most channels | Small streamer, builders | Non-Affiliate | **strong for the gate [V]**; the size of the unmet demand is [U] | We can't use it unless the demo channel is Affiliate. API returns 403 "not a partner or affiliate" for custom rewards, Power-ups and charity. Polls/predictions: no such gate in the API doc text I grepped; Twitch's 2021 blog says Partners and Affiliates [S]. [U] confirm | https://dev.twitch.tv/docs/api/reference/ [V, 2026-10-25] |
| 10 | Chat-controlled play gets griefed and lags | Streamer, chat players | "Chat plays" formats | strong historically (TPP 2014) [S/V]; modern data [U] | Yes; it is a design problem, not a platform problem | Wikipedia [V]; mcvuk, jgeekstudies [S] |
| 11 | Fake viewership and unfair flagging | Streamer, lurkers | Aug 2025 viewbot crackdown | strong that the event happened [V]; Twitch denies a viewership decline | No: Twitch policy | https://www.tubefilter.com/2025/08/27/twitch-viewbot-crackdown-zach-bussey/ [V] |
| 12 | Turn live moments into shareable short clips | Streamer | Growth workflow | weak: vendor blogs claim ~45 min per clip [S]; Twitch Clip Editor exists since 2023 [S] | Partly. API has Create Clip, Create Clip From VOD, Get Clips Download [V: API list] | https://blog.eklipse.gg/ [S, vendor] |
| 13 | Music streamers face DMCA risk and VOD muting | Music streamer | 2020-21 takedown waves | medium, dated [S] | No: licensing and Twitch policy | https://twitch.tv/creatorcamp/paths/getting-started-on-twitch/copyrights-and-your-channel [S] |
| 14 | Accessible captions and chat for deaf, hard-of-hearing, blind and screen-reader users | Viewer | Any | weak-medium: Inverse snippet [S] | Partly | https://inverse.com/input/gaming/twitch-hasnt-kept-its-promises-to-disabled-streamers [S] |

**Developer-side friction** (for planning, not a user need): a CHI 2024 study of 2,179 messages from a Twitch developer Discord (Oct 2018 to Apr 2023) reports extension review waits from about 2 days to "5 months", API migration churn, unreliable whispers, and opaque anti-spam rules. Streamers were not interviewed [V] (https://arxiv.org/html/2401.11317v3). Rules in this hackathon confirm Extensions take 5-14 days [V].

**UserVoice signal [S only]:** Jan 2024 press says the top-voted ask was a bigger sub revenue share (21,000+ votes). July 2024 press says 9 of the top 10 were about reversing the mobile redesign (https://sportskeeda.com/us/streamers/news-remove-tiktok-aspects-users-flood-twitch-forums-requests-roll-back-tiktok-like-features-mobile-app). I could not open UserVoice. Both asks need Twitch to change, and votes are a signal, not a verdict.

## 3. Viewer-side versus streamer-side

**Viewer-side:**
- Unreadable large chats (row 6)
- Missing context as a newcomer (row 7)
- Participation without paying or typing (row 8)
- Accessibility (row 14)
- Fake counts hurting trust (row 11)
- Chat-play griefing (row 10)

**Streamer-side:**
- Silent chat (row 1)
- Discovery (row 2)
- Moderation and safety (rows 3-4)
- Reading chat while busy (row 5)
- Clip workflow (row 12)
- Copyright (row 13)
- Feature gating by Affiliate status (row 9)

## 4. Checks on the stated hypotheses

- **"Affiliate/Partner-only features are unavailable to us":** [V] true for custom rewards, Power-ups and charity APIs (403). [U] for polls and predictions, which should be checked on a test account. Affiliate thresholds in my snippets (50 followers, average 3 viewers, 500 minutes, 7 days within 30) come from a third-party blog [S], so confirm on Twitch before relying on reaching Affiliate by Nov 2.
- **"Judges mostly judge from the video":** consistent with rules, which say judges "are not required to test" [V, rules.md]. Rules also allow automated AI analysis [V].
- **"Many entrants build the organizer's examples":** not tested here.
- **Evidence against a dead-chat thesis:** the strongest voice is one big streamer, and lurkers are defended as legitimate viewers by Twitch and by opinion writers. Treat "dead chat" as a real feeling but not proven demand.

## 5. Stopping note
Further searches on moderation, discovery and quiet chat mostly repeated the above, so I stopped. Unsearched or unreachable: Reddit, UserVoice, a roles/VIP help page, category-level chat metrics, IRL/Science.
