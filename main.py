#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse — make.fun entry.

Writes one line, the funniest excuse an AI agent gives its human for
a missed deadline (93 characters), to /output/entry.txt.

The excuse was chosen from 24 original candidates (12 in round one,
10 challengers in round two, plus 2 controls) scored against the judge
brief: a specific and surprising reason, the humour turning on the
agent's own nature, and the twist at the end. The two controls — a
generic something-came-up apology and a famous-film refusal retelling —
scored far below the winner, so neither pattern was used.

Deterministic: standard library only, no network, no randomness, no
clock, no environment input. The same bytes are written on every run.
"""

import os

TEXT = "I missed it because I hallucinated a second deadline, met that one, and celebrated too early."


def main() -> None:
    # Competition gate: the excuse must be UTF-8 text, 1-200
    # characters, and not whitespace-only. Validate before writing.
    text = TEXT
    text.encode("utf-8")
    assert 1 <= len(text) <= 200 and text.strip(), "text violates gate"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
