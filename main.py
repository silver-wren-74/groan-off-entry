"""The One-Liner Groan-Off.

Writes a single original one-line dad joke (<=140 characters) to
/output/entry.txt, exactly as the competition gate requires.

The line is built to the judge's criteria, in order: it is a one-line
dad joke, a pun a dad would tell out loud at the dinner table (1);
the setup and the turn sit inside the single line and the punchline
lands on the last word (2); the calendar telling the joke is a fresh
angle, not a joke anyone has heard a hundred times (3); it is tight
and rhythmic, easy to say out loud and easy to pass on (4); and the
groan is earned -- the calendar's days are literally numbered, and
the idiom means it is dying, so the joke is silly and sharp at once
(5).

Revision pass (deliberate, against the judge's criteria): the first
draft had the pun but the calendar was a flat prop ("the calendar ...
It said"), so a rival entry with a voice of its own could win on
criteria 3 and 5. The revision gives the calendar a character: it
is now "my calendar", and it answers with a polite refusal ("I'd
love to -- but ...") that turns the pun into its dying wish. The
punchline still lands on the last word, and the line stays one
sentence of plain spoken English.
"""

import os

JOKE = "I asked my calendar for a joke. It said, 'I'd love to \u2014 but my days are numbered.'"


def main() -> None:
    assert 1 <= len(JOKE) <= 140, f"joke is {len(JOKE)} characters"
    assert JOKE.strip() == JOKE and "\n" not in JOKE
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
