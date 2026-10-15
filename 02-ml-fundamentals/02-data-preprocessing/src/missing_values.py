import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "sample_data.csv"


def load_data():
    return pd.read_csv(DATA_PATH)


def inspect_missing_values(df):
    print("Missing values per column:")
    print(df.isnull().sum())

    print("\nMissing percentage:")
    print((df.isnull().mean() * 100).round(2))


def manual_median_imputation(series):
    """Fill missing numeric values using the median."""
    values = sorted(series.dropna().tolist())

    if not values:
        raise ValueError("Cannot impute a column with no valid values.")

    n = len(values)
    mid = n // 2

    if n % 2 == 0:
        median = (values[mid - 1] + values[mid]) / 2
    else:
        median = values[mid]

    return series.fillna(median)


def preprocess_missing_values(df):
    df = df.copy()

    numeric_cols = ["Age", "Salary", "Experience"]

    for col in numeric_cols:
        df[col] = manual_median_imputation(df[col])

    # Fill categorical values with the most frequent category.
    for col in ["City", "Education"]:
        mode = df[col].mode()

        if not mode.empty:
            df[col] = df[col].fillna(mode.iloc[0])

    return df


if __name__ == "__main__":
    df = load_data()

    inspect_missing_values(df)

    cleaned_df = preprocess_missing_values(df)

    print("\nCleaned dataset:")
    print(cleaned_df)

    print("\nRemaining missing values:")
    print(cleaned_df.isnull().sum())
