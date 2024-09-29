# List Reversal Program

# Description:
# This program takes a list of numbers and reverses it.

# How to Run:
# 1. Run the program.
# 2. Enter numbers separated by spaces.
# 3. The program will display the reversed list.

# The code:

# Get a list of numbers from the user
numbers = input("Enter numbers separated by spaces: ").split()

# Reverse the list
reversed_list = numbers[::-1]

# Print the reversed list
print("The reversed list is:", reversed_list)
