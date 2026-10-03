import numpy as np
import matplotlib.pyplot as plt


# Average number of events
lambda_value = 4

samples = np.random.poisson(
    lambda_value,
    1000
)

plt.hist(
    samples,
    bins=range(0, 15),
    align="left",
    rwidth=0.8
)

plt.xlabel("Number of Events")
plt.ylabel("Frequency")
plt.title("Poisson Distribution")

plt.show()