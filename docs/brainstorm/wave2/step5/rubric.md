# Scoring: instructions for raters

You are an independent rater for a hackathon idea pool. Every idea here has already passed a screen for fatal weaknesses. Your job now is to **score** each one on the four judging criteria, as the judges would. You rate alone; you will never see the other raters' answers.

## The competition

**Codex x TwitchCon Hackathon** (Devpost). Deadline: Nov 2, 2026. About 565 registered participants; we expect roughly 30–70 actual submissions. The brief: "Build something streamers and their community on Twitch could really use." Entries must connect to Twitch (chat, overlays, Twitch API, EventSub) and be built with OpenAI Codex.

**Judging criteria** (official text, four equally weighted criteria; ties are broken by the first criterion, then the next):
1. **Innovation/Idea:** How creative and novel is the concept and does the project differ from existing concepts?
2. **Potential Impact:** How useful or entertaining is it for streamers and their communities?
3. **Technological implementation:** How well is it built, and how well does it use Codex?
4. **Design:** Is it easy to use and fun to watch?

Judges mostly watch a **video of under 3 minutes**. They may not run the project.

**The builder:** solo, ~10 hours of building with AI coding agents, new to Twitch, no audience. The demo channel is one streamer plus three test accounts. The video can't show commercial games or copyrighted music, so demos use desk/IRL content or open-source games.

## Expected crowd

Ideas we expect many entrants to build: AI co-host or chatbot, AI "what did I miss" summarizer, Twitch Plays, polls and predictions, trivia, dice or TTRPG overlays, viewer-triggered distractions and sound effects, auto-clippers, collab or cross-channel games, chat pets, bingo, sports overlays, question queues, loyalty levels, alert packs.

## How to score

Give every candidate an integer score from **0 to 5** on each of the four criteria. A candidate's total is 0–20.

Measure against the **whole expected field of 30–70 submissions**, not only against these 20.

| Score | Innovation | Impact | Technical | Design |
| --- | --- | --- | --- | --- |
| 0 | A copy of an existing tool or of a crowd idea | No real streamer would use it | A trivial wrapper; nothing to build | Nothing visible on stream, or it can't be understood |
| 1 | A crowd idea with a cosmetic twist | A one-off novelty | Thin: one call or one setting behind a UI | Needs narration to be understood |
| 2 | A known loop; the twist changes the experience a little | Niche: a rare situation or a rare kind of streamer | Modest: one integration, little to show | Understandable but dull to watch |
| 3 | Known pieces in a combination judges won't see often | Useful for many streamers sometimes, or for some regularly | Several parts working together; a solid demo fits in ~10 h | A clear on-screen moment, mildly fun |
| 4 | A loop few or no other entrants will have; clearly different from existing tools | Most small streamers would use it regularly | Meaningful integration (several Twitch surfaces plus real-time or local parts) that can still be polished in ~10 h; a good Codex story | Readable in seconds and fun to watch |
| 5 | A judge who has seen every entry would remember this one as new | A widely felt problem solved, or a segment communities would ask for again | Impressive depth that still fits ~10 h and shows clearly in the video | A moment judges would want to replay |

Guidance:
- Judge each idea at its **best variant**: if the description lists variants, pick the strongest one.
- Technical means "how well it can be built", so a scope that is clearly too big for ~10 hours scores lower, not higher.
- Do **not** penalize the untested APIs or setup needs listed under "Notes" (a second channel, hardware); they are tested separately.
- Think about what a judge sees in the video, not only what the tool does.
- **Use the whole scale.** On each criterion, give a 5 to at most 4 candidates. If more than half of the candidates share the same score on one criterion, re-check that criterion.

## Output format

Return exactly this, in markdown:

**1. Scores.** One row per candidate, in ID order:

| ID | Name | Innovation | Impact | Technical | Design | Total | One-line reason |
| --- | --- | --- | --- | --- | --- | --- | --- |

**2. Top 5.** Your five strongest, with two or three sentences each: why they would win, and the weakest criterion of each.

**3. Bottom 5.** Your five weakest, with one sentence each: the main reason.

**4. Notes (optional).** Any candidate you think is factually wrong about Twitch, or any two candidates you think are really the same idea.

Rules:
- Score every candidate on all four criteria.
- Don't search the web; judge from your own knowledge.
- Keep reasons concrete.
- Don't rewrite or merge ideas.
