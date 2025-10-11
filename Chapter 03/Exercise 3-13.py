# Programming Exercise 3-13: Shipping Charges
#
# Task: Write a program that calculates shipping charges based on package weight.
#
# Requirements:
# 1. Ask the user to enter the weight of the package
# 2. Calculate the shipping charge based on weight:
#    - Over 10 pounds: $4.75
#    - Over 6 pounds: $4.00
#    - Over 2 pounds: $3.00
#    - 2 pounds or less: $1.50
# 3. Display the shipping charge formatted as currency
#
# Logic:
# - Use if-elif-else structure with weight thresholds
# - Check from highest to lowest weight to get correct rate
#
# Example:
# Enter the weight of the package: 8.5
# Shipping charge: $4.00
#
# Enter the weight of the package: 1.5
# Shipping charge: $1.50

package_weight = 0
 #shipping_charge = float (0) 

package_weight = float(input("Enter the weight of the package: "))

if package_weight > 10:
    shipping_charge = 4.75
elif package_weight > 6:
    shipping_charge = 4.00
elif package_weight > 2:
    shipping_charge = 3.00
else:
    shipping_charge = 1.50

print (f"Shipping charge: {shipping_charge}")