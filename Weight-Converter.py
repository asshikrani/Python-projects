# Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pound (K or L): ")

if unit == 'k' or unit == 'K':
    print(f"Your weight is {round(weight * 2.205, 1)} Kgs.")
elif unit == 'L' or unit == 'l':
    print(f"Your weight is {round(weight / 2.205, 1)} Lbs.")
else:
    print(f"{unit} was not valid.")

#Powered By Ahmad  Siddique.