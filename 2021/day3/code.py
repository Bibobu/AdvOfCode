#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Your docstring here
'''

import numpy as np


def sol1():
    with open('input', 'r') as f:
        line = f.readline().strip()
        bits = list(map(int, [x for x in line]))
        for i, line in enumerate(f.readlines()):
            nbits = list(map(int, [x for x in line.strip()]))
            bits = [x+y for (x,y) in zip(bits, nbits)]
    gamma = [1 if x > (i+2)/2 else 0 for x in bits]
    epsilon = [0 if x > (i+2)/2 else 1 for x in bits]
    gamma = int(''.join(list(map(str, gamma))), 2)
    epsilon = int(''.join(list(map(str, epsilon))), 2)
    print("{} * {} = {}".format(gamma, epsilon, gamma*epsilon))


def sol2():
    data = []
    with open('input', 'r') as f:
        for line in f.readlines():
            data.append(list(map(int, [x for x in line.strip()])))
    data = np.array(data)
    nlin, ncol = data.shape
    oxygen = data.copy()
    CO2 = data.copy()
    for j in range(ncol):
        if oxygen.shape[0] == 1:
            pass
        else:
            count = np.bincount(oxygen[:, j])
            if count[0] == count[1]:
                val = 1
            else:
                val = count.argmax()
            mask = oxygen[:,j] == val
            oxygen = oxygen[mask]
        if CO2.shape[0] == 1:
            pass
        else:
            count = np.bincount(CO2[:, j])
            if count[0] == count[1]:
                val = 0
            else:
                val = count.argmin()
            mask = CO2[:,j] == val
            CO2 = CO2[mask]
    oxygen = int(''.join(list(map(str, *oxygen))), 2)
    CO2 = int(''.join(list(map(str, *CO2))), 2)
    print("{} * {} = {}".format(oxygen, CO2, oxygen*CO2))


def main():

    # sol1()
    sol2()

    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit("User interruption.")

