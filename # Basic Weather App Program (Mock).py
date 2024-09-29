# Basic Weather App Program (Mock)

# Description:
# This program returns a mock weather report based on user input.

# How to Run:
# 1. Run the program.
# 2. Enter a city name.
# 3. The program will return a mock weather report.

# The code:

def get_weather(city):
    return f"The weather in {city} is sunny with a temperature of 25°C."

# Get city from the user
city = input("Enter a city: ")

# Get the weather report
weather_report = get_weather(city)

# Print the weather report
print(weather_report)
