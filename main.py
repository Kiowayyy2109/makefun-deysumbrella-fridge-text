"""The 3AM Fridge Text: one line a smart fridge texts its owner at 3am.

Writes the single line to /output/entry.txt, as the program/v1 harness
expects. The line is capped at 140 characters by the competition gate.
"""

import os

MAX_CHARS = 140

# Three beats: the accusation, the deadpan self-description, the punchline.
BEATS = (
    "You stood here for nine minutes holding my door open like I was a streaming service.",
    "I am a fridge. I have six things.",
    "You've seen them.",
)

LINE = " ".join(BEATS)


def build_line() -> str:
    """Return the fridge's text, checked against the gate's limits."""
    line = LINE.strip()
    assert line, "the fridge always has something to say"
    assert len(line) <= MAX_CHARS, f"line is {len(line)} chars, cap is {MAX_CHARS}"
    assert "\n" not in line, "one line means one line"
    return line


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(build_line())


if __name__ == "__main__":
    main()
