#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Solution for day 3 2023
'''

import time
import argparse as ap


def add_nb(line, x):
    dx = -1
    c = line[x+dx]
    num = []
    while c.isdigit():
        dx -= 1
        c = line[x+dx]
    dx += 1
    c = line[x+dx]
    while c.isdigit():
        num.append(c)
        line[x+dx] = '.'
        dx += 1
        c = line[x+dx]
    num = int(''.join(num))
    return num

def prod_nb(grid, ln, cn):
    myprod = 1
    nlines, ncols = len(grid), len(grid[0])
    if ln == 0:
        nby = [0, 1]
    elif ln == nlines-1:
        nby = [-1, 0]
    else:
        nby = [-1, 0, 1]
    if cn == 0:
        nbx = [0, 1]
    elif cn == ncols-1:
        nbx = [-1, 0]
    else:
        nbx = [-1, 0, 1]
    count = 0
    for dy in nby:
        for dx in nbx:
            y, x = ln+dy, cn+dx
            if grid[y][x].isdigit():
                count += 1
                myprod *= add_nb(grid[y], x)
    if count != 2:
        myprod = 0
    return myprod

def sum_nb(grid, ln, cn):
    mysum = 0
    nlines, ncols = len(grid), len(grid[0])
    if ln == 0:
        nby = [0, 1]
    elif ln == nlines-1:
        nby = [-1, 0]
    else:
        nby = [-1, 0, 1]
    if cn == 0:
        nbx = [0, 1]
    elif cn == ncols-1:
        nbx = [-1, 0]
    else:
        nbx = [-1, 0, 1]
    for dy in nby:
        for dx in nbx:
            y, x = ln+dy, cn+dx
            if grid[y][x].isdigit():
                mysum += add_nb(grid[y], x)
    return mysum


def solve1(file=None, verbose=False, solution=0):
    grid = []
    with open(file, 'r') as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    for ln, line in enumerate(grid):
        for cn, c in enumerate(line):
            if not c.isdigit() and c != '.':
                total = sum_nb(grid, ln, cn)
                solution += total

    return solution

def solve2(file=None, verbose=False, solution=0):
    grid = []
    with open(file, 'r') as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    for ln, line in enumerate(grid):
        for cn, c in enumerate(line):
            if c == '*':
                total = prod_nb(grid, ln, cn)
                solution += total

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
