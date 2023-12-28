#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Solution of day 8 of 2023
'''

import time
import argparse as ap
import re
import math
from itertools import cycle


def solve1(file=None, verbose=False, solution=0):
    try:
        expr = re.compile(r"\W+")
        mymap = {}
        with open(file, 'r') as f:
            data = f.read().split('\n\n')
        instructions = data[0]
        nodes = data[1].split('\n')
        for n in nodes[:-1]:
            info = expr.split(n)
            mymap[info[0]] = {"L": info[1], "R": info[2]}
        current = 'AAA'
        instructions = cycle(instructions)
        while current != 'ZZZ':
            solution += 1
            go = next(instructions)
            current = mymap[current][go]

    except FileNotFoundError:
        pass

    return solution

def solve2(file=None, verbose=False, solution=0):
    try:
        expr = re.compile(r"\W+")
        mymap = {}
        starts = []
        end = []
        with open(file, 'r') as f:
            data = f.read().split('\n\n')
        instructions = data[0]
        instructions = cycle(instructions)

        nodes = data[1].split('\n')
        for n in nodes[:-1]:
            info = expr.split(n)
            if info[0][2] == 'A':
                starts.append(info[0])
            mymap[info[0]] = {"L": info[1], "R": info[2]}
        # The trick is actually that all the paths are rather short loops (less
        # than 100k steps) but they should all end on there Z label *at the
        # same time*. The first time this happens is our puzzle answer, and the
        # LCM of all the individual loops.
        # Note that given that there are two examples in this puzzle, this
        # solution will not work on the test set.
        for start in starts:
            for step, go in enumerate(instructions, start=1):
                start = mymap[start][go]
                if start[2] == 'Z':
                    end.append(step)
                    break
        return math.lcm(*end)

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
