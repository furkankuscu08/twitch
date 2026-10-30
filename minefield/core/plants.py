"""Anonymous, round-scoped bearer codes. Caller supplies randomness and time."""

ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"


class Plants:
    def __init__(self, game, rng):
        self.game = game
        self.rng = rng
        self.codes = {}
        self.round_id = game.round_id

    def clear(self):
        self.codes.clear()
        self.round_id = self.game.round_id

    def prune(self, now):
        if not self.game.running or self.round_id != self.game.round_id:
            self.clear()
        for code, (_, expires) in list(self.codes.items()):
            if expires <= now:
                del self.codes[code]

    def issue(self, word, now, *, pending_hands=0):
        self.prune(now)
        if not self.game.running:
            raise ValueError("No active round")
        if word not in self.game.deck.words:
            raise ValueError("Unknown deck selection")
        # WP11 prunes expired hands first and supplies their count. Allocation
        # and hand insertion must remain synchronous on the same event loop.
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
