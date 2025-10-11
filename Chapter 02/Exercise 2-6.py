# Programming Exercise 2-6: Installment Loan Calculator
#
# Task: Write a program that calculates the cost of an installment loan.
#
# Requirements:
# 1. Ask the user to enter the purchase amount
# 2. Ask the user to enter the desired number of installments
# 3. Calculate the final purchase amount (add 5% to original amount)
# 4. Calculate the cost per installment
# 5. Display the final purchase amount, number of installments, and cost per installment
#
# Formulas:
# - finalAmount = amount * 1.05 (adds 5% to original amount)
# - instalmentCost = finalAmount / instalments
#
# Example:
# Enter the purchase amount: 1000
# Enter the desired number of instalments: 12
# 
# Final purchase amount: 1050.00
# Number of instalments: 12
# Cost per instalment: 87.50

purchase_amount = float(input("What is your purchase amount?"))
number_instalments = float(input("What is your desired number of installments?"))

Final = purchase_amount*1.05

print(f"Final purchase amount: {Final}")
print(f"Number of instalments: {number_instalments}")
print(f"Cost per instalment: {Final/number_instalments}")