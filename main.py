#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun entry.

One line in the GPS's own voice: its excuse for sending the driver down
the wrong road. The program writes the line to /output/entry.txt (the path
the make.fun grader reads) and prints it.
"""

import os
import sys

ENTRY = (
    "The map swore the lake was a shortcut, and the lake has never once "
    "corrected me, so if anyone here is lying, it's the water."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not ENTRY.strip():
        raise SystemExit("entry must not be empty")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit")
    if len(ENTRY.splitlines()) != 1:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise SystemExit("written entry does not match the entry text")
    print(ENTRY)
    print(f"({len(ENTRY)} characters, limit {MAX_CHARS})", file=sys.stderr)


if __name__ == "__main__":
    main()
