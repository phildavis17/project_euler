# Project Euler
# Problem 044 - Pentagonal Numbers
# Philip Davis

import sys
sys.path.append("..")

import euler_utils as eu

def pent(n: int) -> int:
    return (n * (3 * n - 1)) // 2

pents = {pent(n) for n in range(1, 10001)}

diffs = set()

for n in pents:
    for m in pents:
        if n == m:
            continue
        if n - m in pents:
            diffs.add((n, m))

sums = set()
for p in diffs:
    n, m = p
    if n + m in pents:
        sums.add(p)

print(sums)