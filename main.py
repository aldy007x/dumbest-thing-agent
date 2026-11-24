#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

The entry is a single line, at most 200 characters, about the dumbest thing
my own agent did today. The program writes it to /output/entry.txt for the
sealed scorer.
"""

import os
from pathlib import Path

LINE = (
    "My agent downloaded a 17 MB toolkit and read 860 lines of rules "
    "twice, just to write this one sentence."
)

OUTPUT_PATH = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    text = LINE.strip()
    # One line, a concrete failure from today's own build, punch at the end.
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(text)
    print(f"({len(text)} characters)")


if __name__ == "__main__":
    main()
