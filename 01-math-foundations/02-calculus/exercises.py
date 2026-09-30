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


# -------------------------
# Exercise 6 - Chain Rule
# -------------------------

def chain_function(x):
    return (3 * x + 2) ** 2


def chain_derivative(x):
    return 6 * (3 * x + 2)


x = 2

print("\nExercise 6 - Chain Rule:")
print("Function:", chain_function(x))
print("Derivative:", chain_derivative(x))


# -------------------------
# Exercise 7 - MSE
# -------------------------

import numpy as np

actual = np.array([10, 20, 30])
predicted = np.array([11, 19, 28])

mse = np.mean((actual - predicted) ** 2)

print("\nExercise 7 - MSE:")
print(mse)


# -------------------------
# Exercise 8 - Gradient Descent
# -------------------------

def function(x):
    return x ** 2


def derivative(x):
    return 2 * x


x = 5
learning_rate = 0.1

for _ in range(20):
    x = x - learning_rate * derivative(x)

print("\nExercise 8 - Gradient Descent:")
print("Final x:", x)
print("Final loss:", function(x))


# -------------------------
# Exercise 9 - Limit
# -------------------------

def limit_function(x):
    return (x ** 2 - 1) / (x - 1)


print("\nExercise 9 - Limit:")

for x in [0.9, 0.99, 1.01, 1.1]:
    print(x, limit_function(x))


# -------------------------
# Exercise 10 - Optimization
# -------------------------

def function(x):
    return x ** 2


def derivative(x):
    return 2 * x


x = 8
learning_rate = 0.1

for _ in range(20):
    x = x - learning_rate * derivative(x)

print("\nExercise 10 - Optimization:")
print("Final x:", x)
print("Final loss:", function(x))


# -------------------------
# Exercise 11 - Learning Rate
# -------------------------

learning_rates = [0.01, 0.1, 0.5]

print("\nExercise 11 - Learning Rates:")

for learning_rate in learning_rates:

    x = 10

    for _ in range(20):
        x = x - learning_rate * derivative(x)

    print(
        f"Learning rate: {learning_rate}, "
        f"Final x: {x:.5f}, "
        f"Loss: {function(x):.5f}"
    )