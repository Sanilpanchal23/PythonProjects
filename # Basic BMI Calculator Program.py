# Basic BMI Calculator Program

# Description:
# This program calculates the Body Mass Index (BMI) based on the user's weight and height.

# How to Run:
# 1. Run the program.
# 2. Enter your weight in kilograms and height in meters.
# 3. The program will display your BMI.

# The code:

# Get weight and height from the user
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Print the result
print(f"Your BMI is: {bmi:.2f}")
