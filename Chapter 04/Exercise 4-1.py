# Programming Exercise 4-1: Bug Collector
#
# Task: Write a program that collects bug data over 5 days and calculates the total.
#
# Requirements:
# 1. Initialize variables for bugs collected each day and total bugs
# 2. Use a for loop to collect bug data for 5 days
# 3. Ask the user to enter the number of bugs collected each day
# 4. Add each day's bugs to the running total
# 5. Display the total number of bugs collected
#
# Logic:
# - Use for day in range(5) to loop through 5 days
# - Use += operator to accumulate the total
# - Display the final total after the loop
#
# Example:
# Enter the number of bugs collected today: 5
# Enter the number of bugs collected today: 3
# Enter the number of bugs collected today: 7
# Enter the number of bugs collected today: 2
# Enter the number of bugs collected today: 8
# Total bugs collected: 25

bugs = 0 
total = 0

for day in range (5):
    bugs = int(input("Enter the number of bugs collected: "))
    total += bugs

print(f"Total bugs collected: {total}")