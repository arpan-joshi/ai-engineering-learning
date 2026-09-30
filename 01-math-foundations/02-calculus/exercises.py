# exercises.py

# Exercise 1
# Evaluate f(x) = x^2 + 2x + 1

def function(x):
    return x ** 2 + 2 * x + 1


x = 3

print("Exercise 1:")
print(function(x))


# Exercise 2
# Derivative of f(x) = x^3

def derivative(x):
    return 3 * x ** 2


x = 2

print("\nExercise 2:")
print(derivative(x))


# Exercise 3
# Partial derivatives of:
# f(x,y) = x^2 + y^2

x = 3
y = 4

partial_x = 2 * x
partial_y = 2 * y

print("\nExercise 3:")
print("Partial x:", partial_x)
print("Partial y:", partial_y)


# Exercise 4
# Calculate the gradient

gradient = [2 * x, 2 * y]

print("\nExercise 4:")
print("Gradient:", gradient)


# Exercise 5
# Calculate gradient magnitude

import numpy as np

gradient = np.array(gradient)

print("\nExercise 5:")
print("Gradient magnitude:", np.linalg.norm(gradient))