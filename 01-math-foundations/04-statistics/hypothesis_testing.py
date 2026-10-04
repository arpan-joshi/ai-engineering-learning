import numpy as np
from scipy.stats import ttest_1samp


data = np.array([
    52, 49, 51, 53, 50,
    48, 52, 51, 49, 50
])


# Test whether mean is different from 50
t_statistic, p_value = ttest_1samp(
    data,
    50
)


print("T-statistic:", t_statistic)
print("p-value:", p_value)


alpha = 0.05


if p_value < alpha:
    print("Reject the null hypothesis.")

else:
    print("Fail to reject the null hypothesis.")