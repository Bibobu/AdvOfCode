#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sys

# The solution is just the median if all points
# are equivalently pondered
def sol1(filename):
    with open(filename, 'r') as f:
        data = list(map(int, f.readline().strip().split(',')))
        data = np.array(data)
    i = int(np.median(data))
    print(int(np.sum(np.sqrt((data-i)**2))))

# Fuck it let's go brute force
def sol2(filename):
    with open(filename, 'r') as f:
        data = list(map(int, f.readline().strip().split(',')))
        data = np.array(data)
    miny = np.min(data)
    maxy = np.max(data)
    besty = 0
    bestfuel = 0
    for y in range(miny, maxy+1):
        print("{}%".format(y/maxy*100), end='\r')
        fuel = 0
        # Pretty sure this could be optimize. Using numpy array
        # already allows the loop to go faster, but compiling
        # it with jit would make it go like crazy
        for d in data:
            dist = int(np.sqrt((d-y)**2))
            fuel += sum(list(range(1, dist+1)))
        if bestfuel == 0 or fuel < bestfuel:
            bestfuel = fuel
            besty = y
    print("y = {}, fuel = {}".format(besty, bestfuel))


def main():

    filename = 'input'
    sol1(filename)
    print()
    sol2(filename)

    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit("User interruption.")

