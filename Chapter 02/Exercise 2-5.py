# Programming Exercise 2-5: Distance Traveled
#
# Task: Write a program that calculates the distance a car will travel at a constant speed.
#
# Requirements:
# 1. Calculate the distance the car will travel in 6 hours
# 2. Calculate the distance the car will travel in 10 hours
# 3. Calculate the distance the car will travel in 15 hours
# 4. Display all three distances
#
# Constants:
# - SPEED = 70 miles per hour
#
# Formula: distance = speed * time
#
# Example output:
# The car will travel the following distances:
# 420.0 miles in 6 hours.
# 700.0 miles in 10 hours.
# 1050.0 miles in 15 hours.

Time = float(input("How long where you driving?"))
speed = 70

distance = (Time*speed)

print(f"{distance} miles in {Time} hours.")