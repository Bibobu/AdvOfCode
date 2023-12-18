#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Template for solutions
'''

import time
import argparse as ap

def solve1(file=None, verbose=False, solution=0):
    try:
        with open(file, 'r') as f:
            pass
    except FileNotFoundError:
        pass

    return solution

def solve2(file=None, verbose=False, solution=0):
    try:
        with open(file, 'r') as f:
            pass
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
