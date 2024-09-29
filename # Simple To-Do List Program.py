# Simple To-Do List Program

# Description:
# This program allows the user to create a simple to-do list.

# How to Run:
# 1. Run the program.
# 2. Enter tasks to add to your to-do list.
# 3. Type 'done' to see your tasks.

# The code:

# Initialize an empty to-do list
todo_list = []

# Collect tasks from the user
while True:
    task = input("Enter a task (or type 'done' to finish): ")
    if task.lower() == 'done':
        break
    todo_list.append(task)

# Print the final to-do list
print("Your to-do list:")
for idx, item in enumerate(todo_list, start=1):
    print(f"{idx}. {item}")
