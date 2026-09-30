# continuity.py

def function(x):
    return x ** 2


values = [0.9, 0.99, 1.0, 1.01, 1.1]

print("Continuous function: f(x) = x²\n")

for x in values:
    print(f"x = {x}, f(x) = {function(x)}")