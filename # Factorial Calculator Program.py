# Factorial Calculator Program

# Description:
# This Python program calculates the factorial of a given number. 
# A factorial is the product of all positive integers less than or equal to a given number.

# How to Run:
# 1. Download the file.
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where this file is saved.
# 4. Run the following command:
#    python factorial.py
# 5. Enter a number when prompted, and the program will calculate its factorial.

# Features:
# - Takes a positive integer as input.
# - Uses recursion to calculate the factorial.

# The code:

# Recursive function to calculate factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Get user input
number = int(input("Enter a number to calculate its factorial: "))

# Check if the number is valid
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    print(f"The factorial of {number} is {factorial(number)}")
