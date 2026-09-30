# partial_derivatives.py

def function(x, y):
    return x ** 2 + y ** 2


def partial_x(x, y):
    return 2 * x


def partial_y(x, y):
    return 2 * y


x = 3
y = 4

print("Function value:")
print(function(x, y))

print("\nPartial derivative with respect to x:")
print(partial_x(x, y))

print("\nPartial derivative with respect to y:")
print(partial_y(x, y))