# Average of Numbers Program

# Description:
# This program calculates the average of a list of numbers entered by the user.

# How to Run:
# 1. Run the program.
# 2. Enter the numbers separated by spaces.
# 3. The program will calculate and display the average.

# The code:

# Get numbers from the user as input
numbers = input("Enter numbers separated by spaces: ").split()

# Convert the input to a list of floats
numbers = [float(num) for num in numbers]

# Calculate the average
average = sum(numbers) / len(numbers)

# Print the result
print(f"The average of the numbers is {average}.")

