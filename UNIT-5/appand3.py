# Topic: The Nested List Multiplication Trap (Shallow Copying)
# This script shows why multiplying a nested list creates shared memory links.

# 1. Create a nested list by multiplying an empty list by 3
# TRAP: This creates 3 slots pointing to the EXACT SAME list container in memory.
a = [[]] * 3

# 2. Append the number 9 to the first list (index 0)
# Because all 3 slots share the same container, all 3 change at the same time!
a[0].append(9)

# 3. Print the result
print(a)  # Output will be: [[9], [9], [9]]
