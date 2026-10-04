import numpy as np


data = np.array([
    10, 20, 20, 30, 40,
    50, 60, 70, 80, 90
])


# Exercise 1
print("Mean:", np.mean(data))


# Exercise 2
print("Median:", np.median(data))


# Exercise 3
print("Variance:", np.var(data))


# Exercise 4
print("Standard Deviation:", np.std(data))


# Exercise 5
print("25th Percentile:", np.percentile(data, 25))


# Exercise 6
print("75th Percentile:", np.percentile(data, 75))


# Exercise 7
z_scores = (data - np.mean(data)) / np.std(data)

print("Z-Scores:")
print(z_scores)