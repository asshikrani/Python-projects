

menu = {"pizza": 3.55,
        "nachos": 5.76,
        "fries" : 6.75,
        "pop corn": 2.22,
        "chips": 3.11,
        "soda" : 8.23,
        "lemonde": 3.56,
        "pretzel" : 4.78}


a = sorted(menu)
print(a)

# print("=========MENU=========")
# for key, value in menu.items():
#       print(f"{key:10}: ${value:.2f}")
# print("======================")

# total = 0
# foods = []

# while True:
#         food = input("Enter food (q to quit):")
#         if food.lower() == 'q':
#                 break
#         elif menu.get(food) is not None:
#             foods.append(food)
                
# print("======YOUR ORDER======")
# for food in foods:
#        total += menu.get(food)
#        print(food, end=" ")
#        total += menu.get(food)
# print("======================")
# print()
# print(f"Your total bill is {total}")

