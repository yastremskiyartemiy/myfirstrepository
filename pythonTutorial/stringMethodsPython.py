name = input("Enter your full name:")
phoneNumber = input("Enter your phone number:")

result = len(name)
result2 = name.find(" ")
result3 = name.rfind(" ")
name = name.capitalize()
name = name.upper()
name = name.lower()
result4 = name.isdigit()
result5 = name.isalpha()

result6 = phoneNumber.count("-")
phoneNumber = phoneNumber.replace("-", " ")

print(name)

username = input("Enter your username:")

if len(username) > 12:
    print("no-no-no")
else:
    print(f"Welcome {username}")
