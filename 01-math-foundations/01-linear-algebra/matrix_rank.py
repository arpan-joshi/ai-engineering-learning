# matrix_rank.py

import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [1, 2],
    [2, 4]
])

print("Matrix A:")
print(A)

print("\nRank of A:")
print(np.linalg.matrix_rank(A))


print("\nMatrix B:")
print(B)

print("\nRank of B:")
print(np.linalg.matrix_rank(B))