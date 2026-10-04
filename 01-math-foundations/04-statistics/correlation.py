import numpy as np


hours_studied = np.array([
    1, 2, 3, 4, 5
])

scores = np.array([
    40, 50, 60, 70, 80
])


correlation = np.corrcoef(
    hours_studied,
    scores
)[0, 1]


print("Correlation:", correlation)