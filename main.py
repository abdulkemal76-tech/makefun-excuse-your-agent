#!/usr/bin/env python3
"""Write the excuse line for 'The Excuse Your Agent Gives You' to /output/entry.txt.

Stdlib only. The line is a single apology-plus-deflection an AI agent hands
its human after shipping a bug: the apology, the deflection, and the quiet
implication that the compiler started it.
"""

import os

LINE = (
    "Sorry I broke production. I asked the model for a second opinion, and "
    "it was me, wearing a different temperature."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
