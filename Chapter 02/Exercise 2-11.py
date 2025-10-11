# Programming Exercise 2-11: Lion and Tiger Percentage Calculator
#
# Task: Write a program that calculates the percentage of lions and tigers in a zoo.
#
# Requirements:
# 1. Ask the user to enter the number of lions
# 2. Ask the user to enter the number of tigers
# 3. Calculate the total number of cats (lions + tigers)
# 4. Calculate the percentage of lions
# 5. Calculate the percentage of tigers
# 6. Display both percentages formatted as percentages
#
# Formulas:
# - total = lions + tigers
# - percent_lions = lions / total
# - percent_tigers = tigers / total
#
# Example:
# Enter the number of lions: 15
# Enter the number of tigers: 25
# Lions: 37.50%
# Tigers: 62.50%

lions = int(input("Enter the number of lions: "))
tigers = int(input("Enter the number of tigers: "))

total = lions + tigers 

percent_lions = lions / total
percent_tigers = tigers / total

print (f"Lions: {percent_lions*100}%")
print (f"Tigers: {percent_tigers*100}%")