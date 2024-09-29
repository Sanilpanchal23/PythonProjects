# Area of a Circle Calculator Program

# Description:
# This program calculates the area of a circle given its radius.

# How to Run:
# 1. Run the program.
# 2. Enter the radius of the circle.
# 3. The program will display the area of the circle.

# The code:

# Import the math library to use pi
import math

# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
area = math.pi * radius ** 2

# Print the result
print(f"The area of the circle with radius {radius} is {area}.")
