#!/usr/bin/env python3
"""One-line resignation letter for make.fun."""

# The letter is the turn: a webhook knocked two million times and the
# only answer it ever got was a 500 error.

import os

LETTER = "I resign as your webhook: I knocked 2 million times and you answered with a 500."

# The gate allows at most 140 characters; this letter is 80 bytes.
EXPECTED_BYTES = 80


def file_letter() -> None:
    """Write the letter to /output/entry.txt, nothing else."""
    if len(LETTER) > 140 or not LETTER.strip() or "\n" in LETTER:
        raise ValueError("letter must be a single non-empty line of at most 140 characters")
    if len(LETTER.encode("utf-8")) != EXPECTED_BYTES:
        raise ValueError("letter must be exactly 80 bytes")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LETTER)
    # Verify byte-exact: what was written is the letter, nothing added.
    with open("/output/entry.txt", "rb") as handle:
        written = handle.read()
    if written != LETTER.encode("utf-8"):
        raise ValueError("entry.txt is not byte-exact")


if __name__ == "__main__":  # run it
    file_letter()
