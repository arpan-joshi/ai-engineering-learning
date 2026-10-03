import numpy as np


# Function
# f(x, y) = x² + y²
def f(x, y):
    return x**2 + y**2


# Gradient of f
# ∇f = [2x, 2y]
def gradient(x, y):
    return np.array([
        2 * x,
        2 * y
    ])


# Directional derivative
def directional_derivative(x, y, direction):
    
    # Convert direction to NumPy array
    direction = np.array(direction, dtype=float)

    # Convert direction into unit vector
    unit_direction = direction / np.linalg.norm(direction)

    # Calculate gradient
    grad = gradient(x, y)

    # Directional derivative
    result = np.dot(grad, unit_direction)

    return result


# Point
x = 2
y = 3

# Direction
direction = [1, 1]

result = directional_derivative(x, y, direction)

print("Point:", (x, y))
print("Direction:", direction)
print("Directional Derivative:", result)