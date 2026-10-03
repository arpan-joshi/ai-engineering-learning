import numpy as np
import matplotlib.pyplot as plt


# Normal distribution

mean = 0
std = 1

data = np.random.normal(
    mean,
    std,
    1000
)

plt.hist(data, bins=30)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Normal Distribution")

plt.show()