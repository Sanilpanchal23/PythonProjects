# Palindrome Checker Program

# Description:
# This program checks whether a given word or number is a palindrome.

# How to Run:
# 1. Run the program.
# 2. Enter a word or number.
# 3. The program will tell you if it's a palindrome.

# The code:

# Get a word or number from the user
text = input("Enter a word or number: ")

# Check if the input is a palindrome
if text == text[::-1]:
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome.")
