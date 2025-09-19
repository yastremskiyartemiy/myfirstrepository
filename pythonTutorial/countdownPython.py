import time

myTime = int(input("Enter your time in seconds: "))

for i in range(myTime, 0, -1):
    seconds = myTime % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:f{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME IS UP!!!")