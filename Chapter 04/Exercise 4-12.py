# Programming Exercise 4-12: Population Growth
#
# Task: Write a program that calculates population growth over a specified number of days.
#
# Requirements:
# 1. Ask the user to enter the starting number of organisms (must be > 0)
# 2. Ask the user to enter the average daily increase (must be > 0)
# 3. Ask the user to enter the number of days to multiply (must be > 0)
# 4. Use while loops to validate all inputs (must be positive)
# 5. If average daily increase >= 1.0, divide by 100 to convert to percentage
# 6. Display population growth for each day
#
# Logic:
# - Use while loops to ensure all inputs are positive
# - Convert percentage if needed: if avg >= 1.0, then avg /= 100.0
# - Use for day in range(days) to loop through each day
# - Apply growth after first day: num += (num * avg)
# - Display day number and current population
#
# Example:
# Starting number of organisms: 1000
# Average daily increase: 5
# Number of days to multiply: 10
# Day Approximate		 Population
# -----------------------------------
# 1			 1000
# 2			 1050
# 3			 1102
# ... (continues for all days)




starting_number = 0

starting_number = float(input("ENter the starting number of organism (must be > 0): "))
daily_increase = float(input("Average daily increase: "))
number_of_days = int(input("Enter the number of days to multiply: "))

total = starting_number
avg = 0 

if starting_number > 0 and daily_increase > 0 and number_of_days > 0:
    print("\nDay Approximate\tPopulation")
    print("-"*40)
    for day in range(number_of_days):
        avg += total/100*daily_increase
        total += avg
        print(f"{day+1}\t{starting_number+avg:,.0f}")        
else:
    print("Invalid Input: numbers must be > 0!")



