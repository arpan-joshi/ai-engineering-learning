import pandas as pd
from pathlib import Path
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

DATA_PATH = Path(__file__).parent.parent / "data" / "sample_data.csv"


def manual_one_hot_encoding(series):
    """One-hot encode a single categorical column using Pandas."""
    return pd.get_dummies(series, dtype=int)


def main():
    df = pd.read_csv(DATA_PATH)

    city_encoded = manual_one_hot_encoding(df["City"])

    print("Manual one-hot encoding:")
    print(city_encoded.head())

    # Scikit-learn one-hot encoding
    encoder = OneHotEncoder(
        handle_unknown="ignore",
        sparse_output=False
    )

    city_array = encoder.fit_transform(df[["City"]])

    encoded_df = pd.DataFrame(
        city_array,
        columns=encoder.get_feature_names_out(["City"])
    )

    print("\nScikit-learn encoding:")
    print(encoded_df.head())

    # Ordinal encoding: categories have a meaningful order.
    education_encoder = OrdinalEncoder(
        categories=[["Bachelor", "Master", "PhD"]]
    )

    education_encoded = education_encoder.fit_transform(
        df[["Education"]]
    )

    print("\nOrdinal-encoded education:")
    print(education_encoded.ravel())


if __name__ == "__main__":
    main()
