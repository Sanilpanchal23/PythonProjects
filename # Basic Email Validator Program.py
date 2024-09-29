# Basic Email Validator Program

# Description:
# This program checks if an email address is valid.

# How to Run:
# 1. Run the program.
# 2. Enter an email address.
# 3. The program will tell you if it's valid.

# The code:

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Get email from the user
email = input("Enter an email address: ")

# Validate the email
if is_valid_email(email):
    print("The email address is valid.")
else:
    print("The email address is invalid.")
