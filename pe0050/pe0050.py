# Project Euler
# Problem 050
# Philip Davis

import sys
sys.path.append("..")

import euler_utils as eu

primes_l = eu.get_primes()
primes_h = eu.get_primes()
low_primes = []

while sum(low_primes) < 1_000_000:
    low_primes.append(next(primes_l))
low_primes.pop()


totals = {}
for i, _ in enumerate(low_primes):
    s = sum(low_primes[i:])
    if eu.is_prime(s):
        totals[s] = len(low_primes) - i

print(totals)



#p = 0
#high_primes = []
#while p < 1_000_000:
#    p = next(primes_h)
#    high_primes.append(p)
#high_primes.pop()


print(len(low_primes))