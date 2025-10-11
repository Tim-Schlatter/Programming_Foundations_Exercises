# Programming Exercise 3-9: Roulette Wheel Colors
#
# Task: Write a program that determines the color of a roulette wheel pocket.
#
# Requirements:
# 1. Ask the user to enter a pocket number from 0 to 36
# 2. Determine the color based on the pocket number:
#    - Pocket 0: Green
#    - Pockets 1-10: Odd numbers are red, even numbers are black
#    - Pockets 11-18: Odd numbers are black, even numbers are red
#    - Pockets 19-28: Odd numbers are red, even numbers are black
#    - Pockets 29-36: Odd numbers are black, even numbers are red
# 3. Display the color or an error message for invalid input
#
# Logic:
# - Use if-elif-else structure for different pocket ranges
# - Use modulo operator (%) to determine odd/even
# - Include validation for pocket numbers 0-36
#
# Example:
# Enter a pocket number from 0 to 36: 0
# Green
#
# Enter a pocket number from 0 to 36: 7
# Red
#
# Enter a pocket number from 0 to 36: 12
# Red
#
# Enter a pocket number from 0 to 36: 40
# Error: Invalid input

Pocket_Number = int(input("Enter a Number between 0-36: "))

if Pocket_Number >= 0 and Pocket_Number <= 36:
     ()
else:
     print ("Error: Invalid input")

if Pocket_Number == 0:
     print ("Green")
elif Pocket_Number >= 1 and Pocket_Number <= 10:
     Pocket_Number1 = Pocket_Number % 2 
     if Pocket_Number1 != 0:
          print (f"Red")
     else:
          print (f"Black")

elif Pocket_Number >= 11 and Pocket_Number <= 18:
     Pocket_Number2 = Pocket_Number % 2 
     if Pocket_Number2 != 0:
          print (f"Black")
     else:
          print (f"Red")

elif Pocket_Number >= 19 and Pocket_Number <= 28:
     Pocket_Number3 = Pocket_Number % 2 
     if Pocket_Number3 != 0:
          print (f"Red")
     else:
          print (f"Black")

elif Pocket_Number >= 29 and Pocket_Number <= 36:
     Pocket_Number4 = Pocket_Number % 2 
     if Pocket_Number4 != 0:
          print (f"Black")
     else:
          print (f"Red")