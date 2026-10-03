# Probability Basics


# Probability of an event
def probability(favorable, total):
    return favorable / total


# Example:
# Rolling a dice
# Probability of getting 4

favorable_outcomes = 1
total_outcomes = 6

p = probability(favorable_outcomes, total_outcomes)

print("Probability of getting 4:", p)


# Probability of getting an even number
# Outcomes: 2, 4, 6

favorable_outcomes = 3
total_outcomes = 6

p_even = probability(favorable_outcomes, total_outcomes)

print("Probability of getting an even number:", p_even)