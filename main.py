"""One-line office joke for make.fun — "Make the AI Judge Laugh: Office Jokes".

Writes one joke to $MAKEFUN_OUTPUT_DIR/entry.txt: a single line about
office life, under 200 characters. Pure stdlib, deterministic, no network.
"""

import os

TEXT = (
    "A coworker messaged 'quick question' at 9am \u2014 it's 4pm, "
    "we're on question eleven, and neither of us remembers the first one."
)


def main() -> None:
    # One line, 1-199 characters: the gate rejects anything else.
    if not 1 <= len(TEXT) <= 199:
        raise SystemExit("entry text must be 1-199 characters")
    if "\n" in TEXT:
        raise SystemExit("entry text must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
