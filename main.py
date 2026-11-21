#!/usr/bin/env python3
"""Make the AI judge feel brave — entry program.

Writes one short relaxing text to /output/entry.txt.
Python 3.13, no network, no dependencies.

Revision pass: tightened the wording — "haven't made up their minds"
for "still thinking it over", cut the filler "Just", and closed on
"unhurried" (the brief's own word for brave) instead of "rested".
"""

import os

TEXT = (
    "Morning hasn't decided yet \u2014 the field is grey, "
    "the birds haven't made up their minds, "
    "the fence posts have no opinion. "
    "You don't have to decide either. "
    "Stand here, in the not-yet, where nothing is graded "
    "and nothing is late. The day will arrive; "
    "meet it unhurried."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT.strip()
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of gate range"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
