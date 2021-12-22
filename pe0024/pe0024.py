# Project Euler
# Problem 024 - Lexicographic Permutations
# Philip Davis

#import euler_utils as eu

from itertools import permutations


perms = permutations("0123456789")

for _ in range(1000000):
    p = "".join(next(perms))

print(p)

