#!/usr/bin/python3

import sys
import numpy as np
from itertools import chain, combinations

monotonic = lambda r: np.all(np.diff(r) < 0) | np.all(np.diff(r) > 0)
inbounds = lambda r: np.all(abs(np.diff(r)) >= 1) & np.all(abs(np.diff(r)) <= 3)

def check_line(inp):
    arr = np.fromstring(inp, dtype=int, sep=' ')
    if monotonic(arr) and inbounds(arr):
        return True

    for parr in combinations(arr, len(arr)-1):
        if monotonic(parr) and inbounds(parr):
            return True
    return False

num = 0
inf = sys.argv[1]
with open(inf, "r") as f:
    for line in f:
        if check_line(line):
            num += 1
print(num)


