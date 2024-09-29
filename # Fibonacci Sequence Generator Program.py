# Fibonacci Sequence Generator Program

# Description:
# This Python program generates the Fibonacci sequence up to a specified number of terms.
# The Fibonacci sequence is a series where each number is the sum of the two preceding ones.

# How to Run:
# 1. Download the file.
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where this file is saved.
# 4. Run the following command:
#    python fibonacci.py
# 5. Enter the number of terms to generate the Fibonacci sequence.

# Features:
# - Generates the Fibonacci sequence for a given number of terms.
# - Uses a loop to build the sequence.

# The code:

# Function to generate Fibonacci sequence
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Get user input for the number of Fibonacci terms to generate
n = int(input("How many Fibonacci numbers would you like to generate? "))

# Generate and print the Fibonacci sequence
print(f"The first {n} Fibonacci numbers are: {fibonacci(n)}")
