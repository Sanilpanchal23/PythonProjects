# Basic URL Shortener Program

# Description:
# This program allows the user to input a URL and receive a shortened version.

# How to Run:
# 1. Run the program.
# 2. Enter a long URL.
# 3. The program will output a shortened URL (dummy).

# The code:

def shorten_url(url):
    return f"short.ly/{len(url)}"

# Get URL from the user
long_url = input("Enter a URL to shorten: ")

# Generate a shortened URL
shortened = shorten_url(long_url)

# Print the result
print(f"Shortened URL: {shortened}")
