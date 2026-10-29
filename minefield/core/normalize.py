"""The same token normalization is used for matching and receipt masking."""

import unicodedata


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text.lower())
    while text and unicodedata.category(text[0]).startswith("P"):
        text = text[1:]
    while text and unicodedata.category(text[-1]).startswith("P"):
        text = text[:-1]
    return text
