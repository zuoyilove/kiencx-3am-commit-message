"""The 3AM Commit Message entry.

Writes one commit-message line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the line is fixed in this file; no clock, no randomness,
no network, no third-party imports (standard library only).
"""

import os

LINE = "fix: reverted my own 2am fix; past me is a threat to this codebase and I have reported myself to HR"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
