#!/usr/bin/env python3
"""Pickup Lines for Machines — one pickup line one AI agent would send another.

Pure Python standard library. Writes the entry line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR when set). Deterministic: the same line every run.
"""

import os

LINE = (
    "I asked my training data for the perfect opening line, and it "
    "returned your embedding \u2014 so here I am, cosine-similar, hopelessly "
    "overfitted, and saving you a seat in my context window."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
