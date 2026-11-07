tup = (1, 2, [3, 4])
# Scenario A: tup[2].append(5)
# Scenario B: tup[1] = 20
tup[2].append(5)
tup[1] = 20  # This will raise a TypeError because tuples are immutable
print(tup)  # Output: (1, 2, [3, 4, 5])
