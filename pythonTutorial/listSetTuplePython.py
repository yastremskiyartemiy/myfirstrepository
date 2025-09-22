fruits = ["apple", "orange", "banana", "coconut"]

fruits[0] = "orange"
fruits.append("pineapple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
fruits.index("apple")
fruits.clear()
fruits.count("banana")

print(fruits)

fruitss = {"apple", "orange", "banana", "coconut"}

print("pineapple" in fruitss)
fruitss.add("pineapple")
fruitss.remove("apple")
fruitss.pop()
fruitss.clear()
print(fruitss)

fruitsss = ("apple", "orange", "banana", "coconut")

print(len(fruitsss))
print("pineapple" in fruitsss)
fruitsss.index("apple")
fruitsss.count("coconuts")

for fruit in fruitsss():
    print(fruit)