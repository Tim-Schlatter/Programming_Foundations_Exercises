# Programming Exercise 3-10: Dollar Game
#
# Task: Write a program that calculates the total value of coins and determines if it equals exactly one dollar.
#
# Requirements:
# 1. Ask the user to enter the number of pennies
# 2. Ask the user to enter the number of nickels
# 3. Ask the user to enter the number of dimes
# 4. Ask the user to enter the number of quarters
# 5. Calculate the total value in cents
# 6. Convert the total to dollars
# 7. Determine if the total equals exactly one dollar:
#    - If > $1.00: display "more than one dollar" message
#    - If < $1.00: display "less than one dollar" message
#    - If = $1.00: display congratulations message
#
# Constants:
# - PENNY_VALUE = 1 cent
# - NICKEL_VALUE = 5 cents
# - DIME_VALUE = 10 cents
# - QUARTER_VALUE = 25 cents
# - PENNIES_IN_DOLLAR = 100
#
# Formula: totalDollars = totalCentValue / PENNIES_IN_DOLLAR
#
# Example:
# Enter the number of pennies: 0
# Enter the number of nickels: 0
# Enter the number of dimes: 0
# Enter the number of quarters: 4
# Congratulations!
# The amount you entered was exactly one dollar!
# You win the game!

PENNY_VALUE = 1 
NICKEL_VALUE = 5
DIME_VALUE = 10 
QUARTER_VALUE = 25 
PENNIES_IN_DOLLAR = 100

pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))

totalvalue = (pennies*PENNY_VALUE) + (nickels*NICKEL_VALUE) + (dimes*DIME_VALUE) + (quarters*QUARTER_VALUE)

totaldollars = (totalvalue/PENNIES_IN_DOLLAR)

if totaldollars > 1:
    print ("More than a dollar")
elif totaldollars < 1:
    print ("Less than a dollar")
else:
    print('Congratulations!')
    print('The amount you entered was exactly one dollar!')
    print('You win the game!')