from __future__ import annotations
from _typeshed import Self
from math import sqrt

def is_prime(n: int) -> bool:
    for f in range(1, int(sqrt(n)) + 1):
        if n % f == 0:
            return False
    return True


def get_primes(n: int) -> int:
    pass


def nth_fibonacci(n: int) -> int:
    fibs = {0: 0, 1: 1}
    



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

    def is_in_grid(self, coord: tuple) -> bool:
        return coord in self.points

