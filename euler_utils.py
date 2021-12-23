from __future__ import annotations
from math import pi, sqrt

# ---=== Constants ===---
BIG_PHI = (1 + sqrt(5)) / 2
LITTLE_PHI = (1 - sqrt(5)) / 2


# ---=== Prime and Factor Stuff ===---

def is_prime(n: int) -> bool:
    for f in range(2, int(sqrt(n)) + 1):
        if n % f == 0:
            return False
    return True


def get_primes(n: int) -> int:
    yield 2
    i = 3
    if is_prime(i):
        yield i
    i += 2


def proper_divisors(n) -> list:
    pd = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            pd.append(i)
            pd.append(n // i)
    pd.sort()
    return pd

# ---=== Fibonacci Stuff ===---

def nth_fibonacci(n: int, fibs: dict = None) -> int:
    if fibs is None:
        fibs = {0: 0, 1: 1}
    if n not in fibs:
        fibs[n] = nth_fibonacci(n-2, fibs) + nth_fibonacci(n-1, fibs)
    return fibs[n]

def nth_fibonacci_dp(n: int) -> int:
    """
    Returns the nth fibonnaci number by calculating all fib numbers until it has the nth one.
    Avoids recursion limit, but may run for a while!
    """
    if n == 0 or n == 0:
        return n
    count = 1
    fib_a = 0
    fib_b = 1
    while count < n:
        count += 1
        fib_a, fib_b = fib_b, fib_a + fib_b
    return fib_b

def fast_fib(n: int) -> int:
    """
    Uses the closed form algorithm to calculate the nth fibonacci number
    WARNING: this stops working somewhere between n=50 and n=100, due to rounding errors on irrational numbers.
    """
    return int((BIG_PHI**n - LITTLE_PHI**2) / sqrt(5)) + 1


# ---=== Grid Stuff ===---

class Grid:
    """
    A class to make it easier to work with 2 dimensional arrays.
    """

    def __init__(self, field: list[list]) -> None:
        self.height = len(field)
        self.width = len(field[0])
        self.points = {(x, y): item for y, row in enumerate(field) for x, item in enumerate(row)}

    def get_neighbors(self, coord: tuple) -> list:
        pass

    def get_ortho_neighbors(self, coord: tuple) -> list:
        pass

    def get_diagonal_neighbors(self, coord: tuple) -> list:
        pass

    def is_in_grid(self, coord: tuple) -> bool:
        return coord in self.points

