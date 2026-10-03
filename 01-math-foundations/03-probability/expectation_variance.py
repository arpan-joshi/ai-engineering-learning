import numpy as np


data = np.array([
    2,
    4,
    6,
    8,
    10
])


# Mean / Expected value
mean = np.mean(data)

# Variance
variance = np.var(data)

# Standard deviation
std = np.std(data)


print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std)