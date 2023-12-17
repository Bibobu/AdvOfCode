#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solutions for day 2 of 2023
"""

import time
import argparse as ap


class Bag:
    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue

    def is_possible(self, game):
        possible = (
            (self.red >= game.red)
            * (self.green >= game.green)
            * (self.blue >= game.blue)
        )
        return bool(possible)

    def __repr__(self):
        red, green, blue = self.red, self.green, self.blue
        return f"Contains {red} red, {green} green, {blue} blue."


def solve1(file=None, verbose=False, solution=0):
    # See instructions
    Mybag = Bag(red=12, green=13, blue=14)
    if verbose:
        print("MyBag", Mybag)
    with open(file, "r") as f:
        for line in f.readlines():
            possible = True
            (game_id, draws) = line.split(":")
            game_id = list(filter(lambda x: x.isdigit(), game_id))
            game_id = int("".join(game_id))
            draws = draws.split(";")
            for draw in draws:
                red, green, blue = 0, 0, 0
                cubes = draw.split(",")
                for cube in cubes:
                    if "red" in cube:
                        num = list(filter(lambda x: x.isdigit(), cube))
                        red = int("".join(num))
                    elif "green" in cube:
                        num = list(filter(lambda x: x.isdigit(), cube))
                        green = int("".join(num))
                    elif "blue" in cube:
                        num = list(filter(lambda x: x.isdigit(), cube))
                        blue = int("".join(num))
                tmp = Bag(red=red, green=green, blue=blue)
                possible *= Mybag.is_possible(tmp)
                if verbose:
                    print(f"My Draw with id {game_id}", tmp, f" and is {possible}.")
            solution += game_id * possible
    return solution


def solve2(file=None, verbose=False, solution=0):
    with open(file, "r") as f:
        for line in f.readlines():
            red, green, blue = 0, 0, 0
            (_, draws) = line.split(":")
            draws = draws.split(";")
            for draw in draws:
                cubes = draw.split(",")
                for cube in cubes:
                    if "red" in cube:
                        num = list(filter(lambda x: x.isdigit(), cube))
                        tmp = int("".join(num))
                        if tmp > red:
                            red = tmp
                    elif "green" in cube:
                        num = list(filter(lambda x: x.isdigit(), cube))
                        tmp = int("".join(num))
                        if tmp > green:
                            green = tmp
                    elif "blue" in cube:
                        num = list(filter(lambda x: x.isdigit(), cube))
                        tmp = int("".join(num))
                        if tmp > blue:
                            blue = tmp
            solution += red * green * blue

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
