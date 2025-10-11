# Programming Exercise 3-4: Roman Numeral Converter
#
# Task: Write a program that converts numbers 1-10 to Roman numerals.
#
# Requirements:
# 1. Ask the user to enter an integer from 1-10
# 2. Convert the number to its corresponding Roman numeral:
#    - 1 = I, 2 = II, 3 = III, 4 = IV, 5 = V
#    - 6 = VI, 7 = VII, 8 = VIII, 9 = IX, 10 = X
# 3. Display the Roman numeral or an error message for invalid input
#
# Logic:
# - Use if-elif-else structure to handle each number case
# - Include error handling for numbers outside 1-10 range
#
# Example:
# Enter an integer from 1 - 10: 3
# III
#
# Enter an integer from 1 - 10: 7
# VII
#
# Enter an integer from 1 - 10: 15
# Error: Invalid Number

number = int(input("Enter a integer from 1-10: "))

if number == 1:
    print("I")
elif number == 2:
    print("II")
elif number == 3:
    print("III")
elif number == 4:
    print("IV")
elif number == 5:
    print("V")
elif number == 6:
    print("VI")
elif number == 7:
    print("VII")
elif number == 8:
    print("VIII")
elif number == 9:
    print("IX")
elif number == 10:
    print("X")
else:
    print("Error: Invalid Number!")