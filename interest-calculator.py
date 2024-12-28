principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal amount can't be less than zero.")
    else:
        break

while True:
    rate = float(input("Enter the interset rate: "))
    if rate <= 0:
        print("interset rate can't be less than zero.")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than zero.")
    else:
        break

total_amount = principal * pow((1 + rate/100), time)
print(f"Balance after {time} year/s: ${total_amount:.2f}")