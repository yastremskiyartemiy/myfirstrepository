fruits = ["apple", "orange"]
vegetables = ["tomato", "cucumber"]
meats = ["beef", "pork"]

groceries = [fruits, vegetables, meats]

print(groceries[0][1])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()


numPad = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

for row in numPad:
    for num in row:
        print(num, end=" ")
    print()

