#!/bin/python3

import re
import sys

def flatten(xss):
    return [x for xs in xss for x in xs]

inf = sys.argv[1]
ans = 0
enabled = True
with open(inf, "r") as f:
    s = f.read().strip()
    arr = s.split("don't()")
    arr[0] = 'do()' + arr[0]
    arr = [ x+"do()" for x in arr ] # append do() at end of each part, safety
    rem = [ x[x.index("do()"):] for x in arr ] # find first occ off "do()" elemwise
    xxx = flatten([ re.findall(r"(mul\(\d+,\d+\))", x) for x in rem ])
    for tok in xxx:
        x = re.findall(r"\d+", tok)
        ans += int(x[0])*int(x[1])
print(ans)    


