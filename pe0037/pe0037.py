# Project Euler
# Problem 037 - Truncatable Primes
# Philip Davis

import sys
sys.path.append("..")

import euler_utils as eu




def is_left_truncatable(n: int) -> bool:
    n_string = str(n)
    while n_string:
        if not eu.is_prime(int(n_string)):
            return False
        n_string = n_string[1:]
    return True

def is_right_truncatable(n: int) -> bool:
    n_string = str(n)
    while n_string:
        if not eu.is_prime(int(n_string)):
            return False
        n_string = n_string[:-1]
    return True

primes = eu.get_primes()

t_primes = []

while len(t_primes) < 11:
    p = next(primes)
    if len(str(p)) == 1:
        continue
    if is_left_truncatable(p) and is_right_truncatable(p):
        t_primes.append(p)

print(sum(t_primes))