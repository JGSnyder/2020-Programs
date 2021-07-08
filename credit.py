#! python3
# Author: JGSnyder
# Date: June 2020
# Identifies what type of credit card the user inputs

creditcard = int(input(("Number: "))
card2 = int(creditcard / 10) #every other digit operation
cardtype = int(creditcard / 1000000000000) #12 zeros
total = int(0)
total2 = int(0)

#Step 1: take every other digit, starting with 2nd to last digit
for i in range(8):
    digit = int((card2 % 10) * 2) #multiply each digit by 2
    if digit >= 10:
        #add each of the digits (i.e. 13 --> add 1 + 3)
        ones = int(digit % 10)
        tens = int(digit / 10)
        digit = ones + tens
    #get total of the sum of digits
    card2 = int(card2 / 100)
    total += digit

#Step 2: Add sum of digits that weren't included in step 1.
for i in range(8):
    digit2 = int(creditcard % 10)
    creditcard = int(creditcard / 100)
    total2 += digit2

#Step 3: If total's last digit is 0, number is valid.
if int((total + total2) % 10) != 0:
    print("INVALID")

#Step 4: Check to see what type of card this is.
elif int(cardtype / 10) == 34 or int(cardtype / 10) == 37: #15 digit card
    print("AMEX")
elif 51 <= (int(cardtype / 100)) <= 55: #16 digit card
    print("MASTERCARD")
elif (int(cardtype == 4)) or (int(cardtype / 1000) == 4):
    print("VISA")
else:
    print("INVALID")