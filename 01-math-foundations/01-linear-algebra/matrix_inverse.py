# matrix_inverse.py

import numpy as np

A = np.array([
    [2, 1],
    [1, 1]
])

print("Matrix A:")
print(A)

# Calculate inverse
A_inverse = np.linalg.inv(A)

print("\nInverse of A:")
print(A_inverse)

# Identity matrix
identity = A_inverse @ A

print("\nA_inverse @ A:")
print(identity)