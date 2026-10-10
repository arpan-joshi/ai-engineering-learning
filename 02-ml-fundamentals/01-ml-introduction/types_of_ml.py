# Three major types of Machine Learning

# 1. Supervised Learning
# Learns from labeled data.
# Example: Predicting house prices.

X = [[1000], [1500], [2000]]  # House areas
y = [200000, 300000, 400000]  # House prices

print("Supervised Learning")
print("Features:", X)
print("Labels:", y)


# 2. Unsupervised Learning
# Finds patterns in unlabeled data.
# Example: Customer segmentation.

customers = [
    [20, 15000],
    [22, 18000],
    [45, 70000],
    [48, 75000]
]

print("\nUnsupervised Learning")
print("Customer data:", customers)


# 3. Reinforcement Learning
# An agent learns through rewards and penalties.

print("\nReinforcement Learning")
print("Agent -> Action -> Environment -> Reward")