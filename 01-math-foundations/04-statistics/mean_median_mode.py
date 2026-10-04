import numpy as np
from collections import Counter


data = np.array([
    10, 20, 20, 30, 40, 50
])


# Mean
mean = np.mean(data)

# Median
median = np.median(data)

# Mode
counts = Counter(data)
mode = counts.most_common(1)[0][0]


print("Data:", data)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)