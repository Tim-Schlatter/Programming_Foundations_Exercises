# Programming Exercise 2-1: Personal Information
#
# Task: Write a program that displays your personal information.
#
# Requirements:
# 1. Display your name
# 2. Display your address
# 3. Display your city, state, and ZIP code
# 4. Display your telephone number
# 5. Display your college major
#
# Each piece of information should be displayed on a separate line.
#
# Example output:
# Cameron Calero
# 2045 Heliport Loop
# Riverfolk, IN 43286
# 812-555-1212
# Computer Science

name = str(input("What is your Name?"))
address = str(input("What is your Address?"))
city = str(input("What is your city, state and ZIP code?"))
number = str(input("What is your telephone number?"))
college = str(input("What is your college major?"))

print("Your Name is:",(name))
print("Your address is:",(address))
print("Your city, state and ZIP Code are:",(city))
print("Your phone number is:",(number))
print("Your college major is:",(college))