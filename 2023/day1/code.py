#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day1 2023
Note: This solution uses some Python 3.10 features
"""

import time
import argparse as ap


def check_digits(line, verbose):
    num = []
    for i, c in enumerate(line):
        if c.isdigit():
            num.append(int(c))
            break
        match c:
            case "o":
                if line[i : i + 3] == "one":
                    num.append(1)
                    break
                else:
                    continue
            case "t":
                if line[i : i + 3] == "two":
                    num.append(2)
                    break
                elif line[i : i + 5] == "three":
                    num.append(3)
                    break
                else:
                    continue
            case "f":
                if line[i : i + 4] == "four":
                    num.append(4)
                    break
                elif line[i : i + 4] == "five":
                    num.append(5)
                    break
                else:
                    continue
            case "s":
                if line[i : i + 3] == "six":
                    num.append(6)
                    break
                elif line[i : i + 5] == "seven":
                    num.append(7)
                    break
                else:
                    continue
            case "e":
                if line[i : i + 5] == "eight":
                    num.append(8)
                    break
                else:
                    continue
            case "n":
                if line[i : i + 4] == "nine":
                    num.append(9)
                    break
                else:
                    continue
            case _:
                continue
    line = line[::-1]
    if verbose:
        print("State of num after 1st read: ", num)
    for i, c in enumerate(line):
        if c.isdigit():
            num.append(int(c))
            break
        match c:
            case "e":
                if line[i : i + 3] == "eno":
                    num.append(1)
                    break
                elif line[i : i + 5] == "eerht":
                    num.append(3)
                    break
                elif line[i : i + 4] == "evif":
                    num.append(5)
                    break
                elif line[i : i + 4] == "enin":
                    num.append(9)
                    break
                else:
                    continue
            case "o":
                if line[i : i + 3] == "owt":
                    num.append(2)
                    break
                else:
                    continue
            case "r":
                if line[i : i + 4] == "ruof":
                    num.append(4)
                    break
                else:
                    continue
            case "x":
                if line[i : i + 3] == "xis":
                    num.append(6)
                    break
                else:
                    continue
            case "n":
                if line[i : i + 5] == "neves":
                    num.append(7)
                    break
                else:
                    continue
            case "t":
                if line[i : i + 5] == "thgie":
                    num.append(8)
                    break
                else:
                    continue
            case _:
                continue
    if verbose:
        print("State of num after 2nd read: ", num)
    return num


def solve1(file="test", verbose=False, solution=0):
    with open(file, "r") as f:
        for line in f.readlines():
            num = filter(lambda x: x.isdigit(), line)
            num = list(map(int, num))
            solution += 10 * num[0] + num[-1]
    return solution


def solve2(file, verbose=False, solution=0):
    with open(file, "r") as f:
        for line in f.readlines():
            num = check_digits(line, verbose)
            if verbose:
                print(line, " ", num)
            solution += 10 * num[0] + num[-1]

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
