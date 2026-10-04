import numpy as np


data = np.array([
    10, 20, 30, 40, 50,
    60, 70, 80, 90, 100
])


q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)


print("Q1:", q1)
print("Q2 / Median:", q2)
print("Q3:", q3)


print("\nPercentiles:")

for p in [10, 25, 50, 75, 90]:
    print(f"{p}th percentile:", np.percentile(data, p))