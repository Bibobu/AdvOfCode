#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Your docstring here
'''

import numpy as np

opening = {']': '[', ')': '(', '}': '{', '>': '<'}
closing = {'[': ']', '(': ')', '{': '}', '<': '>'}

value1 = {']': 57, ')': 3, '}': 1197, '>': 25137}
value2 = {']': 2, ')': 1, '}': 3, '>': 4}

def sol1(filename):
    corrupt = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            opened = []
            closed = []
            for c in line:
                if c in ['[', '(', '{', '<']:
                    opened.append(c)
                elif c in [']', ')', '}', '>']:
                    if opened[-1] == opening[c]:
                        opened.pop(-1)
                    else:
                        corrupt.append(c)
                        break
    print(corrupt)
    s = sum([value1[x] for x in corrupt])
    print(s)


def sol2(filename):
    incomplete = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            corrupted = False
            line = line.strip()
            opened = []
            closed = []
            for c in line:
                if c in ['[', '(', '{', '<']:
                    opened.append(c)
                elif c in [']', ')', '}', '>']:
                    # Funny thing is this algorithm only keeps
                    # opened chunks
                    if opened[-1] == opening[c]:
                        opened.pop(-1)
                    else:
                        corrupted = True
            if not corrupted:
                incomplete.append(opened)
    print(incomplete)
    completions = []
    for inc in incomplete:
        com = []
        for c in reversed(inc):
            com.append(closing[c])
        completions.append(com)
    scores = []
    for com in completions:
        s = 0
        for c in com:
            s *= 5
            s += value2[c]
        scores.append(s)
    scores = np.array(sorted(scores))
    print(int(np.median(scores)))


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

