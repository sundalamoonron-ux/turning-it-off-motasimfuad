#!/usr/bin/env python3
"""Have You Tried Turning It Off? — one funny tech-support line.

Writes a single line to /output/entry.txt: a hopeless tech support agent
putting a desperate customer on hold while he googles the exact error
message — the same thing the customer already did, but with hold music.
"""

import os

LINE = "I'm going to put you on a brief hold while I google your exact error message — same as you did, but with hold music."


def main() -> None:
    # Gate: 1-199 UTF-8 characters, not only whitespace.
    assert 1 <= len(LINE) <= 199 and LINE.strip(), "line fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
