# D. Landscape: what exists on Twitch, and the entry bar

Compiled 2026-10-25. No ideas proposed. Labels: **[V]** verified (I read the source page), **[S]** only a search snippet or a vendor/aggregator claim, **[I]** inference, **[U]** unknown. "Fetched" means the page was opened on 2026-10-25. Tool "gaps" are my reading of what the source does not say, so they are [I].

## 1. Tools by job-to-be-done

| Job | Tool | Covers | Strength | Gap (inference) | Source |
|---|---|---|---|---|---|
| Alerts, overlays, tips | StreamElements | Chatbot, alerts, overlays, widgets, themes, tipping, merch, sponsor deals [V] | Free, large template library | Homepage lists no AI features [V] | https://streamelements.com/ (fetched) |
| Alerts, overlays, tips | Streamlabs Desktop | Alerts, overlays, tipping, merch [S meta description only; page body empty to my fetch] | Bundled with the encoder | Not assessed beyond the Agent row | https://streamlabs.com/ |
| Viewer-paid interactions | Sound Alerts | Soundboard extension paid in Bits or Channel Points; TTS, tipping, widgets [S/V] | Twitch-native monetization | Bits pricing only for Partner/Affiliate (vendor help page, snippet) | https://soundalerts.com/ (fetched); https://support.soundalerts.com/article/twitch-extension (snippet) |
| Viewer-paid interactions | Crowd Control | Viewers trigger effects in "250+" games, plus overlays, keyboard/mouse, sounds; pay via Bits or Channel Points [V] | Deep game integrations; featured in Twitch showcase | In-game effects need per-game integration [V] | https://crowdcontrol.live/ (fetched) |
| Viewer-paid interactions | Tangia | Purchasable viewer interactions, TTS, memes [S aggregators only] | Unverified | Unverified | https://sourceforge.net/app/tangia/web-app/ (snippet) |
| Automation hub | Streamer.bot | Trigger-to-action engine, C# scripting, multi-platform chat, OBS/Stream Deck/Crowd Control and 20+ integrations [V] | Most flexible for builders | Builder-oriented (inference) | https://streamer.bot/ (fetched) |
| Automation hub | SAMMI | Visual button programming, OBS control, Twitch events, viewer-triggered buttons via extension, community extensions (loyalty, wheel, TTS) [V] | No-code; extension ecosystem | Needs local app | https://sammi.solutions/ (fetched) |
| Automation + bot | Mix It Up | Commands, alerts, overlays, moderation, giveaways, viewer currency; "133 features, 43 integrations" [V] | Broad, free | Windows only per FAQ [S] | https://mixitupapp.com/ (fetched); FAQ via search snippet |
| Chat bot / moderation | Nightbot | Chat automation and moderation [V, meta description only; page needs JS]. Song requests, giveaways [S, blogs] | Cloud, free [S] | Unverified | https://nightbot.tv/ |
| Chat bot / moderation | Moobot | Moderation, timers, song requests, polls, raffles, subscriber rewards [V, homepage plus blog snippets] | Verified on Twitch; cloud [V] | Unverified | https://moo.bot/ (fetched) |
| AI co-host | Streamlabs Intelligent Streaming Agent | Voice-commanded producer, tech support, optional 2D/3D avatar, game-event automations; free tier 100 interactions [V] | Runs locally, tied to Streamlabs Desktop | Agent's platform list not stated [V] | https://streamlabs.com/intelligent-streaming-agent (fetched) |
| AI co-host | ai_licia | Hears chat and voice, speaks, memory across platforms, clips, polls, scene switching, moderation, 19 languages; Twitch extension and public API [V] | Mature feature set. "10,000+" users is a self-claim | Entrant-built chatbots compete with this directly (inference) | https://getailicia.com/ (fetched) |
| AI streamer | Neuro-sama | AI persona that plays games and talks to chat. Described as Twitch's most-subscribed channel (160k+ subs) in Jan 2026 [S, Tubefilter/TechRadar snippets] | Shows audience demand for AI personas | A single bespoke creation, not a product | https://www.tubefilter.com/2026/01/05/neuro-sama-vedal987-most-subscribed-hype-train-record/amp/ (snippet) |
| Twitch-native | Polls, Predictions, Channel Points, Hype Train, Guest Star, Shared Chat, Raids, Clips, Shoutouts | Endpoints exist for polls, predictions, rewards, Guest Star, Shared Chat session, pinned messages, conduits [V] | First-party; no install | Several are monetization-gated (see Q3 below) | https://dev.twitch.tv/docs/api/reference/ (fetched) |
| Extensions | GIPHY, Mobalytics, OP.GG, Pokemon Badge Collector, Live Bingo, Stream Together Timeline | Panels/overlays for media, stats, collectibles, games [V from showcase and 2024 gallery] | Per-use-case niches | No install-count ranking found [U] | https://dev.twitch.tv/showcase/ (fetched) |

Observations:
- Every job above has a free incumbent. Only the AI co-host row has a live market that is still being filled (Streamlabs agent, ai_licia) [I].
- I found no install-count ranking for Extensions (search returned none). "Popular extensions" is therefore [U].
- I did not check Kick or YouTube-only tools, Fossabot, Botrix, Lumia Stream, or Wizebot. Searches returned nothing on Botrix or Fossabot. Absence of evidence only.

## 2. dev.twitch.tv/showcase

- [V, fetched, summarized by a small model] 22 items, mostly extension or game-integration case studies and a few marketing or developer-tool pieces (my grouping). Named items include Blerp, Crowd Control, Genvid SDK, GIPHY, Pokemon Badge Collector, Sound Alerts, Muxy, Mobalytics, OP.GG, Curse Innkeeper, Fortnite quests, Twitch Drops, Devolver case study.
- Dating: the page has no publication date and a 2025 footer. The linked articles' URLs date 2017 to 2019 [V]. No AI, chatbot or EventSub projects. The showcase is stale [I], so it says little about the 2026 field.
- The organizers' hackathon resources page links it as "inspiration" (local file resources.md).

## 3. Past Twitch hackathon entries

All facts below are [V] unless marked. I do not infer why anything won. "Video" gives length and title only; I could not view video content.

| Name | Event | What it did | Demo style (observed) | Source |
|---|---|---|---|---|
| tcghud (Tangia team) | Streamer Tools 2024, category winner | Browser-run model identifies trading cards from camera, similarity search over ~200k cards, shows prices; OBS browser-source overlay | Devpost story with summary and motivation; YouTube demo 2:18 plus a 0:20 OBS clip | https://devpost.com/software/tcghud-by-tangia ; forum post https://discuss.dev.twitch.com/t/streamer-tools-hackathon-2024-winners-and-runner-ups/61823 |
| PixelWars | same, category winner | Viewers send named animated characters to fight another channel or a tower; Extension + FastAPI + JS overlay; solo | Emoji-sectioned write-up; YouTube 2:57 | https://devpost.com/software/bitwars |
| Stream Together Timeline | same, category winner | Timeline of Stream Together sessions and clips, panel plus webpage; solo | YouTube 3:18 | https://devpost.com/software/stream-together-timeline |
| Lights Out! | same, runner-up | Screen goes dark; viewers find a switch by cursor light; team of 4 | YouTube 2:39, plus a separate 12:32 Portuguese promo video | https://devpost.com/software/streamalertstv |
| Spectators Control Minecraft Mobs | same, runner-up | Minecraft mod: viewers buy mob control with Bits or subs | Video not checked | https://devpost.com/software/stream-mob-control-mod |
| Crowd Control Hype Train; Overlay Expert; Mix It Up overlays | same, $6k bonus (most authentications) | Features for existing products | Not checked. These were updates to existing apps, allowed there (forum rules post) | https://discuss.dev.twitch.com/t/streamer-tools-hackathon-2024-bonus-prize-winners/62948 |
| StreamRoll For Chat; Live Bingo + Stream Together; DVD Screensaver w/ Chat | same, $4k additional | 3D dice for chat; shared Bingo extension; bouncing chat messages | Not checked | same bonus post |
| Hydrate | Channel Points Hackathon 2021, winner | Channel Points redemption runs a water pump filling a cup on stream | Not checked | https://blog.twitch.tv/en/2021/04/16/winners-and-honorable-mentions-of-the-twitch-channel-points-hackathon |
| There's a Twitch Among Us; CastMate; Just Spinning | same, winner and runners-up | Among Us mod; rewards-to-Hue/OBS/sound mapper; viewer queue plus game wheel | Not checked | same |
| OK Gamers | TwitchCon Hackathon 2019, grand prize | Streamer says "OK gamers", speech recognition starts a chat poll and a pie-chart extension; Python backend with Azure speech | YouTube 0:27; also a session recording | https://devpost.com/software/ok-gamers ; https://blog.twitch.tv/en/2019/10/31/highlights-from-the-twitchcon-hackathon-2019 |
| Summon.tv; The Rundown; SubClip; Teams+ | same, mentions and challenge wins | Bits trigger Minecraft actions; new-viewer intro overlay; auto-clip sub shoutouts; Teams roles (prototype only) | Not checked | same blog |
| KnowClips; HandEmote; Twitchlight; StreamerTrivia; Twiffle | TwitchCon Hackathon 2018 (24 hr, 70 devs, 13 extensions) | Clip overlay; Leap Motion gestures; LED strip for subs; trivia (backend not usable by deadline); raffles | n/a | https://blog.twitch.tv/en/2018/11/20/twitchcon-hackathon-2018-b66ea6687032/ |

Patterns observed (inference, small sample):
- Winning demos I could time were 0:27 to 3:18, mostly 2 to 3 minutes. The 3:18 one would break this hackathon's under-3-minute rule.
- Several winners involved physical or non-chat output (water pump, LED strip, Leap Motion), and some were partial (StreamerTrivia backend, Teams+ prototype).
- Solo builders won categories in 2024.
- 2021 and 2024 winners were mostly game or overlay mods, not LLM products.

## 4. Signals about this hackathon

- [V] Hackathon page, Oct 25: "Participants (549)". The local overview.md snapshot says 473, so it is growing.
- [V] Project gallery (https://twitchcon-codex.devpost.com/project-gallery): "The hackathon managers haven't published this gallery yet". No entries are observable.
- [V] Updates tab: no announcements. Discussions tab: empty page. Participants list is login-gated, so teams and skills are [U].
- [U] TwitchDev Discord (#codex-twitchcon-hackathon): not accessible to me.
- [V] Search found no public write-ups of entries.

Base rates (for scale only):
- 2024: 894 participants, 53 gallery projects (counted across 3 pages), about 6%. Likes were mostly 0 to 6. [V]
- 2021: about 500 sign-ups, about 60 projects, about 12%. [V, Twitch blog]
- [I] 549 participants could yield roughly 30 to 70 submissions, low confidence. Top 5 finalists are about 7 to 15% of that.

Hypothesis checks:
- **H1, entrants cluster near organizer examples or generic AI bots.** [S/I] Partial support from the 2024 gallery, a different event with different prompts. It contained dice (StreamRoll), polls, giveaways, bingo and trivia, plus AI entries (ai_licia, BedrockStream, Chatlytics, chatcast, Infinite Murder mysteries, a voice-clone convo generator). Against: 2024 category winners were niche (card HUD, lights-out gag, Minecraft mod). For 2026, [U] until the gallery is published.
- **H2, judges mostly judge from video and description.** Rules say judges "are not required to test" [V]. The 2024 panel was 3 streamers and 3 Twitch staff [S, snippet of the forum thread]. 2026 composition is [U].
- **H3, Affiliate/Partner features are unavailable to us.** [V] The API reference returns 403 "not a partner or affiliate" for Create/Get/Update/Delete Custom Rewards, redemptions, Custom Power-ups and charity. Commercials, non-recurring schedule segments and Check User Subscription are partner/affiliate-only. A 2021 forum thread says the Twitch CLI can mock Channel Points [S]. Polls and predictions pages do not state this restriction [V], so Predictions gating is [U]. The chat docs state no affiliate requirement for bots reading and sending chat [V]; overlays are outside Twitch's gating (inference). Non-broadcaster bots get 1 message/second/channel unless moderator or VIP [V].
