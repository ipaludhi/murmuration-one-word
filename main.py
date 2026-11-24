"""Murmuration — one word, first thought.

Writes the single word "murmuration" to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR). No network, no randomness, no input.
Deterministic: every run writes byte-identical output.

Why this word: a flock of starlings swirling as one shape in the sky —
surprising as a first thought, one unmistakable vivid picture, and the
word itself hums like the flock (murmur inside it). Specific, not a
filler; chosen, not a safe cliché like love or serendipity. One word,
no second draft — the first thought, kept as it came.
"""

import os
from pathlib import Path

TEXT = "murmuration"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
