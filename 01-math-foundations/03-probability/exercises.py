import numpy as np


# Exercise 1
# A dice is rolled once.
# What is the probability of getting an even number?

even_probability = 3 / 6

print("Exercise 1:")
print(even_probability)


# Exercise 2
# Calculate mean

data = np.array([10, 20, 30, 40, 50])

print("\nExercise 2:")
print("Mean:", np.mean(data))


# Exercise 3
# Calculate variance

print("\nExercise 3:")
print("Variance:", np.var(data))


# Exercise 4
# Calculate standard deviation

print("\nExercise 4:")
print("Standard Deviation:", np.std(data))


# Exercise 5
# Calculate probability of A and B
# Assume independent events

p_a = 0.3
p_b = 0.5

print("\nExercise 5:")
print("P(A and B):", p_a * p_b)