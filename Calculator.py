# Python Calculator

operator = input("Enter an operator ( + - * / ): ")

if operator == '+' or operator == '-' or operator == '*' or operator == '/':

    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))

    if operator == '+':
        result = num1 + num2
        print(round(result, 3)) 
    elif operator == '-' :
        result = num1 - num2
        print(round(result, 3))
    elif operator == '*' :
        result = num1 * num2
        print(round(result, 3))
    else :
        result = num1 / num2
        print(round(result, 3))   
else:
    print(f"{operator} is not a valid operator.")
    
#Powered By Ahmad  Siddique.

    

