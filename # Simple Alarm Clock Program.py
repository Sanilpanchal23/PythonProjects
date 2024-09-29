# Simple Alarm Clock Program

# Description:
# This program sets a simple alarm that notifies when it's time.

# How to Run:
# 1. Run the program.
# 2. Enter the alarm time in HH:MM format.
# 3. The program will notify you when it's time.

# The code:

import time

# Get alarm time from the user
alarm_time = input("Set the alarm (HH:MM): ")

# Loop until the alarm time is reached
while True:
    current_time = time.strftime("%H:%M")
    if current_time == alarm_time:
        print("Time to wake up!")
        break
    time.sleep(30)  # Check every 30 seconds
