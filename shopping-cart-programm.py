
foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy ( Q to quite )")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"enter price of the {food}: $"))
        foods.append(food)
        prices.append(price)

for food in foods:
    print(food,end=" | ")
     
print(f"{"Welcome to us again":=^75}")
for price in prices:
    total += price
print(f"The total bill is ${total}.")

