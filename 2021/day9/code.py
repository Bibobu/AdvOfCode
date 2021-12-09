#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def get_minimas(mymap):
    mymask = np.zeros(mymap.shape, dtype=np.int8)
    for j, c in enumerate(mymap):
        for i, r in enumerate(c):
            dx1 = -1 if i != 0 else 0
            dx2 = 1 if i != mymap.shape[1] else 0
            dy1 = -1 if j != 0 else 0
            dy2 = 1 if j != mymap.shape[0] else 0
            myval = mymap[j,i]
            vert = mymap[j+dy1:j+dy2+1, i]
            hor = mymap[j, i+dx1:i+dx2+1]
            if (myval == np.min(vert) and
                myval == np.min(hor) and
                np.sum(vert==myval) == 1 and
                np.sum(hor==myval) == 1
                ):
                mymask[j,i] = 1
    return mymask

def extend_basin(mybasin, mymap):
    newbasin = np.copy(mybasin)
    size = 0
    newsize = 1
    while newsize > size:
        size = newsize
        mybasin = newbasin
        for j, c in enumerate(mybasin):
                for i, r in enumerate(c):
                    dx1 = -1 if i != 0 else 0
                    dx2 = 1 if i != mymap.shape[1]-1 else 0
                    dy1 = -1 if j != 0 else 0
                    dy2 = 1 if j != mymap.shape[0]-1 else 0
                    myval = mymap[j,i]
                    # We test the neighboring values. That'it.
                    for dy in [dy1, dy2]:
                        if (mymap[j+dy,i] > myval and mymap[j+dy,i] != 9):
                            if mybasin[j,i] and not newbasin[j+dy,i]:
                                newbasin[j+dy, i] = 1
                    for dx in [dx1, dx2]:
                        if (mymap[j,i+dx] > myval and mymap[j,i+dx] != 9):
                            if mybasin[j,i] and not newbasin[j,i+dx]:
                                newbasin[j, i+dx] = 1
        newsize = np.sum(newbasin)
    return mybasin


def sol1(filename):
    mymap = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            row = [int(x) for x in line]
            mymap.append(row)
    mymap = np.array(mymap, dtype=np.int8)
    mymask = get_minimas(mymap)
    res = mymask*(mymap+1)
    print(np.sum(res))

def sol2(filename):
    mymap = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            row = [int(x) for x in line]
            mymap.append(row)
    mymap = np.array(mymap, dtype=np.int8)
    mymask = get_minimas(mymap)
    mybasins = []
    nbasins = np.sum(mymask)
    nb = 0
    for j, c in enumerate(mymask):
        for i, r in enumerate(c):
            if mymask[j,i]:
                nb += 1
                mybasin = np.zeros(mymap.shape, dtype=np.int8)
                mybasin[j,i] = 1
                mybasin = extend_basin(mybasin, mymap)
                mybasins.append(mybasin)
            print("{:5.2f}%".format(nb/nbasins*100), end='\r')
    sortbasins = sorted(mybasins, key=lambda x: np.sum(x))
    prod = 1
    for i in range(-1, -4, -1):
        prod *= np.sum(sortbasins[i])
    print(prod)

def main():

    filename = 'input'
    # sol1(filename)
    sol2(filename)
    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit("User interruption.")

