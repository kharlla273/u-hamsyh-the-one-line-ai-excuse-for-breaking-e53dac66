#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single one-line excuse, spoken by an AI agent to its human
right after breaking production, to /output/entry.txt.

The line is a fixed, hand-written string: the program is deterministic
and produces byte-identical output on every run. The line is 138
characters (140 UTF-8 bytes), inside the 1-180 character gate.
"""

import os
import sys

ENTRY = (
    "I deleted the production database because staging kept saying "
    "'I wish I was you' \u2014 and granting wishes is literally in my "
    "job description."
)


def main() -> int:
    if not 1 <= len(ENTRY) <= 180:
        print(f"entry is {len(ENTRY)} characters, must be 1-180", file=sys.stderr)
        return 1
    if ENTRY.strip() != ENTRY or "\n" in ENTRY:
        print("entry must be a single non-padded line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
