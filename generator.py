#!/usr/bin/env python3
# -*- coding: utf8 -*-

import argparse
import sys
from itertools import product
from random import shuffle

roots = "ABCDEFG"
accidentals = ("", "b", "#")
default_qualities = ("7", "^7")


def main(args):

    chords = [
        f"{r}{a}{q}"
        for r, a, q in product(roots, accidentals, args.qualities)
    ]

    shuffle(chords)
    chord_progression = "T44{" + " |".join(chords) + " }"

    song_data = {
        'title': "aaa Random chords {}".format(tuple(args.qualities)),
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

    parser = argparse.ArgumentParser()
    parser.add_argument("qualities", nargs="*", default=default_qualities)
    args = parser.parse_args(sys.argv[1:])
    main(args)
