
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

DATA_PATH = Path(__file__).parent.parent / "data" / "sample_data.csv"


def main():
    df = pd.read_csv(DATA_PATH)

    # Demonstration target: predict Salary from other features.
    # In a real project, choose a target that matches the problem.
    df = df.dropna(subset=["Salary"])

    X = df[["Age", "Experience", "City", "Education"]]
    y = df["Salary"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    numeric_features = ["Age", "Experience"]
    categorical_features = ["City", "Education"]

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ])

    preprocessor = ColumnTransformer([
        ("numeric", numeric_pipeline, numeric_features),
        ("categorical", categorical_pipeline, categorical_features),
    ])

    # Fit transformations on training data only.
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    print("Training rows:", len(X_train))
    print("Testing rows:", len(X_test))
    print("Training shape:", X_train_processed.shape)
    print("Testing shape:", X_test_processed.shape)

    print("\nTraining target:")
    print(y_train.to_list())

    print("\nTesting target:")
    print(y_test.to_list())


if __name__ == "__main__":
    main()
