# Programming Exercise 3-2: Area Comparison
#
# Task: Write a program that compares the areas of two rectangles.
#
# Requirements:
# 1. Ask the user to enter the length and width of rectangle A
# 2. Ask the user to enter the length and width of rectangle B
# 3. Calculate the area of both rectangles
# 4. Display both areas formatted to 2 decimal places
# 5. Compare the areas and display which one is greater, or if they are equal
#
# Formula: area = length * width
#
# Logic for comparison:
# - Use if-elif-else to compare areaA and areaB
# - Display appropriate message based on comparison
#
# Example:
# Enter length A: 10
# Enter width A: 5
# Enter length B: 8
# Enter width B: 6
# Area A: 50.00
# Area B: 48.00
# Area A is greater than Area B.

length_A = float(input("Enter the length A: "))
width_A = float(input("Enter the width of A: "))
length_B = float(input("Enter the length B: "))
width_B = float(input("Enter the width B:"))

area_A = length_A*width_A
area_B = length_B*width_B

print(f"Area A: {area_A:.2f}")
print(f"Area B: {area_B:.2f}")

if area_A > area_B:
    print("Area A is greater than Area B.")
elif area_B > area_A:
    print("Area B is greater than Area A")
else:
    print("Area A ist equal to Area B")