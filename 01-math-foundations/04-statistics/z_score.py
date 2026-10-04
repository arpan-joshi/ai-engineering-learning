import numpy as np


data = np.array([
    10, 20, 30, 40, 50
])


mean = np.mean(data)
std = np.std(data)


z_scores = (data - mean) / std


print("Data:", data)
print("Mean:", mean)
print("Standard Deviation:", std)
print("Z-Scores:", z_scores)