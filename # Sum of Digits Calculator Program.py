# Sum of Digits Calculator Program

# Description:
# This program calculates the sum of digits of a given number.

# How to Run:
# 1. Run the program.
# 2. Enter a number.
# 3. The program will display the sum of its digits.

# The code:

# Get a number from the user
number = int(input("Enter a number: "))

# Initialize sum variable
sum_of_digits = 0

# Calculate sum of digits
for digit in str(number):
    sum_of_digits += int(digit)

# Print the result
print(f"The sum of digits of {number} is {sum_of_digits}.")
