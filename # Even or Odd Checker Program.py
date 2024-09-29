# Even or Odd Checker Program

# Description:
# This program checks whether a given number is even or odd.

# How to Run:
# 1. Run the program.
# 2. Enter a number.
# 3. The program will tell you if the number is even or odd.

# The code:

# Get a number from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
