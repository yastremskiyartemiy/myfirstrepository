principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter your principle:"))
    if principle < 0:
        print("Principle can not be less than 0")
    else:
        break
while True:
    rate = float(input("Enter your interest rate:"))
    if rate < 0:
        print("Interest rate can not be less than 0")
    else:
        break
while True:
    time = float(input("Enter your time:"))
    if time < 0:
        print("Time can not be less than 0")
    else:
        break

total = principle * pow((1 + rate / 100),time)
print(f"Balance after {time} years/s: ${total:.2f}")
