#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 7 2023
"""

import time
import collections
import argparse as ap


class Hand:
    values = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    def __init__(self, cards):
        self.cards = cards
        self.type = 0
        cnt = collections.Counter(cards)
        if 5 in cnt.values():
            self.type = 6
        elif 4 in cnt.values():
            self.type = 5
        elif 3 in cnt.values():
            if 2 in cnt.values():
                self.type = 4
            else:
                self.type = 3
        elif 2 in cnt.values():
            ntwo = list(cnt.values()).count(2)
            self.type = ntwo

    def shift(self):
        # Surprisingly this implementation looked a lot like mgtezak:
        # https://github.com/mgtezak/Advent_of_Code/blob/master/2023/Day_07.py
        # But his is much cleaner. Check it.
        js = self.cards.count('J')
        other = [c for c in self.cards if c != 'J']
        cnt = sorted(collections.Counter(other).values(), reverse=True)
        self.cards = self.cards.replace('J', '1')
        if js == 5:
            self.type = 6
        elif cnt[0] + js == 5:
            self.type = 6
        elif cnt[0] + js == 4:
            self.type = 5
        elif cnt[0] + js == 3:
            if cnt[1] == 2:
                self.type = 4
            else:
                self.type = 3
        elif cnt[0] == 2 and (js or cnt[1] == 2):
            self.type = 2
        elif cnt[0] == 2 or js:
            self.type = 1
        else:
            self.type = 0

    def __gt__(self, other):
        if self.type != other.type:
            return self.type > other.type
        for c1, c2 in zip(self.cards, other.cards):
            if c1 != c2:
                return Hand.values[c1] > Hand.values[c2]

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        for c1, c2 in zip(self.cards, other.cards):
            if c1 != c2:
                return Hand.values[c1] < Hand.values[c2]

    def __print__(self):
        return "Hand: {:}".format(self.cards)

    def __repr__(self):
        return "Hand: {:}, Type: {:}".format(self.cards, self.type)


def solve1(file=None, verbose=False, solution=0):
    try:
        data = []
        with open(file, "r") as f:
            for line in f.readlines():
                cards, bid = line.split()
                hand = Hand(cards)
                bid = int(bid)
                data.append([hand, bid])
        data = sorted(data, key=lambda d: d[0])
        solution = sum([(i+1)*d[1] for i, d in enumerate(data)])
    except FileNotFoundError:
        pass

    return solution


def solve2(file=None, verbose=False, solution=0):
    try:
        with open(file, "r") as f:
            data = []
            with open(file, "r") as f:
                for line in f.readlines():
                    cards, bid = line.split()
                    hand = Hand(cards)
                    hand.shift()
                    bid = int(bid)
                    data.append([hand, bid])
            data = sorted(data, key=lambda d: d[0])
            solution = sum([(i+1)*d[1] for i, d in enumerate(data)])
    except FileNotFoundError:
        pass

    return solution


def main():
    parser = ap.ArgumentParser()
    parser.add_argument("-i", dest="input", action="store_true")
    parser.add_argument("-v", dest="verbose", action="store_true")
    args = parser.parse_args()
    infile = "input" if args.input else "test"
    verbose = args.verbose

    t0 = time.time()
    sol1 = solve1(infile, verbose)
    dt = time.time() - t0
    print(f"Solution 1: {sol1}, Time: {dt}")

    t0 = time.time()
    sol2 = solve2(infile, verbose)
    dt = time.time() - t0
    print(f"Solution 2: {sol2}, Time: {dt}")

    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit("User interruption.")
