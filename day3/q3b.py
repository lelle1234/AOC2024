#!/bin/python3

import re
import sys

def flatten(xss):
    return [x for xs in xss for x in xs]

def safe_index(source, search):
    try:
        return source.index(search)
    except:
        return len(source)-1

inf = sys.argv[1]
ans = 0
enabled = True
with open(inf, "r") as f:
    s = f.read().strip()
    arr = s.split("don't()")
    arr[0] = 'do()' + arr[0]
    # find first occ off "do()" elemwise
    rem = [ x[safe_index(x,"do()"):] for x in arr ] 
    xxx = flatten([ re.findall(r"(mul\(\d+,\d+\))", x) for x in rem ])
    for tok in xxx:
        x = re.findall(r"\d+", tok)
        ans += int(x[0])*int(x[1])
print(ans)    


