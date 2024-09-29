# Simple Calculator Program

# Description:
# This program acts as a simple calculator that can add, subtract, multiply, or divide two numbers.

# How to Run:
# 1. Run the program.
# 2. Enter two numbers and an operation (+, -, *, /).
# 3. The program will display the result.

# The code:

# Get two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get the operation from the user
operation = input("Enter operation (+, -, *, /): ")

# Perform the calculation based on the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operation"

# Print the result
print(f"The result is: {result}")
