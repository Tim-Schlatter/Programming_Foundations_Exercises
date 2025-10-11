# Programming Exercise 3-12: Software Sales
#
# Task: Write a program that calculates the discount and total amount for software purchases.
#
# Requirements:
# 1. Ask the user to enter the number of packages purchased
# 2. Calculate the discount rate based on quantity:
#    - 10-19 packages: 10% discount
#    - 20-49 packages: 20% discount
#    - 50-99 packages: 30% discount
#    - 100+ packages: 40% discount
#    - Less than 10 packages: no discount
# 3. Calculate the full price (quantity * retail price)
# 4. Calculate the discount amount (full price * discount rate)
# 5. Calculate the total amount (full price - discount amount)
# 6. Display the discount amount and total amount formatted as currency
#
# Constants:
# - RETAIL_PRICE = 99 (price per package)
#
# Example:
# Enter the number of packages purchased: 25
# Discount Amount: $495.00
# Total Amount: $1,980.00

RETAIL_PRICE = 99
numPackages = 0

numPackages = int(input("Enter the number of packages purchased: "))
price = (numPackages*RETAIL_PRICE)

if numPackages >= 10 and numPackages <= 19:
    endprice = price*0.9
elif numPackages >= 20 and numPackages <= 49:
    endprice = price*0.8
elif numPackages >= 50 and numPackages <= 99:
    endprice = price*0.7
elif numPackages >= 100: 
    endprice = price*0.6

discount = price-endprice

print (f"Discount Amount: CHF {discount:,.2f}")
print (f"Total Amount: CHF {endprice:,.2f}")
 