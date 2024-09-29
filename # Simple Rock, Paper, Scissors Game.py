# Simple Rock, Paper, Scissors Game

# Description:
# This program allows the user to play Rock, Paper, Scissors against the computer.

# How to Run:
# 1. Run the program.
# 2. Enter your choice: Rock, Paper, or Scissors.
# 3. The program will display the winner.

# The code:

# Import the random library
import random

# List of choices
choices = ["Rock", "Paper", "Scissors"]

# Get the user's choice
user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

# Get the computer's choice
computer_choice = random.choice(choices)

# Determine the winner
if user_choice == computer_choice:
    result = "It's a tie!"
elif (user_choice == "Rock" and computer_choice == "Scissors") or \
     (user_choice == "Paper" and computer_choice == "Rock") or \
     (user_choice == "Scissors" and computer_choice == "Paper"):
    result = "You win!"
else:
    result = "You lose!"

# Print the choices and result
print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")
print(result)
