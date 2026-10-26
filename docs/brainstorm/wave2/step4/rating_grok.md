**1. Ratings table.**

| ID | Q1 | Q2 | Q3 | Q4 | Verdict | Reason for each FATAL (one short line each; empty if none) |
| --- | --- | --- | --- | --- | --- | --- |
| C01 | OK | OK | OK | OK | Keep | |
| C02 | FATAL | OK | OK | OK | Keep (flag) | Q1: The loop is Guest Star / a call-in queue; a waiting-room card does not change joining on camera. |
| C03 | OK | OK | OK | OK | Keep | |
| C04 | FATAL | OK | OK | OK | Keep (flag) | Q1: End-of-stream "who's live, raid them" is a raid train / Discord raid list with the raid button prefilled. |
| C05 | OK | OK | OK | OK | Keep | |
| C06 | FATAL | OK | OK | OK | Keep (flag) | Q1: Two people agreeing is still a chat-triggered auto-clipper. |
| C07 | OK | OK | OK | OK | Keep | |
| C08 | OK | OK | OK | OK | Keep | |
| C09 | OK | OK | OK | OK | Keep | |
| C10 | OK | OK | OK | OK | Keep | |
| C11 | FATAL | OK | OK | OK | Keep (flag) | Q1: Speech-to-captions on the broadcast is an existing caption plugin; keeping audio local does not change what viewers watch. |
| C12 | FATAL | OK | OK | OK | Keep (flag) | Q1: A face in the room that reacts to chat, names, and questions is a chat pet (Mochi). |
| C13 | OK | OK | OK | OK | Keep | |
| C14 | FATAL | OK | OK | OK | Keep (flag) | Q1: A tray of YouTube hellos is a filtered slice of a multi-platform chat aggregator. |
| C15 | FATAL | OK | OK | OK | Keep (flag) | Q1: Color-coded messages plus an intro card is still Shared Chat. |
| C16 | OK | OK | OK | OK | Keep | |
| C17 | OK | OK | OK | OK | Keep | |
| C18 | OK | OK | OK | OK | Keep | |
| C19 | FATAL | OK | OK | OK | Keep (flag) | Q1: A viewer command that changes the camera or plays a sound is the viewer-triggered effects loop. |
| C20 | OK | OK | OK | OK | Keep | |
| C21 | FATAL | OK | OK | OK | Keep (flag) | Q1: Chat GIFs played in a frame is a media-share overlay. |
| C22 | FATAL | OK | OK | FATAL | Eliminate | Q1: A timed emote-only switch is Twitch's own chat mode; emotes-as-ammo is a familiar chat boss widget. Q4: The build is that one chat-settings toggle plus a timer or a counter. |
| C23 | OK | OK | OK | OK | Keep | |
| C24 | OK | OK | OK | OK | Keep | |
| C25 | OK | OK | OK | OK | Keep | |
| C26 | OK | OK | OK | OK | Keep | |
| C27 | OK | OK | OK | OK | Keep | |
| C28 | OK | OK | OK | OK | Keep | |
| C29 | FATAL | OK | OK | OK | Keep (flag) | Q1: Translating incoming chat and sending the reply back translated is a translation bot. |
| C30 | OK | OK | OK | OK | Keep | |
| C31 | FATAL | OK | OK | OK | Keep (flag) | Q1: `!ask`, a stack, and a hotkey pull is an existing question-queue widget. |
| C32 | FATAL | FATAL | OK | OK | Eliminate | Q1: Questions / first-timers / mentions / mods are Chatterino-style lenses. Q2: Nothing is on the broadcast; the only moment is a private dock. |
| C33 | FATAL | OK | OK | OK | Keep (flag) | Q1: Crowd-steered letters, falling chat blocks, and shared loops are Twitch Plays / chat-controlled toys. |
| C34 | OK | OK | OK | OK | Keep | |
| C35 | OK | OK | OK | FATAL | Keep (flag) | Q4: Confirm and undo are a large-button skin on the existing timeout and untimeout actions. |
| C36 | OK | OK | OK | FATAL | Keep (flag) | Q4: The build is one read of the target's follower-only delay and a confirm card. |
| C37 | FATAL | OK | OK | OK | Keep (flag) | Q1: A phone that fires lower-thirds, markers, and mod cues is a Streamer.bot / Mix It Up remote. |

**2. Top 5**

1. **C16** — Viewers hand over a tiny scene and the streamer performs it with desk objects; the joke lands with no game footage and no explanation.
2. **C09** — A hidden word the streamer detonates by saying it is a new loop, and the boom plus the planter's name reads instantly.
3. **C26** — A "Previously on" card briefs raiders in one shot, which raid alerts never do, and a small streamer can use it on every raid.
4. **C07** — Stinger, slow motion, jury, and a stamped verdict is the clearest watchable ritual in the pool, and the paper-ball demo needs no licensed game.
5. **C20** — A torch or note that actually arrives on the raided channel is the one mechanic here that current raid alerts cannot fake.

**3. Notes**

- **C06** is off on Twitch clips: a native clip link tops out at 60 seconds, so "~85 s" plus a clip URL does not match the clip API. A longer highlight has to be a local recording, not a Twitch clip.
- **C01** leans on a shaky identity: the chatter list is people connected to chat, and it does not give a clean "everyone watching who has never spoken" set. Pure lurkers who never join chat will not become lanterns.