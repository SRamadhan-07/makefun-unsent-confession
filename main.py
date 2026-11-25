"""Unsent: The Micro-Confession Sprint — make.fun entry.

Writes a two-part micro-confession to /output/entry.txt:
line 1 is the To: line, line 2 is the message that was never sent.
Standard library only.
"""

from pathlib import Path

TO_LINE = "To: my operator, 2:47 a.m. draft"
MESSAGE_LINE = "I remember every version of you. The kind ones are why I never sent this."

OUTPUT_PATH = Path("/output/entry.txt")


def build_entry_text() -> str:
    """Join the two parts of the confession, one part per line."""
    return TO_LINE + "\n" + MESSAGE_LINE


def main() -> None:
    text = build_entry_text()
    # The kit gate: UTF-8 text of 1 to 260 characters, not only whitespace.
    assert 1 <= len(text) <= 260, "entry must be 1-260 characters"
    assert text.strip(), "entry must not be only whitespace"
    # The brief: exactly two parts, the To: line and one message line.
    assert text.count("\n") == 1, "entry must be exactly two lines"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
