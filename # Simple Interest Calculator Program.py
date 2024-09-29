# Simple Interest Calculator Program

# Description:
# This Python program calculates simple interest using the formula:
# Simple Interest = (Principal * Rate * Time) / 100

# How to Run:
# 1. Download the file.
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where this file is saved.
# 4. Run the following command:
#    python simple_interest.py
# 5. Enter the principal amount, rate of interest, and time when prompted, and the program will calculate the interest.

# Features:
# - Calculates simple interest for given principal, rate, and time values.

# The code:

# Function to calculate simple interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Get user input for principal, rate of interest, and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

# Calculate and display the simple interest
interest = simple_interest(principal, rate, time)
print(f"The simple interest for the principal amount {principal} at a rate of {rate}% for {time} years is {interest}.")
