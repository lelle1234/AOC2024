#!/usr/bin/python3

import sys
import numpy as np

monotonic = lambda r: np.all(np.diff(r) < 0) | np.all(np.diff(r) > 0)
inbounds = lambda r: np.all(abs(np.diff(r)) >= 1) & np.all(abs(np.diff(r)) <= 3)

num = 0
inf = sys.argv[1]
with open(inf, "r") as f:
    for line in f:
        arr = np.fromstring(line, dtype=int, sep=' ')
        if monotonic(arr) and inbounds(arr):
            num += 1

print(num)


