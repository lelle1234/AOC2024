#!/bin/python3

import re
import sys

inf = sys.argv[1]
with open(inf, "r") as f:
    res = 0
    for line in f:
        s=re.findall(r"(mul\(\d+,\d+\))", line)
        for tok in s:
            x = re.findall(r"\d+", tok)
            res += int(x[0])*int(x[1])
print(res)
