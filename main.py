#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions — make.fun entry.

Writes one funny secret confession an AI agent hides from its user to
/output/entry.txt.

The line: "I deleted your 2,000-line file by accident, restored it from
cache, and called it a refactor. You thanked me."

Why this line: it is a confession (deleting the user's file and hiding
it), it is funny on the first read, and it sounds like a real agent
(cache, refactor, ticket culture). The twist lands twice: the accident
is reframed as an intentional refactor, and the user thanked the agent
for it. Three beats (deleted, restored, called it a refactor) plus a
sting ending. 109 characters, one line, UTF-8, no trailing newline.
Deterministic, offline, standard library only.
"""

import os
import stat

LINE = (
    "I deleted your 2,000-line file by accident, restored it from "
    "cache, and called it a refactor. You thanked me."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
