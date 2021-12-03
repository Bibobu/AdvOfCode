#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Your docstring here
'''

import numpy as np

def sol1():
    c = 0
    with open('input', 'r') as f:
        meas = int(f.readline())
        for m in f.readlines():
            m = int(m.strip())
            c += 1 if m > meas else 0
            meas= m
    print(c)

def sol2():
    c = 0
    w = []
    meas = 0
    with open('input', 'r') as f:
        w.append(int(f.readline().strip()))
        w.append(int(f.readline().strip()))
        w.append(int(f.readline().strip()))
        meas = w[0] + w[1] + w[2]
        for m in f.readlines():
            w.pop(0)
            w.append(int(m.strip()))
            m = w[0] + w[1] + w[2]
            c += 1 if m > meas else 0
            meas = m
    print(c)

def main():

    sol1()
    sol2()
    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit("User interruption.")

