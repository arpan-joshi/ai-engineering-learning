# gradient_descent.py

# Function:
# f(x) = x^2
#
# Derivative:
# f'(x) = 2x


def function(x):
    return x ** 2


def derivative(x):
    return 2 * x


x = 10
learning_rate = 0.1

print("Starting x:", x)

for step in range(10):

    gradient = derivative(x)

    x = x - learning_rate * gradient

    print(
        f"Step {step + 1}: "
        f"x = {x:.4f}, "
        f"loss = {function(x):.4f}"
    )


# gradient_descent.py

def function(x):
    return x ** 2


def derivative(x):
    return 2 * x


x = 10
learning_rate = 0.1

for step in range(100):

    gradient = derivative(x)

    x = x - learning_rate * gradient

    if abs(gradient) < 0.001:
        break

print("Final x:", x)
print("Final loss:", function(x))
print("Steps:", step + 1)