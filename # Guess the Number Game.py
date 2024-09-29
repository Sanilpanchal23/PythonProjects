# Guess the Number Game

# Description:
# This program generates a random number between 1 and 10, and the user has to guess it.

# How to Run:
# 1. Run the program.
# 2. Try to guess the random number.
# 3. The program will tell you if you guessed it right.

# The code:

# Import random library
import random

# Generate a random number between 1 and 10
number_to_guess = random.randint(1, 10)

# Get the user's guess
guess = int(input("Guess the number (between 1 and 10): "))

# Check if the guess is correct
if guess == number_to_guess:
    print("You guessed it!")
else:
    print(f"Sorry, the number was {number_to_guess}.")
