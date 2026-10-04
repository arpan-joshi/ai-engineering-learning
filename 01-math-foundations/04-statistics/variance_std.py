import numpy as np


data = np.array([
    10, 20, 30, 40, 50
])


mean = np.mean(data)

variance = np.var(data)

standard_deviation = np.std(data)


print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)