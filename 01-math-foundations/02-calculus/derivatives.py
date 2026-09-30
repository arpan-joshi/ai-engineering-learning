# derivatives.py

import numpy as np


# Function:
# f(x) = x^2

def function(x):
    return x ** 2


# Analytical derivative:
# f'(x) = 2x

def derivative(x):
    return 2 * x


x = 5

print("Function value:")
print(function(x))

print("\nDerivative:")
print(derivative(x))


# Numerical derivative

def numerical_derivative(function, x, h=0.0001):
    return (function(x + h) - function(x - h)) / (2 * h)


print("\nNumerical Derivative:")
print(numerical_derivative(function, x))