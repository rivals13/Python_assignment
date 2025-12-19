"""
Sample Test Script

This is a simple demonstration script showing basic input/output operations
with screen clearing functionality. Used for testing basic Python features.

Functions:
- clear_screen(): Clear the terminal screen
"""

import time


def clear_screen():
    """
    Clear the terminal screen using ANSI escape codes.
    """
    print("\033[2J\033[H", end="")


# Input phase - collect user information
name = input("Enter your name: ")
age = input("Enter your age: ")

# Small pause for better user experience
time.sleep(0.5)

# Clear previous inputs from screen
clear_screen()

# Output phase - display collected information
print("===== USER DETAILS =====")
print(f"Your name is : {name}")
print(f"Your age is  : {age}")
print("========================")
