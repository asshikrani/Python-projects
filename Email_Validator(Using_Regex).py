import re
email_codition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your Email:")

if re.search(email_codition, user_email):
    print("Right email")
else:
    print("Wrong email.")