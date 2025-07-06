"""Example of hill climbing optimization."""

import random


def hill_climb(f, start: float, step: float = 0.1, iterations: int = 1000):
    x = start
    for _ in range(iterations):
        neighbors = [x - step, x + step]
        x = max(neighbors, key=f)
    return x


if __name__ == '__main__':
    f = lambda x: -(x - 3) ** 2 + 5  # maximum at x=3
    best = hill_climb(f, random.uniform(-10, 10))
    print('Best x:', best)
