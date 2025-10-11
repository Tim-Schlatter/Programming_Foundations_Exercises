# Programming Exercise 2-3: Pounds to Kilograms Converter
#
# Task: Write a program that converts pounds to kilograms.
#
# Requirements:
# 1. Ask the user to enter a value in pounds
# 2. Convert the pounds to kilograms using the conversion factor 0.454
# 3. Display the result formatted to 2 decimal places
#
# Formula: kilograms = pounds * 0.454
#
# Example:
# Enter a value in pounds: 10
# 10 pounds is 4.54 kilograms.

pound = float(input("Enter a value in pounds!"))
kg = (pound*0.454)

print(f"{pound} pounds is {kg:.2f} kilograms.")