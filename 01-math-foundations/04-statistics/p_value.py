from scipy.stats import ttest_1samp
import numpy as np


data = np.array([
    52, 54, 51, 53, 55,
    52, 54, 53, 51, 55
])


t_statistic, p_value = ttest_1samp(
    data,
    50
)


print("T-statistic:", t_statistic)
print("p-value:", p_value)


if p_value < 0.05:
    print("Statistically significant result.")

else:
    print("Not statistically significant.")