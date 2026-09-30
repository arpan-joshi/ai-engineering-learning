# loss_functions.py

import numpy as np


def mean_squared_error(y_true, y_pred):
    errors = y_true - y_pred
    squared_errors = errors ** 2

    return np.mean(squared_errors)


y_true = np.array([10, 20, 30])
y_pred = np.array([12, 18, 29])

loss = mean_squared_error(y_true, y_pred)

print("Actual values:")
print(y_true)

print("\nPredicted values:")
print(y_pred)

print("\nMean Squared Error:")
print(loss)