# Programming Exercise 2-10: Cookie Recipe Calculator
#
# Task: Write a program that calculates the ingredients needed for a cookie recipe.
#
# Requirements:
# 1. Ask the user to enter the number of cookies they want to make
# 2. Calculate the cups of sugar needed
# 3. Calculate the cups of butter needed
# 4. Calculate the cups of flour needed
# 5. Display all ingredient amounts formatted to 2 decimal places
#
# Constants (original recipe for 48 cookies):
# - COOKIES_RECIPE = 48.0
# - SUGAR_RECIPE = 1.5 cups
# - BUTTER_RECIPE = 1.0 cups
# - FLOUR_RECIPE = 2.75 cups
#
# Formulas:
# - sugar = (cookies * SUGAR_RECIPE) / COOKIES_RECIPE
# - butter = (cookies * BUTTER_RECIPE) / COOKIES_RECIPE
# - flour = (cookies * FLOUR_RECIPE) / COOKIES_RECIPE
#
# Example:
# Enter the number of cookies: 24
# To make 24.0 cookies, you will need:
# 0.75 cups of sugar
# 0.50 cups of butter
# 1.38 cups of flour

n_cookies = int(input("Number of Cookies you want to make: "))

COOKIES_RECIPE = 48
SUGAR_RECIPE = 1.5
BUTTER_RECIPE = 1
FLOUR_RECIPE = 2.75

sugar = (n_cookies*SUGAR_RECIPE/COOKIES_RECIPE)
butter = (n_cookies*BUTTER_RECIPE/COOKIES_RECIPE)
flour = (n_cookies*FLOUR_RECIPE/COOKIES_RECIPE)

print (f"To make {n_cookies} cookies, you will need: ")
print (f"{sugar:.2f} cups of sugar")
print (f"{butter:.2f} cups of butter")
print (f"{flour:.2f} cups of flour")