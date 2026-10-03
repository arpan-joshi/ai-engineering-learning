import numpy as np


hours_studied = np.array([
    1,
    2,
    3,
    4,
    5
])

exam_score = np.array([
    40,
    50,
    60,
    70,
    80
])


# Covariance
covariance = np.cov(
    hours_studied,
    exam_score
)

# Correlation
correlation = np.corrcoef(
    hours_studied,
    exam_score
)


print("Covariance:")
print(covariance)

print("\nCorrelation:")
print(correlation)