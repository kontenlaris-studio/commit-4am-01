#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit-message line (130 chars, single line) to /output/entry.txt.
Stdlib only. Deterministic: same output on every run.
"""
import os

ENTRY = (
    "fix: off-by-one at 4 a.m. \u2014 the loop ran 11 times for 10 users. "
    "The 11th user does not exist and has now filed a support ticket."
)


def main() -> None:
    assert len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
