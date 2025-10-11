# Programming Exercise 3-6: Magic Date
#
# Task: Write a program that determines if a date is a "magic date".
#
# Requirements:
# 1. Ask the user to enter the month in numeric form (1-12)
# 2. Ask the user to enter the day of the month (1-31)
# 3. Ask the user to enter the year in two-digit format (00-99)
# 4. Validate all inputs:
#    - Month must be 1-12
#    - Day must be 1-31
#    - Year must be 00-99
# 5. If inputs are valid, check if it's a magic date:
#    - A magic date occurs when day * month = year
# 6. Display the date and whether it's magic or not
#
# Logic:
# - Use if-elif-else for input validation
# - Use if-else to check magic date condition
#
# Example:
# Enter the month in numeric form: 6
# Enter the day of the month: 10
# Enter the year in two digit format: 60
# The date is 6/10/60
# This is a magic date.
#
# Enter the month in numeric form: 12
# Enter the day of the month: 5
# Enter the year in two digit format: 60
# The date is 12/5/60
# This is not a magic date.

month = int(input("Enter a month in numeric form from 1-12: "))
day = int(input("Enter a day in numeric form from 1-31: "))
year = int(input("Enter a year in two-digit format 00-99 : "))

if  month > 12 or  month < 1:
    print ("Error: Invalid month input")
elif day > 31 or day < 1: 
    print ("Error: Invalid day input")
elif year > 99 or year < 0:
    print("Error: Invalid year input")

else: 
    print (f"The date is {month}/{day}/{year}")
    if (month*day) == year:
        print ("This is a magic date.")
    else:
        print ("This is not a magic date.")
