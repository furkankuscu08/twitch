"""Round state and public projections; no I/O or implicit clocks."""

from dataclasses import dataclass, field

from .config import Config


@dataclass
class Mine:
    id: str
    owner: str
    word: str = field(repr=False)
    planted_at: float = 0
    arms_at: float = 0
    status: str = "arming"
    boom_at: float | None = None
    boom_order: int = 0

    @property
    def live(self):
        return self.status in {"arming", "armed", "sparking"}


class Game:
    def __init__(self, deck, config=None):
        self.deck = deck
        self.config = config or Config()
        self.running = False
        self.started_at = 0
        self.mines = {}
        self.next_id = 1
        self.boom_sequence = 0
        self.archived_booms = 0
        self.archived_entries = []
        self.archived_truncated = False

    def start(self, now):
        if self.running:
            raise ValueError("Round already running")
        self.running = True
        self.started_at = now
        self.boom_sequence = 0
        self.archived_booms = 0
        self.archived_entries.clear()
        self.archived_truncated = False
        self.mines.clear()
        return [self.snapshot(now)]

    def plant(self, owner, word, now):
        if not self.running:
            raise ValueError("No active round")
        self.compact(now)
        live = [mine for mine in self.mines.values() if mine.live]
        if any(mine.owner == owner for mine in live):
            raise ValueError("Owner already has a live mine")
        if any(mine.word == word for mine in live):
            raise ValueError("Word taken, pick another")
        if len(live) >= self.config.MAX_MINES:
            raise ValueError("Minefield full")
        if word not in self.deck.words:
            raise ValueError("Unknown deck selection")
        mine = Mine(str(self.next_id), owner, word, now, now + self.config.ARM_DELAY_S)
        self.next_id += 1
        self.mines[mine.id] = mine
        return [
            {
                "type": "mine_planted",
                "id": mine.id,
                "owner": owner,
                "arms_in_s": self.config.ARM_DELAY_S,
            }
        ]

    def arm(self, now):
        self.compact(now)
        events = []
        for mine in self.mines.values():
            if mine.status == "arming" and now >= mine.arms_at:
                mine.status = "armed"
                events.append({"type": "mine_armed", "id": mine.id})
        return events

    def snapshot(self, now, plant_url=None):
        self.compact(now)
        return {
            "type": "snapshot",
            "round": {"running": self.running},
            "plant_url": plant_url,
            "mines": [
                {
                    "id": mine.id,
                    "owner": mine.owner,
                    "status": mine.status,
                    "arms_in_s": max(0, mine.arms_at - now),
                }
                for mine in self.mines.values()
            ],
        }

    def false_alarm(self, now):
        if not self.running:
            return []
        self.compact(now)
        eligible = [
            mine
            for mine in self.mines.values()
            if mine.status == "exploded"
            and 0 <= now - mine.boom_at <= self.config.FALSE_ALARM_WINDOW_S
        ]
        if not eligible:
            return []
        mine = max(eligible, key=lambda item: (item.boom_at, item.boom_order))
        mine.status = "false_alarm"
        return [{"type": "false_alarm", "id": mine.id, "owner": mine.owner}]

    def end(self, now):
        if not self.running:
            return [], ""
        self.compact(now)
        booms = sorted(
            (mine for mine in self.mines.values() if mine.status == "exploded"),
            key=lambda mine: mine.boom_order,
        )
        duds = [mine for mine in self.mines.values() if mine.live]
        for mine in duds:
            mine.status = "dud"
        events = [
            {
                "type": "reveal",
                "duds": [{"owner": mine.owner, "word": mine.word} for mine in duds],
                "stats": {"booms": self.archived_booms + len(booms)},
            }
        ]
        recap = self._recap(booms, duds)
        self.running = False
        self.mines.clear()
        self.archived_booms = 0
        self.archived_entries.clear()
        self.archived_truncated = False
        return events, recap

    def compact(self, now):
        expired = sorted(
            (
                mine
                for mine in self.mines.values()
                if not mine.live
                and mine.boom_at is not None
                and now - mine.boom_at > self.config.FALSE_ALARM_WINDOW_S
            ),
            key=lambda mine: mine.boom_order,
        )
        for mine in expired:
            if mine.status == "exploded":
                self.archived_booms += 1
                entry = f"@{mine.owner} ({mine.word})"
                used = sum(len(item) + 2 for item in self.archived_entries)
                if (
                    not self.archived_truncated
                    and used + len(entry) + 2 <= self.config.CHAT_MAX_CHARS
                ):
                    self.archived_entries.append(entry)
                else:
                    self.archived_truncated = True
            del self.mines[mine.id]

    def _recap(self, booms, duds):
        count = self.archived_booms + len(booms)
        prefix = f"Round over: {count} booms." if count else "Round over: no booms."
        entries = [("boom", entry) for entry in self.archived_entries]
        if not self.archived_truncated:
            entries += [("boom", f"@{mine.owner} ({mine.word})") for mine in booms]
            entries += [("dud", f'@{mine.owner}\'s "{mine.word}"') for mine in duds]

        def render(items):
            hits = [text for kind, text in items if kind == "boom"]
            survivors = [text for kind, text in items if kind == "dud"]
            return (
                prefix
                + (" 💥 " + ", ".join(hits) + "." if hits else "")
                + (" Survived: " + ", ".join(survivors) + "." if survivors else "")
            )

        message = render(entries)
        truncated = self.archived_truncated
        while entries and len(message) + int(truncated) > self.config.CHAT_MAX_CHARS:
            entries.pop()
            truncated = True
            message = render(entries)
        if truncated:
            message = message[: self.config.CHAT_MAX_CHARS - 1] + "…"
        return message[: self.config.CHAT_MAX_CHARS]
