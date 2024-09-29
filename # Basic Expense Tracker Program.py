# Basic Expense Tracker Program

# Description:
# This program allows the user to track their daily expenses.

# How to Run:
# 1. Run the program.
# 2. Enter expense details (name and amount).
# 3. Type 'done' to finish and see the total expenses.

# The code:

expenses = {}

while True:
    name = input("Enter the expense name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    amount = float(input("Enter the amount for this expense: "))
    expenses[name] = amount

total_expenses = sum(expenses.values())

print("\nYour Expenses:")
for name, amount in expenses.items():
    print(f"{name}: ${amount:.2f}")

print(f"Total Expenses: ${total_expenses:.2f}")
