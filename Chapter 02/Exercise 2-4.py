# Programming Exercise 2-4: Total Purchase
#
# Task: Write a program that calculates the total of a purchase including sales tax.
#
# Requirements:
# 1. Ask the user to enter the price of 5 items
# 2. Calculate the subtotal of all items
# 3. Calculate the sales tax (7% tax rate)
# 4. Calculate the total (subtotal + tax)
# 5. Display the subtotal, sales tax, and total formatted to 2 decimal places
#
# Constants:
# - TAX_RATE = 0.07 (7%)
#
# Formulas:
# - subtotal = sum of all item prices
# - tax = subtotal * TAX_RATE
# - total = subtotal + tax
#
# Example:
# Enter the price of item #1: 10.00
# Enter the price of item #2: 20.00
# Enter the price of item #3: 30.00
# Enter the price of item #4: 40.00
# Enter the price of item #5: 50.00
# Subtotal: 150.00
# Sales Tax: 10.50
# Total: 160.50

Item1 = float(input("What is the price of the 1. Item?"))
Item2 = float(input("What is the price of the 2. Item?"))
Item3 = float(input("What is the price of the 3. Item?"))
Item4 = float(input("What is the price of the 4. Item?"))
Item5 = float(input("What is the price of the 5. Item?"))

TAX_RATE = 0.07

subtotal = (Item1+Item2+Item3+Item4+Item5)
Sales_Tax = (subtotal*TAX_RATE)
Total = (subtotal+Sales_Tax)

print(f"Subtotal: {subtotal:.2f} CHF")
print(f"Sales Tax: {Sales_Tax:.2f} CHF")
print(f"Total: {Total:.2f} CHF")