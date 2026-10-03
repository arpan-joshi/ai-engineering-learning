import numpy as np
import matplotlib.pyplot as plt


# Generate random values between 0 and 1

samples = np.random.uniform(
    0,
    1,
    1000
)

plt.hist(
    samples,
    bins=20
)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Uniform Distribution")

plt.show()