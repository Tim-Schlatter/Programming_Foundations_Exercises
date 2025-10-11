# Programming Exercise 2-7: Miles per Gallon Calculator
#
# Task: Write a program that calculates miles per gallon for a car.
#
# Requirements:
# 1. Ask the user to enter the miles driven
# 2. Ask the user to enter the gallons of fuel used
# 3. Calculate the miles per gallon
# 4. Display the result formatted to 2 decimal places
#
# Formula: mpg = miles / gallons
#
# Example:
# Enter the miles driven: 350
# Enter the gallons of fuel used: 15
# You used 23.33 miles per gallon.

miles_driven = float(input("How many miles did you drive?"))
fuel = float(input("How many gallons of fuel did you use?"))

mpg = miles_driven/fuel

print(f"You used {mpg:.2f} gallons per mile")