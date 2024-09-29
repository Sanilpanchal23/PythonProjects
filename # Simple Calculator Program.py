# Simple Calculator Program

# Description:
# This Python program performs basic arithmetic operations such as addition, subtraction,
# multiplication, and division based on the user's choice.

# How to Run:
# 1. Download the file.
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where this file is saved.
# 4. Run the following command:
#    python simple_calculator.py
# 5. Follow the prompts to choose an operation and enter numbers.

# Features:
# - Addition, subtraction, multiplication, and division operations.
# - Error handling for invalid inputs.

# The code:

# Functions for each arithmetic operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# User prompts for selecting the operation
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get user input for operation choice
choice = input("Enter choice (1/2/3/4): ")

# Get user input for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the selected operation
if choice == '1':
    print(f"The result is: {add(num1, num2)}")
elif choice == '2':
    print(f"The result is: {subtract(num1, num2)}")
elif choice == '3':
    print(f"The result is: {multiply(num1, num2)}")
elif choice == '4':
    print(f"The result is: {divide(num1, num2)}")
else:
    print("Invalid input")