import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler, StandardScaler

DATA_PATH = Path(__file__).parent.parent / "data" / "sample_data.csv"


def manual_min_max_scaling(values):
    minimum = np.min(values, axis=0)
    maximum = np.max(values, axis=0)
    denominator = maximum - minimum

    # Handle constant features safely.
    denominator = np.where(denominator == 0, 1, denominator)

    return (values - minimum) / denominator


def manual_standardization(values):
    mean = np.mean(values, axis=0)
    std = np.std(values, axis=0)

    # Avoid division by zero for constant features.
    std = np.where(std == 0, 1, std)

    return (values - mean) / std


def main():
    df = pd.read_csv(DATA_PATH)
    X = df[["Age", "Salary", "Experience"]].copy()

    # For this demonstration only, fill missing values with
    # column medians. Learn train-only fitting in the pipeline file.
    X = X.fillna(X.median())
    values = X.to_numpy(dtype=float)

    print("Original values:")
    print(values[:5])

    print("\nManual Min-Max scaling:")
    print(manual_min_max_scaling(values)[:5])

    print("\nManual standardization:")
    print(manual_standardization(values)[:5])

    scaler = MinMaxScaler()
    print("\nScikit-learn Min-Max:")
    print(scaler.fit_transform(values)[:5])

    standard_scaler = StandardScaler()
    print("\nScikit-learn standardization:")
    print(standard_scaler.fit_transform(values)[:5])


if __name__ == "__main__":
    main()
