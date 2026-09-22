# eigenvectors.py

import numpy as np

matrix = np.array([
    [2, 0],
    [0, 3]
])

print("Matrix:")
print(matrix)


# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)


# Verify Av = lambda*v

for i in range(len(eigenvalues)):
    eigenvalue = eigenvalues[i]
    eigenvector = eigenvectors[:, i]

    left_side = matrix @ eigenvector
    right_side = eigenvalue * eigenvector

    print(f"\nEigenvalue {i + 1}: {eigenvalue}")
    print("A × v:", left_side)
    print("λ × v:", right_side)

    print("Verified:", np.allclose(left_side, right_side))