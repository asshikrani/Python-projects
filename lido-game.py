# DISE ROLLER GAME

import random
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") 

dise_art = {
    1 : (" ┌─────────┐",
         " │         │",
         " │    ●    │",
         " │         │",
         " └─────────┘"),
    2 : (" ┌─────────┐",
         " │  ●      │",
         " │         │",
         " │      ●  │",
         " └─────────┘"),
    3 : (" ┌─────────┐",
         " │ ●       │",
         " │    ●    │",
         " │       ● │",
         " └─────────┘"),
    4 : (" ┌─────────┐",
         " │  ●   ●  │",
         " │         │",
         " │  ●   ●  │",
         " └─────────┘"),
    5 : (" ┌─────────┐",
         " │  ●   ●  │",
         " │    ●    │",
         " │  ●   ●  │",
         " └─────────┘"),
    6 : (" ┌─────────┐",
         " │  ●   ●  │",
         " │  ●   ●  │",
         " │  ●   ●  │",
         " └─────────┘")
}

dise = []
total = 0
num_of_dise = int(input("Enter the number of dice: "))
for die in range(num_of_dise):
    dise.append(random.randint(1,6))

# ------------------IF YOU WANT TO PRINT IT VERTICALLY-----------------

# for die in range(num_of_dise):
#     for line in dise_art.get(dise[die]):
#         print(line)


# ------------------IF YOU WANT TO PRINT IT HORIZONTALLY-----------------
for line in range(5):
    for die in dise:
        print(dise_art.get(die)[line],end="")
    print()

for die in dise: 
    total += die
print(f"Total: {total}")