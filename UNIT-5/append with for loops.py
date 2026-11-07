items = ["a", "b"]
for item in items:
    items.append("c")
    print("items:", items)
    if len(items) > 6:
        break
# Topic: Repeating List Modifications Using Loops
# This loop repeats the action exactly 5 times and prints the results side-by-side on the same line.
for i in range(5):
    items = ["a", "b"]
    items.append("c")
    print(items)
