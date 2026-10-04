import numpy as np
from scipy.stats import skew


data = np.array([
    10, 11, 12, 13, 14,
    15, 16, 17, 50
])


skewness = skew(data)


print("Data:", data)
print("Skewness:", skewness)


if skewness > 0:
    print("Distribution is positively skewed.")

elif skewness < 0:
    print("Distribution is negatively skewed.")

else:
    print("Distribution is approximately symmetric.")