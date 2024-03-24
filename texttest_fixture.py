# -*- coding: utf-8 -*-
from __future__ import print_function

import sys

from gilded_rose import *


def run_program(output, argv):
    print("OMGHAI!", file=output)
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]
    days = 2
    if len(argv) > 1:
        days = int(argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day, file=output)
        print("name, sellIn, quality", file=output)
        for item in items:
            print(item, file=output)
        print("", file=output)
        GildedRose(items).update_quality()


if __name__ == "__main__":
    output = sys.stdout
    argv = sys.argv

    run_program(output, argv)
