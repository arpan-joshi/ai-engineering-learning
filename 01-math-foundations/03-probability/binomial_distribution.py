import numpy as np
import matplotlib.pyplot as plt


# Number of trials
n = 10

# Probability of success
p = 0.5

# Generate samples
samples = np.random.binomial(
    n=n,
    p=p,
    size=1000
)

plt.hist(
    samples,
    bins=range(0, n + 2),
    align="left",
    rwidth=0.8
)

plt.xlabel("Number of Successes")
plt.ylabel("Frequency")
plt.title("Binomial Distribution")

plt.show()