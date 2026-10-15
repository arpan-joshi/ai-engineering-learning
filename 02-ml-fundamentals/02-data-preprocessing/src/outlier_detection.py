
import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "sample_data.csv"


def detect_outliers_iqr(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    mask = (series < lower_bound) | (series > upper_bound)

    return {
        "q1": q1,
        "q3": q3,
        "iqr": iqr,
        "lower_bound": lower_bound,
        "upper_bound": upper_bound,
        "mask": mask,
    }


def main():
    df = pd.read_csv(DATA_PATH)

    salary = df["Salary"].dropna()
    result = detect_outliers_iqr(salary)

    print("Q1:", result["q1"])
    print("Q3:", result["q3"])
    print("IQR:", result["iqr"])
    print("Lower bound:", result["lower_bound"])
    print("Upper bound:", result["upper_bound"])

    print("\nPotential salary outliers:")
    print(salary[result["mask"]])


if __name__ == "__main__":
    main()
