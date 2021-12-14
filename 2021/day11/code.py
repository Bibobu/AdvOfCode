#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import scipy.ndimage as ndimage

def step(data):
    flash = 0
    canflash = np.ones(data.shape, dtype=np.int64)
    data += 1
    while np.any(data > 9):
        for j, c in enumerate(data):
            for i, r in enumerate(c):
                myval = data[j, i]
                if myval > 9 and canflash[j,i]:
                    flash += 1
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            if (dx == 0 and dy == 0):
                                pass
                            elif (i == 0 and dx == -1):
                                pass
                            elif (j == 0 and dy == -1):
                                pass
                            else:
                                try:
                                    data[j+dy, i+dx] += 1
                                except IndexError:
                                    pass
                    data[j,i] = 0
                    canflash[j,i] = 0
                    data *= canflash
    return data, flash

def sol1(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            data.append([int(x) for x in line])
    data = np.array(data, dtype=np.int64)
    print(data)
    nflash = 0
    for _ in range(100):
        data, flash = step(data)
        nflash += flash
    print(data)
    print(nflash)

def sol2(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            data.append([int(x) for x in line])
    data = np.array(data, dtype=np.int64)
    print(data)
    maxflash = data.shape[0] * data.shape[1]
    nstep = 0
    flash = 0
    while flash != maxflash:
        data, flash = step(data)
        nstep += 1
        print(nstep, end = '\r')
    print(data)
    print(nstep, flash)

def main():

    filename='input'
    # sol1(filename)
    print()
    sol2(filename)
    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit("User interruption.")

