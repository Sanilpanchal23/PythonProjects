# Basic Memory Game (Mock) Program

# Description:
# This program simulates a simple memory game.

# How to Run:
# 1. Run the program.
# 2. Try to remember the numbers displayed.
# 3. Enter the numbers in order.

# The code:

import random
import time

# Generate a random sequence of numbers
sequence = [random.randint(1, 9) for _ in range(3)]
print("Remember this sequence:", sequence)
time.sleep(5)  # Display for 5 seconds
print("\033c", end="")  # Clear the console

# Get user input
user_sequence = input("Enter the sequence (space-separated): ")
user_sequence = list(map(int, user_sequence.split()))

# Check if the user's sequence is correct
if user_sequence == sequence:
    print("You remembered correctly!")
else:
    print("Wrong! The correct sequence was:", sequence)
