#!/usr/bin/python3

import sys
import numpy as np

inf = sys.argv[1]
arr = np.loadtxt(inf, int)
monotonic = lambda r: np.all(np.diff(r) < 0) | np.all(np.diff(r) > 0)
inbounds = lambda r: np.all(abs(np.diff(r)) >= 1) & np.all(abs(np.diff(r)) <= 3)
print(len([ row for row in arr if monotonic(row) and inbounds(row)]))


