# Programming Exercise 4-ter1: Prime Number Checker
#
# Task: Write a program that determines if a number is prime using a for loop.
#
# Requirements:
# 1. Ask the user to enter an integer
# 2. Check if the number is greater than 1
# 3. Use a for loop to test for divisibility
# 4. Check divisibility from 2 to half the number
# 5. Display whether the number is prime or not
#
# Logic:
# - If number <= 1, it's not prime
# - If number > 1, test divisibility from 2 to number/2
# - Use for i in range(2, int(number / 2) + 1)
# - If any number divides evenly (remainder = 0), it's not prime
# - Use break to exit loop when a divisor is found
# - Use else clause with for loop for prime numbers
#
# Example:
# Please enter an integer: 17
# 17 is a prime number.
#
# Please enter an integer: 24
# 24 is NOT a prime number.
#
# Please enter an integer: 1
# 1 is NOT a prime number.
def function():

    number = int(input("Enter an integer: "))

    if number > 0:
        for i in range(2, int(number/2)+1):
            if (number % i) == 0:
                print(number, "is NOT a prime number.")
                break

        else:   
            print(number, "is a prime number.")

    else:
        print(f"{number} is NOT a prime number!")

function()

