# Odd or Even Checker Program

# Description:
# This Python program checks whether a number entered by the user is odd or even.

# How to Run:
# 1. Download the file.
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where this file is saved.
# 4. Run the following command:
#    python odd_or_even.py
# 5. Enter a number when prompted, and the program will tell you if it's odd or even.

# Features:
# - Takes an integer input from the user.
# - Prints whether the number is odd or even.

# The code:

# Get user input for a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
