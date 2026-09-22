# eigenvalues.py

import numpy as np

matrix = np.array([
    [2, 0],
    [0, 3]
])

print("Matrix:")
print(matrix)


# Calculate eigenvalues
eigenvalues = np.linalg.eigvals(matrix)

print("\nEigenvalues:")
print(eigenvalues)