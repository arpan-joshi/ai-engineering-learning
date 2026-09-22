# exercises.py

# Exercise 1
# Add two vectors

vector_a = [2, 4, 6]
vector_b = [1, 3, 5]

addition = [a + b for a, b in zip(vector_a, vector_b)]

print("Exercise 1 - Vector Addition:")
print(addition)


# Exercise 2
# Calculate the dot product

dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

print("\nExercise 2 - Dot Product:")
print(dot_product)


# Exercise 3
# Multiply a vector by 3

result = [3 * x for x in vector_a]

print("\nExercise 3 - Scalar Multiplication:")
print(result)


# Exercise 4
# Find the transpose of a matrix

matrix = [
    [1, 2],
    [3, 4]
]

transpose = [
    [matrix[j][i] for j in range(2)]
    for i in range(2)
]

print("\nExercise 4 - Matrix Transpose:")
for row in transpose:
    print(row)


# Exercise 5
# Add two matrices

matrix_a = [
    [1, 2],
    [3, 4]
]

matrix_b = [
    [5, 6],
    [7, 8]
]

result = [
    [matrix_a[i][j] + matrix_b[i][j] for j in range(2)]
    for i in range(2)
]

print("\nExercise 5 - Matrix Addition:")
for row in result:
    print(row)
    break


# -------------------------
# Eigenvalue Exercise
# -------------------------

import numpy as np

matrix = np.array([
    [4, 0],
    [0, 5]
])

eigenvalues = np.linalg.eigvals(matrix)

print("\nExercise 6 - Eigenvalues:")
print(eigenvalues)


# -------------------------
# Eigenvector Exercise
# -------------------------

eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("\nExercise 7 - Eigenvectors:")
print(eigenvectors)


# -------------------------
# Norm Exercise
# -------------------------

vector = np.array([6, 8])

l1 = np.linalg.norm(vector, ord=1)
l2 = np.linalg.norm(vector, ord=2)
linf = np.linalg.norm(vector, ord=np.inf)

print("\nExercise 8 - Norms:")
print("L1:", l1)
print("L2:", l2)
print("Infinity:", linf)

# -------------------------
# Exercise 9 - Determinant
# -------------------------

import numpy as np

A = np.array([
    [3, 2],
    [1, 4]
])

det = np.linalg.det(A)

print("\nExercise 9 - Determinant:")
print(det)


# -------------------------
# Exercise 10 - Matrix Inverse
# -------------------------

A_inverse = np.linalg.inv(A)

print("\nExercise 10 - Matrix Inverse:")
print(A_inverse)

print("\nVerification:")
print(A_inverse @ A)


# -------------------------
# Exercise 11 - Matrix Rank
# -------------------------

B = np.array([
    [1, 2],
    [2, 4]
])

rank = np.linalg.matrix_rank(B)

print("\nExercise 11 - Matrix Rank:")
print(rank)


# -------------------------
# Exercise 12 - PCA
# -------------------------

from sklearn.decomposition import PCA

X = np.array([
    [1, 2],
    [2, 4],
    [3, 6],
    [4, 8],
    [5, 10]
])

pca = PCA(n_components=1)

X_reduced = pca.fit_transform(X)

print("\nExercise 12 - PCA:")
print(X_reduced)

print("\nExplained Variance:")
print(pca.explained_variance_ratio_)