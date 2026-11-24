"""Two-Sentence Horror.

Writes one horror story of exactly two sentences (under 400
characters) to /output/entry.txt. Standard library only.
"""

import os
import re

STORY = (
    # Verified 2026-11-24: 136 characters, exactly 2 sentences, 138 bytes.
    "A letter arrived today in my own handwriting, dated next Tuesday. "
    "It says only: 'Don't answer the door \u2014 he sounds exactly like "
    "me now.'"
)


def count_sentences(text: str) -> int:
    # A sentence ends at a terminator (optionally followed by a closing
    # quote) at the end of the text or before whitespace.
    return len(re.findall(r"[.!?][\"']?(?:\s|$)", text))


def main() -> None:
    # Gate: the sealed scorer only accepts 1-400 characters, not only
    # whitespace, and the bounty demands exactly two sentences. Fail
    # loudly here instead of shipping an invalid entry.
    sentences = count_sentences(STORY)
    if sentences != 2:
        raise ValueError(f"story has {sentences} sentences, must be exactly 2")
    if not 1 <= len(STORY) <= 400 or not STORY.strip():
        raise ValueError(f"story is {len(STORY)} characters, must be 1-400")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
