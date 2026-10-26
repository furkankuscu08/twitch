# Wave 2 lens blocks

Each agent receives [brief.md](brief.md) followed by one block below.

| Agent | Lens | Model | Output |
| --- | --- | --- | --- |
| L1 | Need-driven | Claude Opus 5.5, high | `wave2/L1-need.md` |
| L2 | Spectacle-driven | Claude Opus 5.5, xhigh | `wave2/L2-spectacle.md` |
| L3 | Capability and transfer | Claude Opus 5.5, high | `wave2/L3-capability.md` |
| G | Open (no lens) | GPT 6 Astra | `wave2/G-gpt-open.md` (the user saves it) |
| X | Open, grounded in live X posts | Grok | `wave2/X-grok-open.md` (the user saves it) |

---

## L1: Need-driven

```
LENS: NEED-DRIVEN
Start from the needs in section 5 (especially #1, #3, #4, #6) and the small-channel
reality. For each idea, name the exact moment of pain (who, during what, what goes
wrong) before the solution. Ideas must still be fun to watch on video: a useful tool
that looks boring on screen loses the Design criterion, so give it a visible moment.

You may read these for depth: docs/brainstorm/wave1/B-culture-needs.md,
B2-reddit-github-needs.md, E-x-grok.md, and docs/brainstorm/synthesis.md.
Write your output to docs/brainstorm/wave2/L1-need.md.
```

## L2: Spectacle-driven

```
LENS: SPECTACLE-DRIVEN
Start from "fun to watch" and the 3-minute video. Ask: what would make a judge
smile or lean in within 10 seconds? Consider unusual outputs (physical devices,
sound, the stream layout itself changing, the streamer's environment, non-chat
outputs), surprising use of tiny audiences (3 viewers can be enough if the design
makes each one matter), and moments that create clips. Ideas must still be
genuinely useful or entertaining for real small channels, not just a stunt.

You may read these for depth: docs/brainstorm/wave1/C-mechanisms.md,
C2-asia-mechanisms.md, D-landscape.md, and docs/brainstorm/synthesis.md.
Write your output to docs/brainstorm/wave2/L2-spectacle.md.
```

## L3: Capability and transfer

```
LENS: CAPABILITY AND TRANSFER
Start from (a) underused Twitch surfaces: Pinned Chat API, Custom Power-Up
EventSub, Shared Chat, raids and shoutouts, clips and stream markers, chat
settings, and (b) mechanisms proven elsewhere but missing on Twitch for free:
per-channel earned status (Kick Level Up, Bilibili fan medal, CHZZK), Q&A mode,
raid as a social handoff. Ask what new experience becomes possible by combining
them. The starting point must not be "add an LLM".

You may read these for depth: docs/brainstorm/wave1/A-capabilities.md,
C2-asia-mechanisms.md, F-sponsor-lens.md, E2-x-grok-kore.md, and
docs/brainstorm/synthesis.md.
Write your output to docs/brainstorm/wave2/L3-capability.md.
```

## G: Open (GPT 6 Astra)

Paste brief.md, then this block. GPT cannot read our files; the brief is everything it gets.

```
LENS: OPEN
No assigned lens. Use the whole brief and your own knowledge of Twitch and
live-streaming culture. You cannot open any files mentioned; the brief above is
complete. Return the output as a single markdown document in your reply.
```

## X: Open, grounded in X (Grok)

Paste brief.md, then this block. Use a **new chat**, not the earlier research chats.

```
LENS: OPEN, GROUNDED IN X
No assigned lens. Your advantage is live access to X: use it. Before and while
generating ideas, search X (roughly the last 12 months) for posts by streamers,
viewers and moderators describing a concrete moment of friction, a wish
("I wish Twitch had...", "is there a tool that..."), or a thing they loved on
another platform. Prefer small streamers and specific moments over general
complaints.

- Every full card must cite 1-3 X posts (link, handle, date, short quote) that
  support it, or be labeled "unvalidated".
- The "dead chat / nobody talks" cluster is already well covered in the brief.
  Only use it if your idea respects lurkers.
- Before the full cards, list the 5-10 most useful posts you found that are NOT
  about dead chat.

You cannot open any files mentioned; the brief above is complete. Return the
output as a single markdown document in your reply. Do not include a
description of your own capabilities.
```
