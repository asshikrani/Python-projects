# Banking system
import time
def show_balance(balance):
    print("*************************")
    print(f"Your balance is ${balance:.2f}")
    print("*************************")
def deposit():
    print("*************************")
    amount = float(input("Enter amount to be deposited: "))
    print("*************************")
    if amount < 0:
        print("*************************")
        print("That's not a valid amount")
        return 0
    else:
        print("*************************")
        return amount
def withdraw(balance):
    print("*************************")
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("*************************")
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("*************************")
        print("Amount must be greater than 0!")
    else:
        return amount


def main():
    balance = 0
    is_running = True
    while is_running:
        print("*************************")
        print("     Banking system.     ")
        print("*************************")
        print("1.Show balance\n2.Deposit\n3.Withdraw\n4.Exit")
        print("*************************")
        choice = input("Enter your choice: ")
        if choice == '1':
            show_balance(balance)
            time.sleep(3)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*************************")
            print("Invalid input!\nRun program again")
            print("*************************")
    print("*************************")
    print("Thankyou have a nice day.")
    print("*************************")

if __name__ == '__main__':
    main()