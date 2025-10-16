# Programming Exercise 4-11: Sleep Debt Calculator
#
# Task: Write a program that calculates sleep debt over a week.
#
# Requirements:
# 1. Initialize constants for desirable sleep hours and number of days
# 2. Use a for loop to collect sleep data for 7 days
# 3. Ask the user to enter hours of sleep for each day
# 4. Calculate the total sleep debt
# 5. Display appropriate message based on sleep debt
#
# Constants:
# - DESIRABLE_SLEEP = 8 hours per day
# - DAYS = 7 days
#
# Logic:
# - Use for day in range(1, DAYS + 1) to loop through 7 days
# - Keep running total of actual sleep hours
# - Calculate sleep debt = (desirable sleep * days) - total actual sleep
# - Display different messages based on whether sleep debt > 0
#
# Example:
# Day 1 of 7
# Enter hours of sleep obtained: 6
# Day 2 of 7
# Enter hours of sleep obtained: 7
# ... (continue for all 7 days)
# Total Sleep Debt: 8 hour(s).
#
# Or if no debt:
# You do not have a sleep debt...
# I wish I could say the same!

DESIRABLE_SLEEP_HOURS = 8 
NUMBER_OF_DAYS = 7
total_slept_debt = 0

for days in range(1, NUMBER_OF_DAYS +1):
    print(f"Day {days} of {NUMBER_OF_DAYS}")
    actual_sleep = float(input("Enter the number of sleep obtained:"))
    total_slept_debt += actual_sleep

if DESIRABLE_SLEEP_HOURS*NUMBER_OF_DAYS > total_slept_debt:
    print(f"TOtal Sleep debt: {DESIRABLE_SLEEP_HOURS*NUMBER_OF_DAYS-total_slept_debt } hour(s)")
else:
    print("\nYou do not have a sleep debt...\n")






