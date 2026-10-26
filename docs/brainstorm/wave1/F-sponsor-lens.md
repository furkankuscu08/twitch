# F - Sponsor lens (OpenAI Codex x Twitch), as of 2026-10-25

Labels: [V] verified on a page read, [S] search snippet only, [I] inference, [U] unknown. Docs moved: developers.openai.com/codex/* now 308-redirects to learn.chatgpt.com/docs/*. Several third-party pages returned 403/404 (noted below). Scope: sponsor alignment only, no product ideas.

## 0. Hackathon facts already on file (competition/*.md) that matter for the lens
- [V] Criterion 3 is "How well is it built, and how well does it use Codex?"; video must show the project on Twitch AND how it was built with Codex; Codex session ID of the main build thread is required; rules say judging may use "automated AI-driven analysis" (rules.md s6, FAQ).
- [V] FAQ: free Codex tier is fine ("Free usage has limits... leave some headroom"); other AI tools allowed but "Your project must be built with Codex"; "Be ready to explain how your project works"; judges may judge on video/description only; Extensions take 5-14 days review (avoid).

## 1. Codex capabilities (as of Oct 2026)

| Capability | Surface | Date | What it shows in a demo/write-up | Source |
|---|---|---|---|---|
| CLI (current 0.164.0: /presets, mid-response steering, /daemon) | Terminal | 2026-10-23 [V] | Visible terminal transcript; slash commands (/plan, /review, /resume) | https://learn.chatgpt.com/docs/changelog |
| Desktop app (Codex inside ChatGPT desktop; composer predictions, Changes panel, review of GitHub PRs) | macOS/Windows app | app 26.1007 on 2026-10-08 [V]; fold-in to ChatGPT app July 2026 [S] | Diff/Changes panel is a good screen-recordable "how it was built" | https://learn.chatgpt.com/docs/changelog |
| Surface list: CLI, IDE extension, Cloud/web, mobile, SDK, App Server, GitHub Action + integration, MCP, AGENTS.md, Skills & Plugins, Subagents, Code review | all | undated page [V] | Breadth menu; none dated individually | https://learn.chatgpt.com/docs |
| Subagents (explorer/worker/default; custom TOML agents in ~/.codex/agents) | CLI/app | GA 2026-03-16 [V] | Parallel agents on one task | https://simonwillison.net/2026/Mar/16/codex-subagents ; CLI 0.161/0.162 notes on changelog |
| Skills (SKILL.md), required env skills enforced | CLI/app | 2026-10-08 [V] | Reusable project-specific workflow | changelog URL above |
| AGENTS.md ("open-format README for agents") | repo file | best-practices page, undated [V] | Committed file proves durable guidance | https://learn.chatgpt.com/docs/learn/best-practices |
| Code review (/review, cloud auto review on Plus) | CLI/GitHub/cloud | 2026-10-08 [V] | Self-review step before accept | changelog; https://learn.chatgpt.com/docs/pricing.md |
| MCP (tool-search default when supported) | CLI | 2026-06-25 [S] | External system access from the agent | https://www.havoptic.com/tools/openai-codex (third-party tracker) |
| Codex SDK (TypeScript `@openai/codex-sdk`, Python `openai-codex`), start/resume threads | programmatic | undated [V] | Codex inside a product/CI | https://learn.chatgpt.com/docs/codex-sdk.md |
| App Server (JSON-RPC; auth, threads, approvals, streamed events) | programmatic | undated [V] | Rich-client embedding | https://learn.chatgpt.com/docs/app-server.md |
| `codex exec` non-interactive (`--json`, `CODEX_API_KEY`) | CLI | undated [S] | Scripted/headless runs | https://developers.openai.com/codex/noninteractive (search snippet; direct fetch failed 404 on alt URL) |
| Models: GPT-6.1 Sol default (2026-10-07), GPT-5.5 retired in Codex for ChatGPT sign-in 2026-10-14; GPT-6 Luna on Free/Go | all | Oct 2026 [V] | Model named in write-up should be current | changelog; pricing.md |

Pricing/free tier [V, https://learn.chatgpt.com/docs/pricing.md, undated]: Free $0 (GPT-6 Luna, desktop app, "subject to rollout"; no explicit allowance listed); Go $8; Plus $20 (web/CLI/IDE/cloud, GPT-6.1 Sol, est. ~15-160 local msgs per 5h on Sol, ~350-3,000 on Luna); Pro from $100; API key = standard API rates, no cloud/GitHub review features.

Runtime use inside a product (capabilities/requirements only):
- SDK/App Server/`codex exec` can drive Codex from your own process [V]. App Server docs state its auth "has never been permitted for commercial or hosted services" [V, app-server.md]; ChatGPT-managed and API-key modes exist [V]. API-key runs bill at API rates [V pricing.md]. Python SDK needs Python 3.10+, TS needs Node 18+ [V]. Sandbox presets read_only / workspace_write / full_access [V].
- SDK page does not explain ChatGPT-vs-API-key auth [V absence]. Plain OpenAI API usage (not Codex) is a separate, key-billed path [I].

## 2. "Using Codex well" signals

- Official best practices (undated) [V, https://learn.chatgpt.com/docs/learn/best-practices]: give goal + context + constraints + "done when"; use Plan mode / have Codex interview you / PLANS.md for ambiguous work; keep AGENTS.md short and add rules as mistakes repeat; tight permissions first; have Codex write tests, run checks and review its own diff (/review); MCP only where it removes a real manual loop; turn repeated prompts into skills; one chat per coherent unit of work, `/compact`, "avoid one chat for an entire project."
- Tension to note [I]: hackathon asks for the one thread holding most of the build; OpenAI advises not putting a whole project in one chat. A long, compacted main thread plus short side threads fits both.
- OpenAI's framing of Build Week: "build something real with Codex and GPT-5.6"; judged on technical implementation, design/UX, impact, idea quality [V, https://developers.openai.com/blog/build-week-winners]. Highlights domain experts and people stepping outside their specialty (Mechanica: Codex for physics/animation/3D) [V same].
- Hackathon-specific: FAQ stresses user owns ideas and decisions and must be able to explain the project [V competition/resources.md].
- Not found: statements by Codex team members about this hackathon [U]; Twitch/OpenAI press release for it [U] (two searches).

## 3. Past Codex/OpenAI hackathons (2025-2026)

| Name | Event | Codex usage emphasized | Source |
|---|---|---|---|
| Mechanica (Education 1st) | OpenAI Build Week (winners announced 2026-08-25 per secondary; OpenAI page says Aug 12 - dates conflict [S]) | Codex used to work outside team expertise (physics, animation, 3D); GPT-5.6 powers in-product docent | https://developers.openai.com/blog/build-week-winners [V]; https://www.remio.ai/post/openai-build-week-winners-show-what-codex-can-build-beyond-demos [V] |
| veTriage (Work 1st) | Build Week | Codex turned a vet's domain expertise into a working workflow | build-week-winners [V] |
| Dau, Pulse, Second Voice, AirBridge, Echo Canvas, Sentinel (2nds / Dev Tools etc.) | Build Week | Write-ups attribute function to GPT-5.6; Codex role not stated; several pair model output with deterministic checks | build-week-winners [V]; remio [V] |
| SB OAI Japan (top prize) | Global Codex Hackathon, Tokyo, 2026-04-22 | No detail read | https://www.softbank.jp/en/sbnews/entry/20260529_01 [S] |
| Sidekick (1st), Arto (2nd, built on Codex SDK) | "Agents Everywhere Hackathon with OpenAI" | Arto uses Codex SDK at runtime; LinkedIn secondhand | search snippet only [S] |
| Sea x OpenAI Codex Hackathon (Singapore 2026-06-06), OpenAI Game Builders Seoul (2026-08-31), Cognizant internal hackathon (10,000 staff) | corporate/regional | No winner detail found | Korea Times 2026-08-04 [S]; news.cognizant.com 2026-07-30 [S] |

Gap [U]: no Devpost project pages or videos read; official build-week page returned 403. Descriptive only; the sources do not show why anything won. Observation [V]: even OpenAI's own winners write-up says little about Codex workflow for 6 of 8 winners, so the Codex-process story in the video may be under-served by past entries [I].

## 4. Session ID and judge inspection
- Hackathon says type `/status` in the thread to get the session ID [V competition/resources.md]. The CLI slash-command page lists /status as model, approval policy, writable roots, token usage and does not mention a session ID; "session id" appears only as an optional /statusline footer item [V https://learn.chatgpt.com/docs/cli/slash-commands.md]. So the ID may come from the app/other surface or footer: verify on our own install now [U].
- App Server docs: thread has `thread.id`; forks get new thread IDs but keep root `thread.sessionId` [V app-server.md]. Forking the main thread could confuse "the thread where most of the build happened" [I].
- How judges inspect a session: nothing public [U]. Rules only say AI-driven analysis may be used [V]. Whether a submitted ID is viewable by non-owners is unknown [U].

## 5. Twitch priorities (2025-2026)

| Priority | Evidence | Date | Source |
|---|---|---|---|
| Monetization (Power-Ups with Bits, Creator Badge Drops, Mythic Train, Gift Em All, Creator Sponsorships up 3x vs 2025, Bounty Board, SEPA payouts) | Rotterdam recap | 2026-05-30 [V] | https://blog.twitch.com/en/2026/05/30/everything-we-announced-at-twitchcon-rotterdam-2026/ |
| Vertical / dual-format streaming | Beta rolling out; first announced San Diego 2025 | 2026-05-30 [V]; 2025-10-17 [V] | Rotterdam post; https://gamesbeat.com/?p=308304 |
| Clips and auto-generated content (Auto Clips, stream summaries, clip captions, Clips in Stories) | "Auto Clips" AI-driven | 2025-10-17 / 2026-05-30 [V] | same two |
| Discovery (mid-stream notifications, avatars in notifications, 1440p, Guilds) | Rotterdam | 2026-05-30 [V] | Rotterdam post |
| Safety / moderation (AutoMod smart detection, Lead Moderator role, Mod Appreciation; narrower suspensions) | | 2026-05-30, 2025-10-17 [V] | same two |
| Creator business tools (Creator Camp: sponsorships, analytics, Partnership path) for San Diego 2026 | Programming preview | 2026-08-27 [V] | https://www.netinfluencer.com/twitch-releases-programming-for-twitchcon-san-diego-2026/ |
| Community/collaboration framing ("belonging", collaboration foundational) | CEO interview summaries | June 2026 [S] | ceointerviews.ai summaries via search (AI-compiled, low reliability) |
| Developer platform | Active changelog: Pinned Chat API GA (2026-05-29/06-18), Custom Power-Up API/EventSub (2026-05-19), app access tokens for Send Chat Message, conduit shards, GIF in chat (2026-07-16), gifted-drops notices (2026-10-01); Extension CSP tweaks only | through 2026-10-01 [V] | https://dev.twitch.tv/docs/change-log/ |

Notes: Rotterdam post announced nothing for APIs/chatbots/Extensions [V]. San Diego 2026 is Nov 13-15; CEO keynote expected with "product announcements" [V netinfluencer]; the netinfluencer program mentions no AI, developers, hackathon or Codex [V]. Pre-event "predictions" (VR, AI moderation) are unsourced speculation [S].

## 6. Twitch AI stance
- Clancy, GamesBeat interview at Tokyo Game Show, article 2026-09-20 [V, https://gamesbeat.com/twitch-ceo-dan-clancy-says-platform-doesnt-need-ai-disclosure-rules-for-now/]: Twitch does not need AI disclosure rules "for now"; would act if streamers were "substituting themselves"; cited Esfand's Sora 2 videos as enhancing community creativity, "in no way... substitutional"; says most AI use on stream is apparent to viewers; AI for moderation/recommendations framed as responsibility. Did not discuss AI chatbots/co-hosts [V absence].
- Twitch uses AI in its own product (AutoMod smart detection, Auto Clips, stream summaries) [V Rotterdam post].
- Amazon AI training toggle ("Training for Generative AI") on by default, August 2026, community backlash [S only: godisageek (403), betanews (403), snippets]. Relevant to tone: creator trust and AI is a live sensitivity [I].
- Kick requires AI disclosure since March 2026 (contrast) [S].
- No Twitch rule found specifically on AI chatbots, AI co-hosts or AI-generated chat replies [U]. Dev changelog has no AI entries in 2026 and the Developer Services Agreement's latest listed revision is 2024-12-04 [V dev.twitch.tv/docs/change-log]; its text on bots/AI was not read [U].
- Extensions in 2026: only CSP updates found; no strategic statement [V/U]. Hackathon text itself treats Extensions as optional and slow [V].

## 7. Twitch/hackathon showcase intent
- Hackathon page: "Give chat a way to play along, help streamers create together, or add something new to enhance the content they stream"; judges want original ideas, not the example list [V overview.md]. Prize: top 5 on Codex Booth stage at TwitchCon, winners announced live [V]. Sponsor of record is Amazon Advertising LLC [V rules.md]; Twitch-side showcase intent beyond that: [U].

## Open questions
1. Where exactly does the session ID appear (/status on CLI vs app)? Test on our install today; confirm forked threads do not change the ID.
2. Can judges open a Codex thread by ID, or is the ID only a verification token? [U]
3. Free-tier model (GPT-6 Luna) vs Plus (GPT-6.1 Sol): does Free include CLI/cloud, or desktop app only? Pricing page implies app only [I]. Decide plan before build.
4. Twitch Developer Services Agreement terms on bots/AI-generated chat output (not read).
5. San Diego 2026 keynote (Nov 13) may shift stated priorities after our Nov 2 deadline; nothing sourced on developer/AI content.
6. Build Week page/Devpost galleries unread (403); real past-entry videos would show what a Codex "how it was built" segment looks like.
