import random
from dataclasses import replace

import pytest

from minefield.core.config import Config
from minefield.core.deck import Deck
from minefield.core.game import Game
from minefield.core.plants import Plants


def setup(**overrides):
    game = Game(
        Deck(
            [
                {"word": word, "variants": []}
                for word in ("pineapple", "volcano", "banana")
            ]
        ),
        replace(Config(), **overrides),
    )
    game.start(0)
    return game, Plants(game, random.Random(1))


def test_anonymous_one_time_bind_and_secrecy():
    game, plants = setup()
    code = plants.issue("pineapple", 1)
    assert len(code) == 4 and not set(code) & set("0O1I")
    events = plants.redeem(code.lower(), "viewer", 2)
    assert "pineapple" not in str(events) + str(game.snapshot(2))
    assert next(iter(game.mines.values())).owner == "viewer"
    with pytest.raises(ValueError, match="Unknown or expired"):
        plants.redeem(code, "other", 3)


def test_rejections_do_not_consume_code():
    game, plants = setup(MAX_MINES=1)
    code = plants.issue("pineapple", 0)
    other = plants.issue("volcano", 0)
    game.plant("viewer", "pineapple", 0)
    for owner, selected in [("viewer", other), ("other", code), ("other", other)]:
        with pytest.raises(ValueError):
            plants.redeem(selected, owner, 1)
        assert selected in plants.codes
    game.end(2)
    game.start(3)
    # Runtime clears the store at round boundaries; direct calls also cannot
    # resurrect a previous round's code after a new Game.start.
    with pytest.raises(ValueError, match="Unknown or expired"):
        plants.redeem(code, "other", 4)


def test_expiry_pruning_cap_and_future_hands_share_budget():
    game, plants = setup(MAX_PENDING_PLANTS=2, CODE_TTL_S=5)
    code = plants.issue("pineapple", 0, pending_hands=1)
    with pytest.raises(ValueError, match="capacity"):
        plants.issue("volcano", 1, pending_hands=1)
    with pytest.raises(ValueError, match="Unknown or expired"):
        plants.redeem(code, "viewer", 5)
    first = plants.issue("pineapple", 5)
    second = plants.issue("volcano", 5)
    assert first != second
    with pytest.raises(ValueError, match="capacity"):
        plants.issue("banana", 6)
    assert len(plants.codes) == 2
    plants.issue("banana", 10)
    assert len(plants.codes) == 1
    game.end(11)
    plants.clear()
    assert not plants.codes
    with pytest.raises(ValueError, match="No active round"):
        plants.issue("pineapple", 12)


def test_code_collision_is_resolved_without_overwriting():
    game, plants = setup()
    plants.rng.randrange = lambda _: 0
    first = plants.issue("pineapple", 0)
    second = plants.issue("volcano", 0)
    assert first != second
    plants.redeem(first, "a", 1)
    plants.redeem(second, "b", 1)
    assert {mine.word for mine in game.mines.values()} == {"pineapple", "volcano"}


def test_invalid_word_is_rejected_before_allocation():
    _, plants = setup()
    with pytest.raises(ValueError, match="Unknown deck selection"):
        plants.issue("unknown", 0)
    assert not plants.codes
