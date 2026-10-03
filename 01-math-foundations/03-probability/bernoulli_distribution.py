import numpy as np
import matplotlib.pyplot as plt


# Bernoulli distribution
# 0 = Failure
# 1 = Success

p = 0.7

samples = np.random.binomial(
    n=1,
    p=p,
    size=1000
)

values, counts = np.unique(
    samples,
    return_counts=True
)

print("Values:", values)
print("Counts:", counts)

plt.bar(values, counts)

plt.xlabel("Outcome")
plt.ylabel("Frequency")
plt.title("Bernoulli Distribution")

plt.show()