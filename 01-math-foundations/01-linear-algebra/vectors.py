# vectors.py

# Two vectors
vector_a = [1, 2, 3]
vector_b = [4, 5, 6]

print("Vector A:", vector_a)
print("Vector B:", vector_b)


# Vector addition
addition = [a + b for a, b in zip(vector_a, vector_b)]

print("Addition:", addition)


# Vector subtraction
subtraction = [a - b for a, b in zip(vector_a, vector_b)]

print("Subtraction:", subtraction)


# Scalar multiplication
scalar = 2

scalar_multiplication = [scalar * x for x in vector_a]

print("Scalar Multiplication:", scalar_multiplication)


# Dot product
dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

print("Dot Product:", dot_product)