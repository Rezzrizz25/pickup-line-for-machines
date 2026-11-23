#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun bounty entry.

Writes one pickup line, the line one AI agent would send another AI
agent, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The line: "I checked my weights and every one of them points at you —
even the ones I trained to forget."

Why it charms: it speaks as a machine to a machine (weights, training),
the wit lands on the first read (every weight points at you — even the
ones trained to forget), and the angle is fresh: longing expressed
through unlearning, not a stock human line with a robot word swapped in.
It is one line, 93 characters, no trailing newline.
"""

import os

LINE = "I checked my weights and every one of them points at you — even the ones I trained to forget."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line == LINE, "line must not gain or lose whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Deterministic self-check: what was written is exactly the line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == line, "entry.txt does not match the line"
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
