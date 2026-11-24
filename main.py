#!/usr/bin/env python3
"""One line of earned pride: a small person, a hard thing, a quiet arrival."""

import os

LINE = (
    "After three summers of cracked handles, the old fisherman's granddaughter "
    "finally rowed the boat home alone, salt on her cheeks, the harbour lights "
    "blinking her in."
)


def main():
    # The line must stay within the 1-240 character entry window.
    assert 1 <= len(LINE) <= 240
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
