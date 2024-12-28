

sum_odd_num = 0
sum_even_num = 0
total = 0

# step1
card_num = (input("Enter a credit card: "))
card_num = card_num.replace('-', '')
card_num = card_num.replace(' ', '')
card_num = card_num[::-1]

# step 2

for i in card_num[::2]:
    sum_odd_num += int(i)
    
# step 3

for i in card_num[1::2]:
    i = int(i) * 2
    if i > 9:
        sum_even_num += (1 + (i % 10))
    else:
        sum_even_num += i

# step 4

total = sum_even_num + sum_odd_num

# step 5

if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")
 
