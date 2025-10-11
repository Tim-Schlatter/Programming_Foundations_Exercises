# Programming Exercise 3-1: Number Classification
#
# Task: Write a program that classifies a number based on its properties.
#
# Requirements:
# 1. Ask the user to enter an integer
# 2. Determine if the number is positive, negative, or zero
# 3. Determine if the number is even or odd
# 4. Display both classifications
#
# Logic:
# - For positive/negative/zero: use if-elif-else with comparison operators
# - For even/odd: use modulo operator (%) to check remainder when divided by 2
#
# Example:
# Enter an integer: 7
# Positive
# Odd
#
# Enter an integer: -4
# Negative
# Even
#
# Enter an integer: 0
# Zero
# Even

number = int(input("Enter an integer number: "))

if number > 0:
    print ("Positive")
elif number < 0:
    print ("Negative")   
else: 
    print ("Zero")

if number % 2 == 0:
    print ("Even")
else:
    print ("Uneven")