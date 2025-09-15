num = -5

print("positive" if num > 0 else "negative")

result = "EVEN" if num % 2 == 0 else "ODD"

a = 5
b = 7

max_num = a if a > b else b
min_num = a if a < b else b

print(max_num)
print(min_num)

role = admin

access = "Full Access" if role == "admin" else "Limited Access"