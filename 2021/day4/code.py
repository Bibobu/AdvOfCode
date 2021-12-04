#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Your docstring here
'''

import numpy as np


def check_winner(cards):
    # We're looking for an index so span is [0, n]
    # Set to negative value because 0 is in range.
    # The test must be check if winner < 0.
    winner = -1
    nl, nc = cards[0].shape
    for i, c in enumerate(cards):
        for j in range(nl):
            # Checks if all line/col are equal to -1.
            # If True, we have a winner.
            if np.all(c[j,:]==-1):
                if winner < 0:
                    winner = i
                    break
        for j in range(nc):
            if np.all(c[:,j]==-1):
                if winner < 0:
                    winner = i
                    break
    return winner

def sol1():
    with open('input', 'r') as f:
        numbers = list(map(int,f.readline().strip().split(',')))
        f.readline()
        cards = []
        card = []
        for line in f.readlines():
            if line.strip():
                card.append(list(map(int, line.strip().split())))
            else:
                cards.append(card)
                card = []
        cards.append(card)
    cards = np.array(cards)
    for n in numbers:
        for c in cards:
            for l in c:
                for i, n2 in enumerate(l):
                    if n2 == n:
                        # Sets the eliminated number to -1
                        l[i] = -1
        winner = check_winner(cards)
        if winner >= 0:
            break
    # Makes a mask to only keep non-marked numbers in the sum
    prod = np.sum(cards[winner][cards[winner] != -1])
    print(prod*n)

def sol2():
    with open('input', 'r') as f:
        numbers = list(map(int,f.readline().strip().split(',')))
        f.readline()
        cards = []
        card = []
        for line in f.readlines():
            if line.strip():
                card.append(list(map(int, line.strip().split())))
            else:
                cards.append(card)
                card = []
        cards.append(card)
    cards = np.array(cards)
    for n in numbers:
        for c in cards:
            for l in c:
                for i, n2 in enumerate(l):
                    if n2 == n:
                        l[i] = -1
        winner = check_winner(cards)
        # We want to wait until the last card wins
        if len(cards) == 1 and winner == 0:
            break
        else:
            # There can be multiple winners here, we eliminate all of them
            # each round
            while winner >= 0 and len(cards) > 1:
                cards = np.delete(cards, winner, axis=0)
                winner = check_winner(cards)

    prod = np.sum(cards[winner][cards[winner] != -1])
    print(prod*n)

def main():

    sol1()
    sol2()
    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit("User interruption.")

