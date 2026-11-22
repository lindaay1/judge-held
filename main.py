#!/usr/bin/env python3
# Entry: "The Evening Saved You a Seat" — 248 code points, deterministic.
"""Write the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt). No deps, no network, deterministic."""
import os

TEXT = "Somewhere, rain is falling on a tin roof, slow and unhurried, and a kettle is coming to the boil for no one in particular. Nothing here needs you to be clever or quick. Stay a little longer. The evening has already saved you a seat, and it is warm."

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
