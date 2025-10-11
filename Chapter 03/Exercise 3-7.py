# Programming Exercise 3-7: Grade Calculator
#
# Task: Write a program that calculates a student's grade based on test and exam scores.
#
# Requirements:
# 1. Ask the user to enter points for Test 1 (out of 25)
# 2. Ask the user to enter points for Test 2 (out of 25)
# 3. Ask the user to enter points for the Exam (out of 50)
# 4. Validate all inputs (must be within valid ranges)
# 5. Calculate the total points (sum of all scores)
# 6. Determine the grade based on total points and exam score:
#    - Fail: if total < 50 OR exam < 25
#    - Pass: if total >= 50 and total <= 59
#    - Credit: if total >= 60 and total <= 79
#    - Distinction: if total >= 80 and total <= 100
# 7. Display the total points and grade
#
# Validation:
# - Test 1: 0-25 points
# - Test 2: 0-25 points
# - Exam: 0-50 points
#
# Example:
# Enter points out of 25 for Test 1: 20
# Enter points out of 25 for Test 2: 22
# Enter points out of 50 for the Exam: 45
# Total points: 87
# Distinction

Test_1 = float(input("Enter the points of Test 1: "))
Test_2 = float(input("Enter the points of Test 2: "))
Exam = float(input("Enter the points for the Exam: "))

if Test_1 > 25 or Test_1 < 0:
    print ("Error: Invalid input for Test 1")
elif Test_2 > 25 or Test_2 < 0:
    print ("Error: Invalid input for Test 2")
elif Exam > 50 or Exam < 0:
    print ("Error: Invalid input for Exam")
else:
    Totalpoints = (Test_1+Test_2+Exam)
    print (f"Total point: {Totalpoints}")
    
    if Totalpoints < 50 or Exam < 25:
        print ("Fail")
    elif Totalpoints >= 50 and Totalpoints <= 59:
        print ("Pass")
    elif Totalpoints >= 60 and Totalpoints <= 79:
        print ("Credit")
    elif Totalpoints >= 80 and Totalpoints <= 100:
        print ("Distinction")