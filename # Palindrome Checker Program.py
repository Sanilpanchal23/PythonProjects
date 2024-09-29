# Palindrome Checker Program

# Description:
# This program checks if a word entered by the user is a palindrome.
# A palindrome is a word that reads the same forwards and backwards.

# How to Run:
# 1. Download the file.
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where this file is saved.
# 4. Run the following command:
#    python palindrome_checker.py
# 5. Enter a word when prompted, and the program will tell you if it's a palindrome.

# Features:
# - Supports case-insensitive checking.
# - Uses string slicing to check if the word is a palindrome.

# The code:

# Function to check if a word is a palindrome
def is_palindrome(word):
    return word == word[::-1]

# Get user input for a word and convert it to lowercase for case-insensitive checking
word = input("Enter a word: ").lower()

# Check if the word is a palindrome and print the result
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
