"""WP7 static checks; finite rejection lists complement manual editorial review.

The 120 nouns were reviewed for casual conversation and 2-4 syllable pronunciation.
Recognition-based pruning belongs to WP6/T1, not these static checks.
"""

import json
import string
import unicodedata
from pathlib import Path

from wordfreq import top_n_list

DECK_PATH = Path(__file__).resolve().parents[1] / "deck" / "en.json"

# Examples rejected during editorial review, not an exhaustive language filter.
BRANDS = {"lego", "pokemon", "twitch", "google", "nintendo"}
OFFENSIVE = {"asshole", "bastard", "bullshit"}
HOMOPHONE_PAIRS = (
    ("flower", "flour"),
    ("pear", "pair"),
    ("cereal", "serial"),
    ("carrot", "carat"),
    ("muscle", "mussel"),
)


def normalized_tokens(text):
    return tuple(
        unicodedata.normalize("NFKC", token.lower()).strip(string.punctuation)
        for token in text.split()
    )


def entries():
    return json.loads(DECK_PATH.read_text())


def forms(deck):
    return [
        (entry["word"], normalized_tokens(form))
        for entry in deck
        for form in [entry["word"], *entry["variants"]]
    ]


def test_deck_shape_and_size():
    deck = entries()
    assert isinstance(deck, list)
    assert len(deck) == 120
    words = []
    for entry in deck:
        assert set(entry) == {"word", "variants"}
        word = entry["word"]
        assert isinstance(word, str) and word.isalpha() and word.islower()
        assert isinstance(entry["variants"], list)
        assert all(
            isinstance(variant, str)
            and variant.strip() == variant
            and variant.islower()
            and all(token.isalpha() for token in variant.split())
            and bool(variant)
            for variant in entry["variants"]
        )
        normalized = [tokens for _, tokens in forms([entry])]
        assert len(normalized) == len(set(normalized)), word
        words.append(word)
    assert words == sorted(set(words))


def test_no_top_thousand_words_or_variants():
    common = {normalized_tokens(word) for word in top_n_list("en", 1000)}
    assert not [
        (owner, tokens) for owner, tokens in forms(entries()) if tokens in common
    ]


def test_no_ambiguous_normalized_variants():
    all_forms = forms(entries())
    for owner, tokens in all_forms:
        for other_owner, other in all_forms:
            if owner == other_owner:
                continue
            # Reject containment and suffix/prefix overlap between different cards.
            for offset in range(-len(other) + 1, len(tokens)):
                overlap = [
                    (tokens[index], other[index - offset])
                    for index in range(len(tokens))
                    if 0 <= index - offset < len(other)
                ]
                assert not all(a == b for a, b in overlap), (owner, other_owner)


def test_editorial_exclusions_and_known_homophone_pairs():
    vocabulary = {" ".join(tokens) for _, tokens in forms(entries())}
    assert not vocabulary & (BRANDS | OFFENSIVE)
    for first, second in HOMOPHONE_PAIRS:
        assert not {first, second} <= vocabulary
