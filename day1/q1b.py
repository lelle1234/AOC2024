#!/usr/bin/python3

import sys
import numpy as np

inf = sys.argv[1]
arr = np.transpose(np.loadtxt(inf, int))
print(sum((arr[1] == x).sum()*x for x in arr[0]))

