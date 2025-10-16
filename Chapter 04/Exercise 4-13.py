# Programming Exercise 4-13: Triangle Pattern
#
# Task: Write a program that prints a triangle pattern using asterisks.
#
# Requirements:
# 1. Initialize a character variable with '*' and size variable with 7
# 2. Use nested for loops to create a triangle pattern
# 3. The pattern should have 7 rows
# 4. Each row should have fewer columns than the previous row
# 5. Print the character without moving to a new line (use end='')
# 6. Move to a new line after each row
#
# Logic:
# - Use for row in range(size) for the outer loop (rows)
# - Use for col in range(size, row, -1) for the inner loop (columns)
# - Print character with end='' to stay on same line
# - Print() after inner loop to move to next row
#
# Expected output:
# *******
# ******
# *****
# ****
# ***
# **
# *

size = 7
character = "*"

for row in range(size):
    for colum in range(size, row, -1):
        print(character, end='')


    print() 