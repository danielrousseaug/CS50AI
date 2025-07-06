"""Tiny neural network to learn XOR without external dependencies."""

import random

DATA = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0),
]

random.seed(0)


def sigmoid(x: float) -> float:
    import math
    return 1 / (1 + math.exp(-x))


def train(epochs: int = 10000, lr: float = 0.1):
    # two hidden neurons
    w1 = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(2)]
    b1 = [random.uniform(-1, 1) for _ in range(2)]
    w2 = [random.uniform(-1, 1) for _ in range(2)]
    b2 = random.uniform(-1, 1)

    for _ in range(epochs):
        for x, y in DATA:
            # forward pass
            z1 = [w1[i][0] * x[0] + w1[i][1] * x[1] + b1[i] for i in range(2)]
            a1 = [sigmoid(z) for z in z1]
            z2 = sum(w2[i] * a1[i] for i in range(2)) + b2
            a2 = sigmoid(z2)

            # backprop
            dz2 = a2 - y
            for i in range(2):
                w2[i] -= lr * dz2 * a1[i]
            b2 -= lr * dz2
            dz1 = [dz2 * w2[i] * a1[i] * (1 - a1[i]) for i in range(2)]
            for i in range(2):
                for j in range(2):
                    w1[i][j] -= lr * dz1[i] * x[j]
                b1[i] -= lr * dz1[i]

    return w1, w2, b1, b2


def predict(model, x):
    w1, w2, b1, b2 = model
    z1 = [w1[i][0] * x[0] + w1[i][1] * x[1] + b1[i] for i in range(2)]
    a1 = [sigmoid(z) for z in z1]
    z2 = sum(w2[i] * a1[i] for i in range(2)) + b2
    a2 = sigmoid(z2)
    return int(a2 > 0.5)


if __name__ == '__main__':
    model = train()
    results = [predict(model, x) for x, _ in DATA]
    print('Predictions:', results)
