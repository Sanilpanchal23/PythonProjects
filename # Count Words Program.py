# Count Words Program

# Description:
# This program counts the number of words in a given sentence.

# How to Run:
# 1. Run the program.
# 2. Enter a sentence.
# 3. The program will display the word count.

# The code:

# Get a sentence from the user
sentence = input("Enter a sentence: ")

# Count the number of words
word_count = len(sentence.split())

# Print the result
print(f"The number of words in the sentence is: {word_count}")
