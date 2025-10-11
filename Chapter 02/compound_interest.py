# Programming Exercise: Compound Interest Calculator
# 
# Task: Write a program that calculates the ending principal in a bank
# account after compounding the interest.
#
# Requirements:
# 1. Ask the user to enter the starting principal
# 2. Ask the user to enter the annual interest rate (as a percentage)
# 3. Ask the user how many times per year the interest is compounded
# 4. Ask the user for how many years the account will earn interest
# 5. Calculate the ending balance using the compound interest formula:
#    A = P(1 + r/n)^(nt)
#    Where: A = ending amount, P = principal, r = annual interest rate,
#           n = number of times interest is compounded per year, t = time in years
# 6. Display the ending balance formatted as currency
#
# Formula: a = p * (1 + r/n)^(n*t)
# Note: Remember to convert the interest rate from percentage to decimal
#
# Example output: "At the end of 5 years you will have $1,276.28"
P = float(input("What is your starting principal?"))
R = float(input("What is your interest rate?"))
N = int(input("How many times per year is the interest compounded?"))
T = int(input("How many years will the account earn interest?"))

R = R / 100

A = P * (1 + R/N)**(N*T)

print(f"At the end of {T} years you will have {A:,.2f} CHF")