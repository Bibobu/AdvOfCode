#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Your docstring here
'''

import numpy as np


# For this one, let's make a line class
class Line:
    # A line is defined by only two points
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return "p1 = {} {}\np2 = {} {}".format(
            self.p1[0],
            self.p1[1],
            self.p2[0],
            self.p2[1]
            )

    # The class can draw the line on an array
    def draw_line(self, array, diag=True):
        x1, x2 = self.p1[0], self.p2[0]
        y1, y2 = self.p1[1], self.p2[1]
        ymin = min(y1, y2)
        ymax = max(y1, y2)
        xmin = min(x1, x2)
        xmax = max(x1, x2)
        if x1 == x2:
            array[ymin:ymax+1, x1] += 1
        elif y1 == y2:
            array[y1,xmin:xmax+1] += 1
        # This argument is added for solution 1 to
        # give the correct answer
        elif diag:
            # Look for higher point and goes down
            # The trick is to correctly match the range
            # Don't forget that the stop index is not used
            # in the loop. Hence the xstop+step.
            y = ymin
            xstart, xstop = (x1, x2) if y1 == ymin else (x2, x1)
            step = 1 if xstart <= xstop else -1
            for x in range(xstart, xstop+step, step):
                array[y, x] += 1
                y += 1
        return array

# I make a read function for simplicity.
# It's trivial, and returns list of lines
# and maximum dimensions to use for the array.
def read_file(file):
    with open(file, 'r') as f:
        smoke_lines = []
        max_x = 0
        max_y = 0
        for line in f.readlines():
            line = line.strip()
            p1, p2 = line.split('->')
            p1 = list(map(int, p1.strip().split(',')))
            p2 = list(map(int, p2.strip().split(',')))
            smoke_lines.append(Line(p1, p2))
            max_x = max([p1[0], p2[0], max_x])
            max_y = max([p1[1], p2[1], max_y])
    return (max_x+1, max_y+1), smoke_lines


# We simply make an array of 0.
# Each line drawn will increase the line count by 1.
def sol1(filename):
    dims, smoke_lines = read_file(filename)
    print(dims)
    mymap = np.zeros(dims, dtype=np.uint32)
    for l in smoke_lines:
        mymap = l.draw_line(mymap, diag=False)
    ncross = np.sum(mymap > 1)
    # print(mymap)
    print(ncross)


# The solution is essentially the same as sol1.
# Only the algorithm of draw_line changes.
def sol2(filename):
    dims, smoke_lines = read_file(filename)
    print(dims)
    mymap = np.zeros(dims, dtype=np.uint32)
    for l in smoke_lines:
        mymap = l.draw_line(mymap)
    ncross = np.sum(mymap > 1)
    # print(mymap)
    print(ncross)


def main():

    filename = 'input'
    sol1(filename)
    sol2(filename)

    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit("User interruption.")

