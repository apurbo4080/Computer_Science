# Topic: Input Validation in Python
# This script takes user input, cleans extra spaces, and checks if it is a valid number.

# 1. Take input from the user (Python stores this input as text/string)
val = input("Enter values: ")

# 2. Clean the input and check if it contains only digits
# .strip() removes any accidental spaces from the front and back
# .isdigit() checks if the remaining characters are strictly numbers (0-9)
result = val.strip().isdigit()

# 3. Print the final answer (True or False)
print(result)
