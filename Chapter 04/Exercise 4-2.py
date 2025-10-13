# Programming Exercise 4-2: Calories Burned
#
# Task: Write a program that displays calories burned during exercise over time.
#
# Requirements:
# 1. Initialize a constant for calories burned per minute (4.2)
# 2. Create a table header showing "Minutes" and "Calories Burned"
# 3. Use a for loop to calculate calories burned for different time periods
# 4. Display minutes from 10 to 30 in increments of 5
# 5. Calculate calories burned for each time period
# 6. Display the results in a tabular format
#
# Constants:
# - caloriesPerMinute = 4.2
#
# Logic:
# - Use for minutes in range(10, 31, 5) to get 10, 15, 20, 25, 30
# - Calculate caloriesBurned = caloriesPerMinute * minutes
# - Display each row with minutes and calories burned
#
# Example output:
# Minutes		Calories Burned
# -------------------------------
# 10		42.0
# 15		63.0
# 20		84.0
# 25		105.0
# 30		126.0

CALORIESPERMINUTE = 4.2 
calories_burned = 0 
minutes = 0 

print ('Minutes\t\tCalories Burned')
print ('-------------------------------')

for minutes in range (10, 31, 5):
    calories_burned