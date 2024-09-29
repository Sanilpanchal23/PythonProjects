# Temperature Converter Program (Celsius to Fahrenheit)

# Description:
# This Python program converts a temperature from Celsius to Fahrenheit.
# The formula used for conversion is F = C * 9/5 + 32.

# How to Run:
# 1. Download the file.
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where this file is saved.
# 4. Run the following command:
#    python temperature_converter.py
# 5. Enter a temperature in Celsius, and the program will display the equivalent in Fahrenheit.

# Features:
# - Converts Celsius temperatures to Fahrenheit.

# The code:

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Get user input for temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert and display the result
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F.")
