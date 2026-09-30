# optimization.py

def function(x):
    return x ** 2


def derivative(x):
    return 2 * x


x = 5
learning_rate = 0.1

print("Starting point:", x)
print("Starting loss:", function(x))

for step in range(20):

    gradient = derivative(x)

    x = x - learning_rate * gradient

    print(
        f"Step {step + 1}: "
        f"x = {x:.5f}, "
        f"loss = {function(x):.5f}"
    )

print("\nFinal point:", x)
print("Final loss:", function(x))