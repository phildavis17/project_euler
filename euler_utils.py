from __future__ import annotations
from math import pi, sqrt

BIG_PHI = (1 + sqrt(5)) / 2
LITTLE_PHI = (1 - sqrt(5)) / 2

def is_prime(n: int) -> bool:
    for f in range(2, int(sqrt(n)) + 1):
        if n % f == 0:
            return False
    return True


def get_primes(n: int) -> int:
    pass


def nth_fibonacci(n: int, fibs: dict = None) -> int:
    if fibs is None:
        fibs = {0: 0, 1: 1}
    if n not in fibs:
        fibs[n] = nth_fibonacci(n-2, fibs) + nth_fibonacci(n-1, fibs)
    return fibs[n]

def fast_fib(n: int) -> int:
    return int((BIG_PHI**n - LITTLE_PHI**2) / sqrt(5)) + 1


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

