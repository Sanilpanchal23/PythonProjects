# Multiplication Table Generator Program

# Description:
# This Python program generates the multiplication table for a given number up to 10.
# It allows users to quickly visualize the results of multiplying their chosen number.

# How to Run:
# 1. Download the file.
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where this file is saved.
# 4. Run the following command:
#    python multiplication_table.py
# 5. Enter a number when prompted, and the program will display its multiplication table.

# Features:
# - Generates multiplication tables for any given number.

# The code:

# Get user input for a number
number = int(input("Enter a number to generate its multiplication table: "))

# Generate and print the multiplication table
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
