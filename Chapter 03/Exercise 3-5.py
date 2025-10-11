# Programming Exercise 3-5: Weight Calculator
#
# Task: Write a program that calculates the weight of an object and evaluates if it's too heavy or too light.
#
# Requirements:
# 1. Ask the user to enter the object's mass in kilograms
# 2. Calculate the weight using the formula: weight = mass * 9.8
# 3. Display the calculated weight formatted to 2 decimal places
# 4. Evaluate the weight:
#    - If weight > 500 Newtons: display "too heavy" message
#    - If weight < 100 Newtons: display "too light" message
#    - If weight is between 100-500 Newtons: no message (object is acceptable)
#
# Constants:
# - MASS_MULTIPLIER = 9.8 (gravitational acceleration)
# - TOO_HEAVY = 500.0 Newtons
# - TOO_LIGHT = 100.0 Newtons
#
# Example:
# Enter the object's mass in kilograms: 60
# Object Weight: 588.00
# The object is too heavy. It weighs more than 500.0 Newtons.
#
# Enter the object's mass in kilograms: 5
# Object Weight: 49.00
# The object is too light. It weighs less than 100.0 Newtons.

MASS_MULTIPLIER = 9.8 
TOO_HEAVY = 500.00
TOO_LIGHT = 100.00

mass = float(input("Enter the object's mass in kilograms: "))
weight = (mass*MASS_MULTIPLIER)

print (f"Object Weight: {weight:.2f}")

if weight >= TOO_HEAVY:
    print(f"The object is too heavy. It weighs more than {TOO_HEAVY} Newtons")
elif weight <= TOO_LIGHT:
    print(f"The object is too light. It weighs less than {TOO_LIGHT} Newtons")
