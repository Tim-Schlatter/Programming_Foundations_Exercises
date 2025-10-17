# Programming Exercise 4-14: Hollow Triangle Pattern
#
# Task: Write a program that prints a hollow triangle pattern using hash symbols.
#
# Requirements:
# 1. Initialize variables: character = '#', numRows = 7, space = ' '
# 2. Use nested for loops to create a hollow triangle pattern
# 3. The pattern should have 7 rows
# 4. Each row should have 2 more columns than the row number
# 5. Print the symbol only in the first and last column of each row
# 6. Print spaces between the symbols
# 7. Use end='' to stay on the same line
#
# Logic:
# - Use for row in range(numRows) for the outer loop (rows)
# - Use for col in range(row + 2) for the inner loop (columns)
# - Check if col == 0 or col == row + 1 to print symbol
# - Otherwise print space
# - Print() after inner loop to move to next row
#
# Expected output:
# ##
# # #
# #  #
# #   #
# #    #
# #     #
# #      #

size = 6
char = "#"
space = " "



for row in range(size):
    for column in range(row +2):
        if column == 0 or column == row +1:
            print(char, end="")
        else:
            print(space, end="")
        
    print()


