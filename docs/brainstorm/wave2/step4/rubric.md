# Quality gate: instructions for raters

You are an independent rater for a hackathon idea pool. Your job is to find **fatal weaknesses**, not to rank. You rate alone; you will never see the other raters' answers.

## The competition

**Codex x TwitchCon Hackathon** (Devpost). Deadline: Nov 2, 2026. About 565 registered participants; we expect roughly 30–70 actual submissions. The brief: "Build something streamers and their community on Twitch could really use." Entries must connect to Twitch (chat, overlays, Twitch API, EventSub) and be built with OpenAI Codex.

**Judging:** four equally weighted criteria. Ties are broken by Innovation.
1. **Innovation:** Does it differ from existing concepts?
2. **Potential Impact:** Is it useful or entertaining for streamers and their communities?
3. **Technical implementation:** How well does it use Codex?
4. **Design:** Is it easy to use and fun to watch?

Judges mostly watch a **video of under 3 minutes**. They may not run the project.

**The builder:** solo, ~10 hours of building with AI coding agents, new to Twitch, no audience. The demo channel is one streamer plus three test accounts. The video can't show commercial games or copyrighted music, so demos use desk/IRL content or open-source games.

## Expected crowd

Ideas we expect many entrants to build:
- AI co-host or chatbot
- AI "what did I miss" summarizer
- Twitch Plays
- polls and predictions
- trivia
- dice or TTRPG overlays
- viewer-triggered distractions and sound effects
- auto-clippers
- collab or cross-channel games
- chat pets
- bingo
- sports overlays
- question queues
- loyalty levels
- alert packs

## The four questions

For each candidate, answer each question with **OK** or **FATAL**. FATAL means a weakness serious enough that this idea should not take one of the few remaining slots. Judge the idea at its **best variant**: the description may list variants, so pick the strongest one.

| # | Criterion | FATAL if… |
| --- | --- | --- |
| Q1 | Innovation | With the name and visuals stripped away, the core loop is something the expected crowd or a well-known existing tool already does, **and** the claimed twist does not change the experience. |
| Q2 | Design | There is no moment in the first 10 seconds of a video that a judge would understand **without narration**, e.g. it happens only in private views, needs explanation, or looks like nothing happened. |
| Q3 | Impact | A real small streamer would use it **once or never**: a one-off stunt, a problem too rare to matter, or value only for the demo. |
| Q4 | Technical | Either **too thin**: little more than a wrapper around one existing Twitch setting or feature, so the build (and the Codex story) would look trivial. Or **clearly too big** for ~10 agent-assisted hours to reach a demo-quality MVP. |

**Do not** mark FATAL for feasibility risks listed under "Notes" (untested APIs, a second channel, hardware). They are tracked and tested separately. Only judge Q4's size question.

**Verdict:** 0 FATAL → **Keep**. 1 FATAL → **Keep (flag)**. 2 or more FATAL → **Eliminate**.

## Output format

Return exactly this, in markdown:

**1. Ratings table.** One row per candidate, in ID order:

| ID | Q1 | Q2 | Q3 | Q4 | Verdict | Reason for each FATAL (one short line each; empty if none) |
| --- | --- | --- | --- | --- | --- | --- |

**2. Top 5 (optional, not used for elimination).** The five candidates you find most promising for winning this competition, with one line each.

**3. Notes (optional).** Any candidate whose description you think is factually wrong about Twitch, or any two candidates you think are really the same idea.

Rules:
- Rate every candidate.
- Don't search the web; judge from your own knowledge.
- Keep reasons concrete.
- Don't rewrite or merge ideas.
