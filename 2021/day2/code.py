#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Your docstring here
'''

def sol1():
    x = 0
    d = 0
    with open('input', 'r') as f:
        for line in f.readlines():
            comm, value = line.split()
            if comm == 'up':
                d -= int(value)
            elif comm == 'down':
                d += int(value)
            elif comm == 'forward':
                x += int(value)
    print(x*d)


def sol2():
    x = 0
    d = 0
    aim = 0
    with open('input', 'r') as f:
        for line in f.readlines():
            comm, value = line.split()
            if comm == 'up':
                aim -= int(value)
            elif comm == 'down':
                aim += int(value)
            elif comm == 'forward':
                x += int(value)
                d += aim*int(value)
    print(x*d)


def main():

    sol1()
    sol2()

    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit("User interruption.")

