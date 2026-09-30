# gradients.py

import numpy as np


def function(x, y):
    return x ** 2 + y ** 2


def gradient(x, y):
    return np.array([
        2 * x,
        2 * y
    ])


x = 3
y = 4

print("Function value:")
print(function(x, y))

print("\nGradient:")
print(gradient(x, y))


gradient_vector = gradient(x, y)

magnitude = np.linalg.norm(gradient_vector)

print("\nGradient magnitude:")
print(magnitude)