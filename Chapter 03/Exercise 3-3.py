# Programming Exercise 3-3: Quarter of the Year
#
# Task: Write a program that determines the quarter of the year based on a month number.
#
# Requirements:
# 1. Ask the user to enter a number (1-12) representing a month
# 2. Determine which quarter of the year the month belongs to:
#    - Months 1-3: First Quarter
#    - Months 4-6: Second Quarter
#    - Months 7-9: Third Quarter
#    - Months 10-12: Fourth Quarter
# 3. Display the quarter or an error message for invalid input
#
# Logic:
# - Use if-elif-else with range conditions
# - Include error handling for numbers outside 1-12 range
#
# Example:
# Enter a number (1-12) for the month: 3
# First Quarter
#
# Enter a number (1-12) for the month: 7
# Third Quarter
#
# Enter a number (1-12) for the month: 15
# Error: Please enter a number between 1 and 12.

number = int(input("Enter a number between 1-12: "))

if number >= 1 and number <= 3:
    print (f"Your month is in the first quarter!")
elif number >= 4 and number <= 6:
    print ("Your month is in the second quarter!")
elif number >= 7 and number <= 9:
    print ("Your month is in the third quarter!")
elif number >= 10 and number <= 12:
    print ("Your month is in the fourth quarter!")
else:
    print ("Error: Please enter a number between 1 and 12.")
