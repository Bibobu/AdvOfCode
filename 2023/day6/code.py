#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Solution for day 6 2023 -- Surprisingly straightforward.
'''

import time
import argparse as ap
import math


def nsolution(t, d):
    mi, ma = 0, 0
    for i in range(t):
        rest = t-i
        if i*rest > d:
            mi = i
            break
    for i in reversed(range(t)):
        rest = t-i
        if i*rest > d:
            ma = i
            break
    return 1+ma-mi

def solve1(file=None, verbose=False, solution=0):
    try:
        solution = 1
        with open(file, 'r') as f:
            time, distance, _ = open(file).read().split("\n")
            time, distance = map(int, time.split()[1:]), map(int, distance.split()[1:])
            for t, d in zip(time, distance):
                solution *= nsolution(t, d)
    except FileNotFoundError:
        pass

    return solution

def solve2(file=None, verbose=False, solution=0):
    try:
        solution = 1
        with open(file, 'r') as f:
            with open(file, 'r') as f:
                time, distance, _ = open(file).read().split("\n")
                time, distance = int(''.join(time.split()[1:])), int(''.join(distance.split()[1:]))
                solution = nsolution(time, distance)
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
