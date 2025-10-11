# Programming Exercise 3-11: Book Club Points
#
# Task: Write a program that calculates points earned for book purchases.
#
# Requirements:
# 1. Ask the user to enter the number of books purchased
# 2. Determine the points earned based on the number of books:
#    - 2 books: 5 points
#    - 4 books: 15 points
#    - 6 books: 30 points
#    - 8 or more books: 60 points
#    - 0, 1, 3, 5, 7 books: 0 points
# 3. Display the number of books purchased and points earned
#
# Logic:
# - Use if-elif-else structure to handle specific book quantities
# - Use >= for the highest tier (8 or more books)
#
# Example:
# Enter the number of books purchased: 4
# You have purchased 4 books.
# This earns you 15 points.
#
# Enter the number of books purchased: 10
# You have purchased 10 books.
# This earns you 60 points.

numBooks = 0 
points = 0 

numBooks = int(input("Enter the number of books you purchased: ")) 

if numBooks == 2:
    points += 5
elif numBooks == 4:
    points += 15 
elif numBooks == 6:
    points += 30
elif numBooks >= 8:
    points += 60

print (f"You have purchased {numBooks} books.")
print (f"This earns you {points} points.")

