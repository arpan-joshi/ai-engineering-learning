# determinant.py

import numpy as np

A = np.array([
    [2, 3],
    [1, 4]
])

print("Matrix A:")
print(A)

# Calculate determinant
det = np.linalg.det(A)

print("\nDeterminant:")
print(det)


# Calculate manually for 2x2 matrix
a = A[0][0]
b = A[0][1]
c = A[1][0]
d = A[1][1]

manual_det = (a * d) - (b * c)

print("\nManual determinant:")
print(manual_det)