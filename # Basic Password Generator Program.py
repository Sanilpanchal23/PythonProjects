# Basic Password Generator Program

# Description:
# This program generates a random password with letters, numbers, and symbols.

# How to Run:
# 1. Run the program.
# 2. Enter the desired password length.
# 3. The program will generate and display a random password.

# The code:

import random
import string

# Get the desired password length from the user
length = int(input("Enter the desired password length: "))

# Define the character set
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ''.join(random.choice(characters) for _ in range(length))

# Print the generated password
print(f"Your generated password is: {password}")
