#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt (the competition's deliverable path).
"""

import os

LINE = "The function you are afraid to touch is afraid of you too."


def main() -> None:
    # Self-check against the gate: 1-120 chars, one line, not blank.
    text = LINE.strip()
    assert 1 <= len(text) <= 120, f"line is {len(text)} chars, must be 1-120"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
