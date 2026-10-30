"""Anonymous, round-scoped bearer codes. Caller supplies randomness and time."""

ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"


class Plants:
    def __init__(self, game, rng):
        self.game = game
        self.rng = rng
        self.codes = {}
        self.hands = {}
        self.round_id = game.round_id

    def clear(self):
        self.codes.clear()
        self.hands.clear()
        self.round_id = self.game.round_id

    def prune(self, now):
        if not self.game.running or self.round_id != self.game.round_id:
            self.clear()
        for code, (_, expires) in list(self.codes.items()):
            if expires <= now:
                del self.codes[code]
        for hand_id, (_, expires) in list(self.hands.items()):
            if expires <= now:
                del self.hands[hand_id]

    def hand(self, now):
        self.prune(now)
        if not self.game.running:
            raise ValueError("No active round")
        if len(self.codes) + len(self.hands) >= self.game.config.MAX_PENDING_PLANTS:
            raise ValueError("Plant capacity reached, try again shortly")
        cards = self.game.deck.hand(self.rng, self.game.config.HAND_SIZE)
        start = self.rng.randrange(2**128)
        for offset in range(len(self.hands) + 1):
            hand_id = f"{self.round_id}-{(start + offset) % (2**128):032x}"
            if hand_id not in self.hands:
                self.hands[hand_id] = (tuple(cards), now + self.game.config.CODE_TTL_S)
                return {"hand_id": hand_id, "cards": cards}

    def pick(self, hand_id, word, now):
        self.prune(now)
        if hand_id not in self.hands:
            raise ValueError("Unknown or expired hand, pick a new hand")
        if word not in self.hands[hand_id][0]:
            raise ValueError("Selection is not in this hand")
        # Replace this hand with a code without increasing the shared budget.
        code = self.issue(word, now, pending_hands=len(self.hands) - 1)
        del self.hands[hand_id]
        return {
            "code": code,
            "command": f"!mine {code}",
            "expires_at": self.codes[code][1],
        }

    def issue(self, word, now, *, pending_hands=None):
        self.prune(now)
        if not self.game.running:
            raise ValueError("No active round")
        if word not in self.game.deck.words:
            raise ValueError("Unknown deck selection")
        if pending_hands is None:
            pending_hands = len(self.hands)
        if len(self.codes) + pending_hands >= self.game.config.MAX_PENDING_PLANTS:
            raise ValueError("Plant capacity reached, try again shortly")
        space = len(ALPHABET) ** 4
        start = self.rng.randrange(space)
        # At most len(codes) collisions: bounded even with a constant test RNG.
        for offset in range(len(self.codes) + 1):
            number = (start + offset) % space
            code = ""
            for _ in range(4):
                code = ALPHABET[number % len(ALPHABET)] + code
                number //= len(ALPHABET)
            if code not in self.codes:
                self.codes[code] = (word, now + self.game.config.CODE_TTL_S)
                return code

    def redeem(self, code, owner, now):
        self.prune(now)
        code = code.upper()
        if code not in self.codes:
            raise ValueError("Unknown or expired code")
        word, _ = self.codes[code]
        events = self.game.plant(owner, word, now)
        del self.codes[code]
        return events
