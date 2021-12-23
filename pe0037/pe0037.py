# Project Euler
# Problem 037 - Truncatable Primes
# Philip Davis

from itertools import permutations

from .. import euler_utils as eu

prime_digits = {3, 7, 9}


primes = []
for n in eu.get_primes():
    primes.append(n)
    if len(primes) >= 11:
        break