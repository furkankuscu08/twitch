"""Validate decoded deck data and index forms once, outside the audio hot path."""

from dataclasses import dataclass

from .normalize import normalize


@dataclass(frozen=True)
class Occurrence:
    word: str
    number: int
    first: int
    last: int
    start: float
    end: float
    prob: float


class Deck:
    def __init__(self, entries):
        self.words = tuple(entry["word"] for entry in entries)
        if not self.words or len(set(self.words)) != len(self.words):
            raise ValueError("Invalid deck")
        forms = []
        for entry in entries:
            for form in (entry["word"], *entry["variants"]):
                tokens = tuple(normalize(token) for token in form.split())
                if not tokens or not all(tokens):
                    raise ValueError("Invalid deck form")
                for other_word, other in forms:
                    if other_word == entry["word"]:
                        continue
                    for offset in range(-len(other) + 1, len(tokens)):
                        if all(
                            tokens[i] == other[i - offset]
                            for i in range(len(tokens))
                            if 0 <= i - offset < len(other)
                        ):
                            raise ValueError("ambiguous deck variants")
                forms.append((entry["word"], tokens))
        self.index = {}
        for word, tokens in forms:
            self.index.setdefault(tokens[0], []).append((word, tokens))

    def hand(self, rng, size):
        return rng.sample(self.words, size)

    def occurrences(self, words):
        tokens = [normalize(word["text"]) for word in words]
        counts = {}
        result = []
        for first, token in enumerate(tokens):
            for canonical, form in self.index.get(token, ()):
                last = first + len(form)
                if tuple(tokens[first:last]) != form:
                    continue
                counts[canonical] = counts.get(canonical, 0) + 1
                result.append(
                    Occurrence(
                        canonical,
                        counts[canonical],
                        first,
                        last,
                        words[first]["start"],
                        words[last - 1]["end"],
                        min(word["prob"] for word in words[first:last]),
                    )
                )
                break
        return result

    def receipt(self, words, hit, limit):
        first = max(0, hit.last - limit)
        # Include the complete hit even when a multiword form spans the window.
        first = min(first, hit.first)
        masked = set()
        for occurrence in self.occurrences(words):
            if occurrence.first == hit.first and occurrence.last == hit.last:
                continue
            masked.update(range(occurrence.first, occurrence.last))
        result = []
        index = first
        while index < hit.last:
            if index == hit.first:
                result.append(
                    {
                        "text": " ".join(
                            word["text"] for word in words[hit.first : hit.last]
                        ),
                        "hit": True,
                    }
                )
                index = hit.last
            else:
                result.append(
                    {
                        "text": "•••" if index in masked else words[index]["text"],
                        "hit": False,
                    }
                )
                index += 1
        return result
