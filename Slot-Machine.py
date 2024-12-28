# python slot machine
import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0


def main():
    balance = 100
    print("***********************")
    print("Welcome to python slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐ ")
    print("***********************")

    while balance > 0:
        print(f"Your balance is {balance}")
        bet = input("Place your bet amount: ")

        if not balance.is_integer():
            print("Please enter a valid input!")
            continue

        bet = int(bet)

        if bet > balance:
            print("insufficient funds")
            continue
        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"Congratulations! you won {payout}")
        else:
            print("Sorry! you  lost")
        balance += payout

        play_a = input("Do you  want to play again (y/n)").lower()
        if play_a == 'n':
            break

    print("*********************************************")
    print(f"Game over your current balance is ${balance}")
    print("*********************************************")

if __name__ =='__main__':
    main()

