# Simple Voting System Program

# Description:
# This program simulates a simple voting system for two candidates.

# How to Run:
# 1. Run the program.
# 2. Enter votes for Candidate A or Candidate B.
# 3. The program will display the results.

# The code:

# Initialize vote counters
votes_A = 0
votes_B = 0

# Number of voters
num_voters = int(input("Enter the number of voters: "))

# Collect votes
for _ in range(num_voters):
    vote = input("Vote for Candidate A or B: ").strip().upper()
    if vote == 'A':
        votes_A += 1
    elif vote == 'B':
        votes_B += 1
    else:
        print("Invalid vote. Please enter A or B.")

# Display the results
print(f"Candidate A: {votes_A} votes")
print(f"Candidate B: {votes_B} votes")
