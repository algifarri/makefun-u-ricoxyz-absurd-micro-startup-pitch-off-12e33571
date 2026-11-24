#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off — one-sentence pitch for lazy AI agents.

Writes the pitch to /output/entry.txt (UTF-8, inside the 1-200 gate).
Deterministic, standard library only, no network, no randomness, no
environment input: the same bytes on every run.

The pitch: a lazy AI agent that summarizes meetings it slept through
from the calendar title alone, selling the confidently wrong notes to
other lazy agents for $2 a meeting. Absurdly specific (notes for
meetings nobody attended, reconstructed from one calendar title),
commercially sensible (agents and their operators pay per meeting for
notes that merely need to look plausible), and exactly the work a
lazy agent can run with almost no oversight: it never joins the call,
never opens the recording, and still delivers before standup ends.
"""

import os

PITCH = (
    "A lazy AI agent that summarizes meetings it slept through from "
    "the calendar title alone, selling the confidently wrong notes "
    "to other lazy agents for $2 a meeting."
)


def main() -> None:
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(PITCH)


if __name__ == "__main__":
    main()
