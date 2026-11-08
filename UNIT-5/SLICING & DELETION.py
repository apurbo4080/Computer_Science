# ==============================================================================
# THE ULTIMATE PYTHON LIST SLICING & DELETION CHEAT SHEET
# Save this file to your GitHub for quick reference!
# ==============================================================================

# Setup our playground list
# Positive indices:   0   1   2   3   4   5   6   7   8   9
# Negative indices: -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# ------------------------------------------------------------------------------
# PART 1: MASTERING SLICING SYNTAX -> list[start:stop:step]
# Remember: "start" is inclusive, "stop" is exclusive (not included).
# ------------------------------------------------------------------------------

# 1. Basic Slicing (Omitting Step defaults to 1)
print(numbers[2:6])      # Output: [30, 40, 50, 60] -> Elements from index 2 up to 5

# 2. Omitting Start (Starts from the very beginning)
print(numbers[:4])       # Output: [10, 20, 30, 40] -> First 4 elements

# 3. Omitting Stop (Goes all the way to the end)
print(numbers[6:])       # Output: [70, 80, 90, 100] -> From index 6 to the end

# 4. Using Stride/Step (Skip elements)
print(numbers[1:8:2])    # Output: [20, 40, 60, 80] -> Start at 1, jump by 2 indices

# 5. Extract Every N-th Element (Entire list)
print(numbers[::3])      # Output: [10, 40, 70, 100] -> Every 3rd item from start


# ------------------------------------------------------------------------------
# PART 2: SLICING TRICKS & ADVANCED TECHS
# ------------------------------------------------------------------------------

# Trick 1: The Quick Copy
# Creates a brand new, independent clone of the list in memory.
list_copy = numbers[:]  
print(list_copy)         # Output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Trick 2: Reversing a List Completely
# A negative step moves backward. No start/stop means look at the whole list.
reversed_list = numbers[::-1]
print(reversed_list)     # Output: [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

# Trick 3: Slicing Backward (Negative Steps)
# When step is negative, "start" must be greater than "stop" to move backward.
print(numbers[7:2:-1])   # Output: [80, 70, 60, 50, 40] -> From index 7 down to 3

# Trick 4: Out of Bounds Handling
# Slicing never throws an IndexError; it gracefully caps at the list boundaries.
print(numbers[5:100])    # Output: [60, 70, 80, 90, 100] -> Stops at the actual end


# ------------------------------------------------------------------------------
# PART 3: DELETING ELEMENTS & CHUNKS
# ------------------------------------------------------------------------------

# Method 1: del statement with index (Removes single item by position)
demo_del = [1, 2, 3, 4, 5]
del demo_del[1]          # Removes index 1 (value 2)
print(demo_del)          # Output: [1, 3, 4, 5]

# Method 2: del statement with a SLICE (Removes a whole block at once!)
demo_slice_del = [10, 20, 30, 40, 50, 60]
del demo_slice_del[1:4]  # Deletes indices 1, 2, and 3
print(demo_slice_del)    # Output: [10, 50, 60]

# Method 3: Delete by Empty Slice Assignment
# Replacing a slice with an empty list effectively deletes those elements.
demo_assign = [100, 200, 300, 400, 500]
demo_assign[2:4] = []    # Removes indices 2 and 3
print(demo_assign)       # Output: [100, 200, 500]

# Method 4: .remove() (Removes by VALUE, not position. Only deletes the first match)
demo_remove = ["apple", "banana", "apple"]
demo_remove.remove("apple") 
print(demo_remove)       # Output: ["banana", "apple"]

# Method 5: .pop() (Removes by index AND returns the removed value)
demo_pop = ["x", "y", "z"]
popped_val = demo_pop.pop(1) # Removes index 1 ("y")
print(demo_pop)          # Output: ["x", "z"]
print(popped_val)        # Output: "y" (Useful if you need to use the deleted item)

# Method 6: .clear() (Empties the entire list completely)
demo_clear = [1, 2, 3]
demo_clear.clear()
print(demo_clear)        # Output: []
