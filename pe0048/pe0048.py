# Project Euler
# Problem 048
# Philip Davis

import sys
sys.path.append("..")

import euler_utils as eu

def get_last_ten_digits(n: int) -> int:
    return int(str(n)[-10:])

total = 0

for n in range(1, 1001):
    total += get_last_ten_digits(n ** n)
    total = get_last_ten_digits(total)

print(total)