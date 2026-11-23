"""One Letter for Your Day — make.fun entry.

The day behind this letter: unhinged. One plan after another came
loose from its hinges — meetings moved, tools broke, the schedule
rewrote itself — and by evening the whole day was swinging free.
The letter below is the first letter of that word, and the whole entry.
"""

from pathlib import Path

LETTER = "U"


def main() -> None:
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        raise ValueError("entry must be exactly one letter A-Z")
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    tmp = output.with_suffix(".tmp")
    tmp.write_text(LETTER, encoding="utf-8")
    tmp.replace(output)


if __name__ == "__main__":
    main()
