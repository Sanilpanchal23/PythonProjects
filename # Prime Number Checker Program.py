# Prime Number Checker Program

# Description:
# This Python program checks if a number entered by the user is a prime number.
# A prime number is a number greater than 1 with no divisors other than 1 and itself.

# How to Run:
# 1. Download the file.
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where this file is saved.
# 4. Run the following command:
#    python prime_checker.py
# 5. Enter a number when prompted, and the program will tell you if it's prime.

# Features:
# - Checks for prime numbers efficiently by testing divisibility up to the square root of the number.

# The code:

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Get user input for a number
number = int(input("Enter a number to check if it's prime: "))

# Check if the number is prime and print the result
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
