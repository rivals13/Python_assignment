import time


def clear_screen():
    print("\033[2J\033[H", end="")


# Input phase
name = input("Enter your name: ")
age = input("Enter your age: ")

# Small pause (optional, feels natural)
time.sleep(0.5)

# Clear previous inputs
clear_screen()

# Output phase
print("===== USER DETAILS =====")
print(f"Your name is : {name}")
print(f"Your age is  : {age}")
print("========================")
