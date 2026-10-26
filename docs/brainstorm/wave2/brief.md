# Wave 2 brief: idea generation

This brief is self-contained. Every idea agent receives the same text, followed by one lens block from prompts.md (deleted; in commit b282398).

---

## 1. The competition

**Codex x TwitchCon Hackathon** (Devpost). Deadline: Nov 2, 2026, 14:00 PT. About 565 registered participants. Based on past submit rates, we expect ~30–70 actual submissions (low-confidence estimate). The top 5 are shown at the Codex booth at TwitchCon San Diego.

**Brief from the organizers:** "Build something streamers and their community on Twitch could really use." The project must be an interactive experience that connects to Twitch (chat, overlay, Twitch API, EventSub, or Extension), be built with OpenAI Codex, and be newly created after Oct 23, 2026. The organizer's examples are explicitly "starting points, not templates":
- streamer collaboration
- audience participation (Twitch Plays, live polls, streamer distractions)
- content enhancements (tabletop dice roller, live sports overlay, IRL or science-stream tools)

**Judging:** four equally weighted criteria. Ties are broken by Innovation first.
1. **Innovation / Idea:** Does it differ from existing concepts?
2. **Potential Impact:** Is it useful or entertaining for streamers and their communities?
3. **Technical implementation:** How well does it use Codex?
4. **Design:** Is it easy to use and fun to watch?

Judges are not required to run the project. They mostly judge the **video, under 3 minutes**, which must show the project working on Twitch and how Codex was used. They also see the description and the repo. AI-assisted screening is possible. Runtime use of Codex or an LLM is **not** required.

## 2. The builder

- **Solo.** About 9–10 hours of building, done by directing many AI coding agents in parallel, plus ~4 hours for the demo video.
- Strong in Python/FastAPI/Docker/Redis and ML. Open to any stack (a web overlay is HTML/JS anyway). LLMs are available via OpenRouter.
- **New to Twitch, with no audience.** The demo channel will have one streamer plus 2–3 test accounts typing in chat. The video can be scripted with these real accounts.
- Do **not** steer toward ML or LLMs because of the builder's background. Use them only where they are clearly the best tool.

## 3. Hard filters

An idea must pass all of these. Breaking one is not deletion: put the idea in the "Parked" section of your output and say what would need to be true.

- No Twitch Extension (review takes 5–14 days).
- Does not need Affiliate/Partner features. Polls, predictions, and custom channel-point rewards *might* work on a new channel since Twitch's May 2026 "Monetization for All" change, but the API docs still say affiliate-only. This is untested, so these can only be a bonus.
- The core experience works with chat + OBS browser-source overlay + EventSub + Helix API.
- Tolerates 2–30 seconds of viewer-side stream latency. Real-time feedback must happen on the streamer's side or in chat, not depend on viewers reacting to frame-exact video.
- Does not require storing Twitch content longer than 24 hours (Developer Agreement). Sending chat text to an LLM is a grey area: allowed, but flag it.
- Convincing in a demo with 1 streamer + 3 test accounts. It is even better if it is *designed* for small channels, since most channels are small.
- Buildable in ~10 agent-assisted hours to a demo-quality MVP.

## 4. What Twitch gives us

| Surface | Notes |
| --- | --- |
| Chat | Read via EventSub `channel.chat.message`. Send via Helix Send Chat Message. A bot that is a moderator gets 100 msgs/30 s. Whispers exist. |
| EventSub (WebSocket) | 79 event types, none affiliate-gated in docs: follows, raids, shoutouts, chat, stream online/offline, channel updates, ad breaks, Shared Chat sessions, and more. No public URL needed. |
| Helix API | Clips, stream markers, raids (start/cancel), shoutouts, chat settings, pinned chat (new), user and channel info. |
| Overlay | An OBS browser source: any web page, composited on the stream. Must stay small and must not cover the content. |
| New or underused (2026 changelog) | Pinned Chat API, Custom Power-Up EventSub, GIFs in chat. |
| Not available on a new channel | Ads, charity, subscriptions, stream delay. Power-Ups are uncertain. |
| Testing | Twitch CLI can mock many EventSub events, but not chat, follow, or channel.update. Chat is tested with real accounts. |

## 5. Evidence digest

Labels: **[V]** verified, **[S]** secondary or snippet, **[I]** inference.

### Needs

1. **The streamer cannot read or answer chat while playing or performing.** Causes: single monitor, games that block overlays, VR, deep focus. This is the most consistent need across three independent sources (culture research, ~17 Reddit posts, ~8 X posts) [V]. Current workarounds: a second screen, a friend reading chat aloud, DIY Streamer.bot alerts. Yet a "chat woke up" signal is still crude.
2. **"Dead chat" discourages small streamers.** The feeling is real and is the biggest X cluster [V]. But viewers push back: "I don't watch for chat", "don't shame lurkers". Overlays that try to make chat talk get comments like "nobody plays them, even in 30–40 viewer chats" [V]. Arguing "revive chat" alone is weak. An idea here must respect lurkers and explain why people would actually engage.
3. **New viewers feel excluded** by clique chats and inside jokes they don't get. A 169-point Reddit thread, also found in culture research [V].
4. **Moderators can only act through public `!commands`.** They have no private control surface for running the show [V, Reddit].
5. **Automated bot spam annoys new viewers** [V, Reddit].
6. **The streamer cannot filter their own chat view** (focus on questions, new chatters, etc.) [V, Reddit].
7. **Multi-platform chat** (unified, styled, repliable). Demand is real, but so is the tool supply. The missing piece is quality: animation, big emotes, replying [V].
8. **Clip workflow** (marker to clip, highlights). Weak–medium evidence [S]. Twitch named "AI-assisted clips and highlights" a 2026 priority [V].
9. **Production quality matters more than gimmicks.** The top "small streamer" post (3.5k points) blames bad audio, long starting screens, and overlays covering 40% of the screen [V].
10. **Customization is a hobby.** "Nobody talks but I spent 5 hours on my chat overlay, it's so fun" [V].

### Mechanisms from other platforms

- **Per-channel identity or status earned by watching or participating** is the most repeated pattern: Kick Level Up and Daily Rewards, Bilibili fan medals, TikTok Fan Club, CHZZK watch-time points and top-5 watcher badges [V]. On Twitch, status exists mainly through paid subs. Twitch users on X explicitly envy Kick's Level Up [V]. Proven love for free versions is thin.
- **Q&A mode** exists on YouTube Live. Twitch has no native equivalent [V].
- **Locked-in predictions with a reveal of what others picked**, viewer voting on control rules, danmaku-style chat over video. Success evidence is weak or old [S].
- **Paid-gift battles and gift-triggered game effects** need crowds and money, and already exist on Twitch (Crowd Control, TikFinity) [V]. They are a poor fit.
- **Raids** are valued as social discovery and a "handoff". Korean users who left Twitch miss raids, clips, channel points, and follow thank-yous [V].
- **Hype cycles:** HQ Trivia, Fan Controlled Football, and Chinese danmaku games rose fast and saturated [S].

### Twitch's direction (sponsor lens)

- **2026 priorities:** monetization, vertical and dual-format streaming, AI-assisted clips and highlights, discoverability, moderation [V].
- The CEO's red line on AI is **AI replacing the streamer**. AI that empowers streamers is aligned [V].
- **Codex usage is a judged criterion.** OpenAI's own Build Week write-up praised "building outside your expertise" and "turning domain knowledge into a working workflow" [V]. The video should show Codex usage visibly: plan mode, AGENTS.md, subagents, tests, `/review`.

### Competition landscape

- Every common job already has a free owner: alerts and overlays (StreamElements, Streamlabs), automation (Streamer.bot, Mix It Up, SAMMI), chat bots (Nightbot, Moobot), paid viewer effects (Crowd Control, Sound Alerts) [V].
- AI co-host is an active commercial space (ai_licia, Streamlabs Intelligent Streaming Agent, Neuro-sama) [V].
- **Past Twitch hackathon winners** (2018–2024) were niche, often solo, sometimes prototype-level, with 2–3 minute videos. Several had **physical or non-chat outputs**: a water pump, LEDs, a lights-off game [V]. This describes them; it does not explain why they won.
- The 2024 gallery was full of dice, polls, bingo, trivia, and AI chat projects. The winners were niche [V].

### Crowded areas

These are not banned, but they need a meaningful difference that changes the experience:
- alert and overlay tools
- viewer-paid game effects
- AI chatbot or co-host
- dice, polls, bingo, trivia
- classic "Twitch Plays"

## 6. Your output

Write **one markdown file** (path given in your lens block), max ~3500 words, in this order:

### A. Crowd map
List the ~10 ideas you expect most of the 565 participants to build, given this brief and the organizer's examples. One line each.

**These are not banned.** The map is a reference for judging novelty later. An idea that starts from a familiar base is allowed if it states the twist and passes the test: *"Would a judge who has already seen five entries like this still remember this one?"* At most 2 of your 5 full cards may start from a crowd-map idea, and they must be labeled `Familiar base: <which>`.

### B. Wide list
At least **15 one-line ideas**, numbered. Tag each with its main need or mechanism (e.g. `need #1`, `Kick Level Up`, `raid`). Go wide. Include odd and risky ones; they will be filtered later.

### C. Five full cards
Pick your best 5 from the wide list and write each with this template:

```
### <Name>
- One-liner:
- Who installs it / who gets the value (streamer, viewers, mods — separately):
- Streamer category fit:
- Core loop (what the viewer does → what happens on screen):
- First 10 seconds of the demo (what a judge sees):
- Twitch surfaces used:
- Works with 1 streamer + 3 test accounts? How?
- Closest existing thing and the meaningful difference:
- Why wouldn't 30 other teams build this?
- Evidence it links to (section 5 items), or "unvalidated — how we'd validate":
- MVP scope / explicitly out of scope:
- Riskiest assumption:
```

### D. Parked
Good ideas that break a hard filter. One line each, plus what would need to be true.

### E. Your pick
One short paragraph: which card you would build, and why.

## 7. Rules

- Label claims: verified / inference / unknown. Do not invent evidence. "Unvalidated" is acceptable if labeled.
- An idea is not stronger because it uses AI. Twitch's red line is AI that replaces the streamer.
- Prefer one sharp, demoable core loop over a platform with many features.
- Work independently. Do not read other agents' wave 2 outputs. Do not write code. Do not spawn agents.
