# matrices.py

matrix_a = [
    [1, 2],
    [3, 4]
]

matrix_b = [
    [5, 6],
    [7, 8]
]

print("Matrix A:")
for row in matrix_a:
    print(row)

print("\nMatrix B:")
for row in matrix_b:
    print(row)


# Matrix addition
addition = [
    [matrix_a[i][j] + matrix_b[i][j] for j in range(2)]
    for i in range(2)
]

print("\nMatrix Addition:")
for row in addition:
    print(row)


# Matrix subtraction
subtraction = [
    [matrix_a[i][j] - matrix_b[i][j] for j in range(2)]
    for i in range(2)
]

print("\nMatrix Subtraction:")
for row in subtraction:
    print(row)


# Matrix multiplication
multiplication = [
    [
        sum(matrix_a[i][k] * matrix_b[k][j] for k in range(2))
        for j in range(2)
    ]
    for i in range(2)
]

print("\nMatrix Multiplication:")
for row in multiplication:
    print(row)


# Matrix transpose
transpose = [
    [matrix_a[j][i] for j in range(2)]
    for i in range(2)
]

print("\nTranspose:")
for row in transpose:
    print(row)