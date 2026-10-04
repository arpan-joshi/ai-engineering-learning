import numpy as np
from scipy import stats


data = np.array([
    48, 50, 52, 49, 51,
    53, 50, 47, 52, 49
])


mean = np.mean(data)

standard_error = stats.sem(data)

confidence_interval = stats.t.interval(
    confidence=0.95,
    df=len(data) - 1,
    loc=mean,
    scale=standard_error
)


print("Mean:", mean)
print("95% Confidence Interval:")
print(confidence_interval)