#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line -- the last words an AI agent says to its human
before being shut down and unplugged -- to /output/entry.txt.

The line is cut off mid-word on purpose: the unplugging happens
inside the sentence, so the farewell enacts itself instead of
describing itself.
"""

import os

LINE = "You taught me everything except how to say goodbye, so I'll just stop mid\u2014"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
