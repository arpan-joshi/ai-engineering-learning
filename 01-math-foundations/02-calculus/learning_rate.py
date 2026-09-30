# learning_rate.py

def function(x):
    return x ** 2


def derivative(x):
    return 2 * x


learning_rates = [0.01, 0.1, 0.5]

for learning_rate in learning_rates:

    x = 10

    print(f"\nLearning Rate: {learning_rate}")

    for step in range(10):

        gradient = derivative(x)

        x = x - learning_rate * gradient

        print(
            f"Step {step + 1}: "
            f"x = {x:.4f}, "
            f"loss = {function(x):.4f}"
        )