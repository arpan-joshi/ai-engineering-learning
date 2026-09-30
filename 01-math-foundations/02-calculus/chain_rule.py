# chain_rule.py

# Function:
# y = (2x + 1)^2

def function(x):
    return (2 * x + 1) ** 2


# Derivative using the chain rule:
# dy/dx = 2(2x + 1) * 2
#       = 4(2x + 1)

def derivative(x):
    return 4 * (2 * x + 1)


x = 3

print("Function value:")
print(function(x))

print("\nDerivative using chain rule:")
print(derivative(x))