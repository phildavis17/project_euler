# Project Euler
# Problem 049 - Prime Permutations
# Philip Davis

import sys
sys.path.append("..")

from collections import defaultdict
from itertools import permutations

import euler_utils as eu

primes = eu.get_primes()
p = next(primes)
four_digit_primes = set()
while len(str(p)) < 5:
    #if len(set(str(p))) == 4:
    four_digit_primes.add(p)
    p = next(primes)


digit_sets = defaultdict(list)

for n in four_digit_primes:
    s = frozenset(str(n))
    digit_sets[s].append(n)

diffs = []
digit_sets = {k: v for k, v in digit_sets.items() if len(v) >= 3}
for s in digit_sets.values():
    s.sort()
    dif_count = defaultdict(int)
    for p in s:
        for op in s:
            if p == op:
                continue
            d = abs(p - op)
            dif_count[d] += 1
    for n, c in dif_count.items():
        if c >= 3:
            diffs.append((s, n))

actual_count = []
for p_list, dif_int in diffs:
    local_count = set()
    for p in p_list:
        if p + dif_int in p_list and p + 2 * dif_int in p_list:
            local_count.add(p)
            local_count.add(p + dif_int)
            local_count.add(p + 2 * dif_int)
    if local_count:
        actual_count.append((dif_int, local_count))
for i in actual_count:
    print(i)




#potentials = []
#dif_set = defaultdict(set)
#for p_list in digit_sets.values():
#    comps = zip(p_list, p_list[1:])
#    for c in comps:
#        diff = abs(c[0] - c[1])
#        dif_set[diff].add(c[0])
#        dif_set[diff].add(c[1])



