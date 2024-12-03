#!/usr/bin/python3

import sys
import numpy as np
from itertools import chain, combinations

inf = sys.argv[1]
arr = np.loadtxt(inf, int)
monotonic = lambda r: np.all(np.diff(r) < 0) | np.all(np.diff(r) > 0)
inbounds = lambda r: np.all(abs(np.diff(r)) >= 1) & np.all(abs(np.diff(r)) <= 3)
for r in range(2):
    print([ row for row in combinations(arr, len(arr)-r) if monotonic(row) and inbounds(row) ])


