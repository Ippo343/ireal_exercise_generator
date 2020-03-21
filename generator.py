#!/usr/bin/env python3
# -*- coding: utf8 -*-

from itertools import product
from random import shuffle

roots = "ABCDEFG"
accidentals = ("", "b", "#")
qualities = "7"

# iRealPro agrees with Code.
unsupported = {
    ("E", "#"),
    ("F", "b"),
    ("B", "#"),
}


def main():
    chords = [
        f"{r}{a}{q}"
        for r, a, q in product(roots, accidentals, qualities)
        if (r, a) not in unsupported
    ]

    shuffle(chords)
    chord_progression = "T44{" + " |".join(chords) + "}"

    song_data = {
        'title': "Exercise",
        'composer': 'Pilotino Gino',
        'style': 'Medium Swing',
        'key': 'C',
        'chord_progression': chord_progression,
    }

    link_template = "irealbook://{title}={composer}={style}={key}=n={chord_progression}"
    link = link_template.format(**song_data)

    with open("template.html") as f:
        template = f.read()

    print(template.format(link))


if __name__ == "__main__":
    main()
