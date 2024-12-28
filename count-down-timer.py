import time
import pyttsx3

input_time = int(input("Enter Time in seconds: "))

for i in range(input_time, 0, -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600) % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    time.sleep(1)
print("TIME'S UP!")
speak = pyttsx3.speak("TIME'S UP!")
