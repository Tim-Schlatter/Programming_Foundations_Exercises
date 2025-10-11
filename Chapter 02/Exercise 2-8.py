# Programming Exercise 2-8: Tip, Tax, and Total Calculator
#
# Task: Write a program that calculates the tip, tax, and total for a restaurant bill.
#
# Requirements:
# 1. Ask the user to enter the charge for food
# 2. Calculate the tip (18% of food charge)
# 3. Calculate the tax (7% of food charge)
# 4. Calculate the total (food + tip + tax)
# 5. Display the tip, tax, and total formatted as currency
#
# Constants:
# - TAX_RATE = 0.07 (7%)
# - TIP_RATE = 0.18 (18%)
#
# Formulas:
# - tip = food * TIP_RATE
# - tax = food * TAX_RATE
# - total = food + tip + tax
#
# Example:
# Enter the charge for food: 50.00
# Tip: $9.00
# Tax: $3.50
# Total: $62.50

TAX_RATE = 0.07
TIP_RATE = 0.18

food = float(input("How much did your food cost?"))

tip = food*TIP_RATE
tax = food*TAX_RATE

total = food+tip+tax

print(f"Your food costed ${food}")
print(f"Tip: ${tip}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")

