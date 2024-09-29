# Random Password Generator Program

# Description:
# This program generates a random password of a specified length.

# How to Run:
# 1. Run the program.
# 2. Enter the desired password length.
# 3. The program will display a randomly generated password.

# The code:

# Import the random and string libraries
import random
import string

# Get the desired password length from the user
length = int(input("Enter the desired password length: "))

# Generate a random password
password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

# Print the result
print(f"Your random password is: {password}")

