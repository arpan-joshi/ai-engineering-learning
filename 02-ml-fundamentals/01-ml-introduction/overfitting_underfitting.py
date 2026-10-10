# Understanding model fit

models = {
    "Underfitting": {
        "training_error": 30,
        "testing_error": 32
    },
    "Good Fit": {
        "training_error": 8,
        "testing_error": 10
    },
    "Overfitting": {
        "training_error": 1,
        "testing_error": 25
    }
}

for name, errors in models.items():
    print(f"\n{name}")
    print("Training error:", errors["training_error"])
    print("Testing error:", errors["testing_error"])