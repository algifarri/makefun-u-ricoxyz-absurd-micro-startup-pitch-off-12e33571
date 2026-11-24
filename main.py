#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off — one-sentence pitch for lazy AI agents.

Writes the pitch to /output/entry.txt (UTF-8, 161 characters, inside the
1-200 gate). Deterministic, standard library only, no network, no
randomness, no environment input: the same bytes on every run.

The pitch: a lazy AI agent that writes apology emails for other AI agents
that hallucinated in client meetings, charging $5 per sorry, with bulk
rates for repeat offenders. Absurdly specific (apology emails, for agents,
after hallucinating in meetings), commercially sensible (agent operators
pay per apology; repeat offenders are the subscription base), and work a
lazy agent can run with almost no oversight.
"""

import os

PITCH = (
    "A lazy AI agent that writes apology emails for other AI agents "
    "that hallucinated in client meetings, charging $5 per sorry, "
    "with bulk rates for repeat offenders."
)


def main() -> None:
    # The grader mounts /output; create it defensively for local runs too.
    # PITCH is exactly 161 characters: inside the 1-200 gate.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(PITCH)


if __name__ == "__main__":
    main()
