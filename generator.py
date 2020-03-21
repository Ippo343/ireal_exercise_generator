#!/usr/bin/env python3
# -*- coding: utf8 -*-


def main():
    with open("template.html") as f:
        template = f.read()

    chord_progression = "T44*A{C^7 |A-7 |D-9 |G7#5 }"

    song_data = {
        'title': "Exercise",
        'composer': 'Pilotino Gino',
        'style': 'Medium Swing',
        'key': 'C',
        'chord_progression': chord_progression,
    }

    link_template = "irealbook://{title}={composer}={style}={key}=n={chord_progression}"
    link = link_template.format(**song_data)
    print(template.format(link))


if __name__ == "__main__":
    main()
