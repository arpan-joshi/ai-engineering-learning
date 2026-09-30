# limits.py

def function(x):
    return (x ** 2 - 1) / (x - 1)


values = [
    0.9,
    0.99,
    0.999,
    1.001,
    1.01,
    1.1
]

print("Approaching x = 1:\n")

for x in values:
    print(f"x = {x}, f(x) = {function(x)}")