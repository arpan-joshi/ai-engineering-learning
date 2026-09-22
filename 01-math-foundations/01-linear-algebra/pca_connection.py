# pca_connection.py

import numpy as np
from sklearn.decomposition import PCA

# Simple dataset
X = np.array([
    [1, 2],
    [2, 4],
    [3, 6],
    [4, 8],
    [5, 10]
])

print("Original Data:")
print(X)


# Apply PCA
pca = PCA(n_components=1)

X_reduced = pca.fit_transform(X)

print("\nReduced Data:")
print(X_reduced)


# Explained variance
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)