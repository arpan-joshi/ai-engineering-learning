
import pandas as pd
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

DATA_PATH = Path(__file__).parent.parent / "data" / "sample_data.csv"


def main():
    df = pd.read_csv(DATA_PATH)

    # Remove rows where the target is missing.
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

    # The preprocessing steps are fitted only on training data.
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    print("Processed training shape:", X_train_processed.shape)
    print("Processed testing shape:", X_test_processed.shape)

    # A simple baseline model for demonstrating the workflow.
    model = LinearRegression()
    model.fit(X_train_processed, y_train)

    predictions = model.predict(X_test_processed)

    print("\nBaseline regression metrics")
    print("MAE:", mean_absolute_error(y_test, predictions))
    print("RMSE:", mean_squared_error(y_test, predictions) ** 0.5)
    print("R²:", r2_score(y_test, predictions))


if __name__ == "__main__":
    main()
