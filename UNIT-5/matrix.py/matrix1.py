# Topic: Advanced Matrix Operations & Multi-Dimensional Lists
# This script covers creating matrices, deep index tracking, modifications, and looping.

# ==========================================
# 1. CREATING A DEEPLY NESTED MATRIX
# ==========================================
# We create a matrix with rows, columns, and a 3rd layer nested list inside index 0.
matrix = [
    [1, 2, [3, 4]],  # Row 0 (Contains a sub-list at index 2)
    [5, 6, 7]        # Row 1
]

print("--- Output 1: The Entire Initial Matrix ---")
print(matrix)
print()

# ==========================================
# 2. ACCESSING DIFFERENT LAYERS OF THE MATRIX
# ==========================================
print("--- Output 2: Accessing Different Layers ---")

# Accessing an entire row (Row 0)
print("Row 0 completely:", matrix[0])

# Accessing the inner list inside Row 0
print("The inner sub-list:", matrix[0][2])

# Accessing a single specific value deep inside (the number 4)
# Path: Row 0 -> Index 2 (sub-list) -> Index 1 (value 4)
print("Deep item value:", matrix[0][2][1])
print()

# ==========================================
# 3. MODIFYING VALUES DEEP INSIDE
# ==========================================
print("--- Output 3: Modifying the Matrix ---")

# Task: Target the '4' inside the sub-list and change it to 99
matrix[0][2][1] = 99
print("Sub-list after modification:", matrix[0][2])
print("Entire matrix after modification:", matrix)
print()

# ==========================================
# 4. LOOPING THROUGH A 2D MATRIX (ROW BY ROW)
# ==========================================
print("--- Output 4: Printing Row by Row using a Loop ---")
row_number = 0
for row in matrix:
    print(f"Row {row_number} content is:", row)
    row_number += 1
