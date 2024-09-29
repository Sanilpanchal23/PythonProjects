# Basic Rock-Paper-Scissors Game

# Description:
# This program allows the user to play Rock-Paper-Scissors against the computer.

# How to Run:
# 1. Run the program.
# 2. Enter your choice (rock, paper, or scissors).
# 3. The program will compare your choice with the computer's choice.

# The code:

import random

options = ["rock", "paper", "scissors"]

# Get user choice
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
computer_choice = random.choice(options)

print(f"Computer chose: {computer_choice}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")

