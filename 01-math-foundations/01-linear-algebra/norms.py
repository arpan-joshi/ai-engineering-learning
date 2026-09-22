# norms.py

import math

vector = [3, 4]

print("Vector:", vector)


# L1 Norm
l1_norm = sum(abs(x) for x in vector)

print("L1 Norm:", l1_norm)


# L2 Norm
l2_norm = math.sqrt(sum(x ** 2 for x in vector))

print("L2 Norm:", l2_norm)


# Infinity Norm
infinity_norm = max(abs(x) for x in vector)

print("Infinity Norm:", infinity_norm)


import numpy as np

v = np.array([3, 4])

print("\nUsing NumPy:")
print("L1 Norm:", np.linalg.norm(v, ord=1))
print("L2 Norm:", np.linalg.norm(v, ord=2))
print("Infinity Norm:", np.linalg.norm(v, ord=np.inf))