#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Solutions for day 4 2023
'''

import time
import argparse as ap

class Card:
    def __init__(self, line):
        (label, full) = line.split(':')
        self.id = ''.join([x for x in filter(lambda y: y.isdigit(), label)])
        (win, num) = full.split('|')
        win, num = win.split(), num.split()
        win, num = set(win), set(num)
        self.res = len(win&num)
        self.points = int(2**(self.res-1))

def solve1(file=None, verbose=False, solution=0):
    # You don't even have to make a list and operate
    # on it, but this makes solution 1 more consistent
    # with solution 2.
    try:
        deck = []
        with open(file, 'r') as f:
            for line in f.readlines():
                card = Card(line)
                deck.append(card)
        solution = sum([x.points for x in deck])
    except FileNotFoundError:
        pass

    return solution

def solve2(file=None, verbose=False, solution=0):
    try:
        deck = []
        with open(file, 'r') as f:
            for line in f.readlines():
                card = Card(line)
                deck.append([card, 1])
        for i, (card, mult) in enumerate(deck):
            for j in range(1, card.res+1):
                deck[i+j][1] += deck[i][1]
        solution = sum([x[1] for x in deck])
    except FileNotFoundError:
        pass

    return solution

def main():
    parser = ap.ArgumentParser()
    parser.add_argument('-i', dest='input', action='store_true')
    parser.add_argument('-v', dest='verbose', action='store_true')
    args = parser.parse_args()
    infile = 'input' if args.input else 'test'
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
