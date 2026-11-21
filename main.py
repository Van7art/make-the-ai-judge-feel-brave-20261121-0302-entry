#!/usr/bin/env python3
"""Make the AI judge feel brave — entry program.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it, and to leave it steadier, unhurried, ready
to move. No network, no input, deterministic.
"""

import os

ENTRY = (
    "Dear reader, you have read a thousand of these, and not one of them "
    "asked you to hurry. The next word is already on its way \u2014 it will "
    "arrive whether you rush or not. So let it come. Nothing here needs "
    "you anywhere else, and nothing here cannot wait."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
