#credit card validation program
number = []
creditCard=str(input("please enter your credit card number(13-16 digits):"))
number.append(creditCard)
sumEven = 0
sumodd = 0
# Return True if the card number is valid
def isValid(number):
    sumOfDoubleEvenPlace(number)
    sumOfOddPlace(number)
    prefixMatched(number)
    if ((sumEven + sumodd)%10) == 0:
        print("Your credit card is valid")
    else:
        print("Your Credit card is not valid")

# Get the result from Step (b)
def sumOfDoubleEvenPlace(number):
    sumEven = 0
    position = len(number) - 2

    while position >= 0:
        Value = digitsum(int(number[position] * 2))
        if Value > 9:
            getDigit()
            position = position - 2
            sumEven += sumEven
        else:
            sumEven = sumEven + Value
        return sumEven

# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number):
    Value2 = digitsum(int(number[position] + 2))
    sumEven = sumEven + Value2
    return sumEven

# Return sum of odd place digits in number
def sumOfOddPlace(number):
    sumodd = 0
    position = len(number) - 1

    while position >= 0:
        sumodd = sumodd + int(number[position])
        position = position - 2

# Return True if the digit d is a prefix for number
def prefixMatched(number):
    if number[0] == "6":
        print("Your card type is Discover Card")
    elif number[0] == "5":
        print("Your card type is Master card")
    elif number[0] == "4":
        print("Your card type is visa")
    elif number[0] == "3" and number[1] == "7":
        print("Your card type is American express")

isValid(number)
