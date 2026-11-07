# Topic: Python List Slicing Summary
# Formula: nums[start : boundary : jump]
# Note: Python always stops RIGHT BEFORE the boundary index.

# 1. Create a list
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 2. Deleting a block (Deletes index 1 up to 6)
del nums[1:7]
print("After regular delete:", nums)  # Output: [10, 80, 90, 100]

# 3. Deleting with a jump (Starts at 1, jumps 2 slots, stops before 3)
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
del nums[1:3:2]
print("After jump delete:", nums)  # Output: [10, 30, 40, 50, 60, 70, 80, 90, 100]
