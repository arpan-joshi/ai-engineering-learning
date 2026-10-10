from sklearn.model_selection import train_test_split

# Example dataset
X = [
    [1000, 2],
    [1200, 2],
    [1500, 3],
    [1800, 3],
    [2000, 3],
    [2200, 4],
    [2500, 4],
    [2800, 4],
    [3000, 5],
    [3200, 5]
]

y = [
    200000, 240000, 300000, 360000, 400000,
    440000, 500000, 560000, 600000, 640000
]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training examples:", len(X_train))
print("Testing examples:", len(X_test))

print("\nTraining features:", X_train)
print("Testing features:", X_test)