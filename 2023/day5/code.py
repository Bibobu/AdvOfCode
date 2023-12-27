#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 5 2023
"""

import time
import argparse as ap
import copy
import sys
from functools import reduce


def convert_range(inputs, mappings):
    for start, length in inputs:
        while length > 0:
            for m in mappings.split("\n")[1:]:
                dst, src, len = map(int, m.strip().split())
                delta = start - src
                if delta in range(len):
                    len = min(len - delta, length)
                    yield (dst + delta, len)
                    start += len
                    length -= len
                    break
            else:
                yield (start, length)
                break


def solve2(file=None, verbose=False, solution=0):
    """
    This snippet was cleverly set up by 4HBq. Link here:
    https://www.reddit.com/r/adventofcode/comments/18b4b0r/comment/kc2au1l/?utm_source=share&utm_medium=web2x&context=3
    Took me a while to get the reduce and generator part but I finally figured out why it worked as is.
    """
    try:
        seeds, *mappings = open(file).read().split("\n\n")
        seeds = list(map(int, seeds.split()[1:]))

        solution = [
            min(reduce(convert_range, mappings, s))[0]
            for s in [zip(seeds[0::2], seeds[1::2])]
        ][0]
    except FileNotFoundError:
        pass

    return solution


def convert(f, field1, field2, verbose=False):
    """
    Reads a map and computes the corresponding values to field1 to field2
    """
    while line := f.readline():
        if "map" in line:
            continue
        elif line.isspace():
            break
        (start2, start1, ran) = map(int, line.split())
        delta2 = start2 - start1
        for j, f1 in enumerate(field1):
            if f1 > start1 and f1 < start1 + ran:
                field2[j] += delta2
    if verbose:
        print(field1, field2)

    return


def solve1(file=None, verbose=False, solution=0):
    try:
        with open(file, "r") as f:
            seeds = list(map(int, f.readline().split()[1:]))
            f.readline()
            soils = copy.deepcopy(seeds)
            print("Converting soils...")
            convert(f, seeds, soils, verbose)
            ferti = copy.deepcopy(soils)
            print("Converting ferti...")
            convert(f, soils, ferti, verbose)
            water = copy.deepcopy(ferti)
            print("Converting water...")
            convert(f, ferti, water, verbose)
            light = copy.deepcopy(water)
            print("Converting light...")
            convert(f, water, light, verbose)
            tempe = copy.deepcopy(light)
            print("Converting tempe...")
            convert(f, light, tempe, verbose)
            humid = copy.deepcopy(tempe)
            print("Converting humid...")
            convert(f, tempe, humid, verbose)
            locat = copy.deepcopy(humid)
            print("Converting locat...")
            convert(f, humid, locat, verbose)
            solution = min(locat)
        if verbose:
            print("Seeds: {:}".format(seeds))
            print("Soils: {:}".format(soils))
            print("Ferti: {:}".format(ferti))
            print("Water: {:}".format(water))
            print("Light: {:}".format(light))
            print("Tempe: {:}".format(tempe))
            print("Humid: {:}".format(humid))
            print("Locat: {:}".format(locat))
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
