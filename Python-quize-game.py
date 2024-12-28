# Python quiz comptetion


questions = ("How many  elements are in periodic table?: ",
            "Which animal lays the largest eggs?: ",
            "Whta is the most abundant gas on the earth?: ",
            "How many bones are in human body>:",
            "Which is hottest palnet in the solar system?: " )

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Hydrogen", "D. Carbon-Di-Oxide"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),)

answers = ("C", "D", "A", "A", "B")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("===========================")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong answer!")
        print(f"The right answer is {answers[question_num]}")
    question_num += 1

print("======================")
print("         Result       ")
print("======================")

print("Answers: ", end='')
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end='')
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"You got {score}% result")





