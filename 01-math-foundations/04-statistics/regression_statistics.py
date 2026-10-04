import numpy as np
from scipy.stats import linregress


x = np.array([
    1, 2, 3, 4, 5
])

y = np.array([
    2, 4, 5, 8, 10
])


result = linregress(x, y)


print("Slope:", result.slope)
print("Intercept:", result.intercept)
print("R-squared:", result.rvalue ** 2)
print("p-value:", result.pvalue)