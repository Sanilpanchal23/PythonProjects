# Count Vowels Program

# Description:
# This program counts the number of vowels in a given string.

# How to Run:
# 1. Run the program.
# 2. Enter a string.
# 3. The program will display the number of vowels.

# The code:

# Get a string from the user
text = input("Enter a string: ")

# Initialize a counter for vowels
vowel_count = 0

# Define vowels
vowels = "aeiouAEIOU"

# Count the vowels in the string
for char in text:
    if char in vowels:
        vowel_count += 1

# Print the result
print(f"The number of vowels in the string is {vowel_count}.")
