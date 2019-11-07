#!/usr/bin/python

import sys

def gen_plays(arr):
    new_arr = []
    moves = [['rock'], ['paper'], ['scissors']]

    for item in arr:
        for move in moves:
            new_arr.append(item + move)
    
    return new_arr


def rock_paper_scissors(n):
    if n <= 0:
        return [[]]
    
    if n == 1:
        return [['rock'], ['paper'], ['scissors']]

    return gen_plays(rock_paper_scissors(n - 1))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')