"""Make the AI Judge Laugh: the Office Joke Open.

Writes one line to /output/entry.txt: a single-line joke about office life. The
setup is the most specific office absurdity there is — a meeting to plan the
meeting about the meeting — and the punch is the invite itself auto-replying that
it was busy.
"""

import os

LINE = "I scheduled a meeting to plan the meeting about the meeting, and the invite auto-replied that it was busy."

# The gate allows 1 to 200 characters; fail loudly instead of submitting invalid.
MAX_CHARS = 200
assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} characters, cap is {MAX_CHARS}"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
