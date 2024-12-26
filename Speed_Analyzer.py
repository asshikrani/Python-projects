
from time import *
import random as r

def mistaker(par,user):
    error = 0
    try:
        if par != user:
            error = error + 1
    except:
            error = error + 1
    return error

def timer(timestart,timeend,userinput):
     timedelay = timeend - timestart
     timedelay_r = round(timedelay)
     speed = len(userinput)/ timedelay_r
     return round(speed)
     
        

test = ["I am a student of city college of science and science and commerce Multan.","i am ahmad siddique.","Welcome to my programmes."]

test1 = r.choice(test)

a = "TYPING SPEED CALCULATOR"
print(f"{a: ^300}")

print(test1)

print("""


""")
time_1 = time()
testinput = input("start:")
time_2 = time()

print("speed:",timer(time_1,time_2,testinput), "w/sec")
print(f"Error:{mistaker(test,testinput)}")

