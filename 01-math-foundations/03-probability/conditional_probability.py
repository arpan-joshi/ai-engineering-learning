# Conditional Probability


# Formula:
# P(A|B) = P(A and B) / P(B)


# Example:
# 60 students
# 30 students know Python
# 20 students know Python and SQL

python_students = 30
python_and_sql_students = 20

p_sql_given_python = python_and_sql_students / python_students

print("P(SQL | Python):", p_sql_given_python)