# Programming Exercise 3-8: Hot Dog Cookout Calculator
#
# Task: Write a program that calculates the number of hot dog and bun packages needed for a cookout.
#
# Requirements:
# 1. Ask the user to enter the number of people attending the cookout
# 2. Ask the user to enter the number of hot dogs per person
# 3. Calculate the total number of hot dogs and buns needed
# 4. Calculate the minimum packages needed:
#    - Hot dogs come in packages of 10
#    - Buns come in packages of 8
# 5. Calculate leftovers for both hot dogs and buns
# 6. Display all results
#
# Constants:
# - HOT_DOGS_PER_PACKAGE = 10
# - BUNS_PER_PACKAGE = 8
#
# Logic:
# - Calculate total needed = people * hot dogs per person
# - Calculate packages needed using integer division (//)
# - Add extra package if there are leftovers (using modulo %)
# - Calculate final leftovers after purchasing packages
#
# Example:
# Enter the number of people attending the cookout: 25
# Enter the number of hot dogs for each person: 2
# Minimum packages of hot dogs needed: 5
# Minimum packages of hot dog buns needed: 7
# Hot dogs left over: 0
# Hot dog buns left over: 6

peopleNumber = int(input("Enter the number of people attending the cookout: "))
hotdogsPerPerson = int(input("Enter the number of hot dogs per person: "))

HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

total_hotdogs = (peopleNumber*hotdogsPerPerson)

minimum_hotdogs = (total_hotdogs // HOT_DOGS_PER_PACKAGE)

if minimum_hotdogs > 0:
    dogsleft = total_hotdogs % HOT_DOGS_PER_PACKAGE
    if dogsleft != 0: 
        minimum_hotdogs += 1

else:
    minimum_hotdogs = 1

dogsleft = HOT_DOGS_PER_PACKAGE * minimum_hotdogs - total_hotdogs

minimum_buns = (total_hotdogs // BUNS_PER_PACKAGE)

if minimum_buns > 0:
    bunsleft = total_hotdogs % BUNS_PER_PACKAGE
    if bunsleft != 0: 
        minimum_buns += 1

else:
    minimum_buns = 1

bunsleft = BUNS_PER_PACKAGE * minimum_buns - total_hotdogs


print (f"Minimum packages of hot dogs needed: {minimum_hotdogs}")
print (f"Minimum packages of buns needed: {minimum_buns}")
print (f"Hot dogs left over: {dogsleft}")
print (f"Hot dog buns left over: {bunsleft}")
