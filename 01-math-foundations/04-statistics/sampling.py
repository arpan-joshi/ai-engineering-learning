import numpy as np


population = np.arange(1, 101)


sample = np.random.choice(
    population,
    size=10,
    replace=False
)


print("Population:")
print(population)

print("\nSample:")
print(sample)

print("\nPopulation Mean:", np.mean(population))
print("Sample Mean:", np.mean(sample))