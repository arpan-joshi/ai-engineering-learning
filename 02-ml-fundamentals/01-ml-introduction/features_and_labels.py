import numpy as np

# Each row represents one house.
# Columns: area (sq ft), bedrooms

X = np.array([
    [1000, 2],
    [1500, 3],
    [2000, 3],
    [2500, 4]
])

# Target prices
y = np.array([
    200000,
    300000,
    400000,
    500000
])

print("Features (X):")
print(X)

print("\nLabels (y):")
print(y)

print("\nNumber of houses:", X.shape[0])
print("Number of features:", X.shape[1])
print("Number of labels:", y.shape[0])