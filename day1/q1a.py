#!/usr/bin/python3

import sys
import numpy as np

inf = sys.argv[1]
arr = np.transpose(np.loadtxt(inf, int))
print(sum(abs(np.sort(arr[0]) - np.sort(arr[1]))))


