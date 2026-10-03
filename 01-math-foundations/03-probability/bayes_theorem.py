# Bayes Theorem


# Formula:
#
# P(A|B) = P(B|A) * P(A) / P(B)


# Example:
# Disease testing

p_disease = 0.01
p_positive_given_disease = 0.90
p_positive_given_no_disease = 0.05

p_no_disease = 1 - p_disease

# Total probability of positive test
p_positive = (
    p_positive_given_disease * p_disease
    + p_positive_given_no_disease * p_no_disease
)

# Bayes theorem
p_disease_given_positive = (
    p_positive_given_disease * p_disease
) / p_positive


print("P(Disease | Positive Test):")
print(p_disease_given_positive)