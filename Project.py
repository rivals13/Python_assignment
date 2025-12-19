"""
Banking Management System - Main Entry Point

This is the main file of the banking management system project.
It handles user authentication and directs users to their respective interfaces.

Authors:
- Satyaraj Joshi (NP070996)
- Rajkumar Tiruwa (NP070980)
- Sansar Chhetri (NP070995)

Features:
- Admin login for system management
- Staff login for customer service
- User login for account management
"""

from functions.logins import admin_login, staff_login, user_login
from functions.cli_utils import clear_screen  # Function to clear the terminal screen
import time

# Global variable to track login status
isLoggedin = False  # Initial status of login


def welcome_display():
    """
    Display the welcome screen with group details and login options.

    This function shows the project title, team information, and available login options.
    """
    print("==" * 20)
    print("Group details:")
    print('TEAM-6')
    print("Satyaraj joshi(NP070996)")
    print("Rajkumar Tiruwa(NP070980)")
    print("Sansar chhetri(NP070995)")
    print("==" * 20)
    print("Welcome to the banking management system")
    print('=='*20)
    print("select one option")
    print("--" * 20)
    print("1 |Admin login 👨🏻‍💻|")
    print("\n2 |Staff Login 👨🏻‍💼|")
    print("\n3 |user Login 👨🏻‍💼|")
    print("\n current status: (Not logged in)")
    print("--" * 20)


# Display welcome screen if not logged in
if not isLoggedin:  # Show welcome display only when not logged in
    welcome_display()


def login(type_var):
    """
    Handle login process for different user types.

    Args:
        type_var (str): Type of user ('admin', 'staff', or 'user')
    """
    # Clear the terminal before showing the login prompt
    clear_screen()
    if type_var == "admin":
        print()
        print(f"you are trying to login in as: '{type_var}'")
        print("--" * 20)
        admin_login()  # Entry point for admin login function
    elif type_var == "staff":
        print()
        print(f"You are trying to login in as: {type_var}")
        print("--" * 20)
        staff_login()

    elif type_var == "user":
        print()
        print(f"You are trying to login in as: {type_var}")
        print("--" * 20)
        user_login()

    else:
        print("invalid login type!!")
        print("--" * 20)


# Main program loop for user selection
login_type = ""
while True:
    try:
        choice = int(input("enter the choice(integers only): "))
        if choice <= 0:
            print("enter value greater than 0")
        elif choice > 0 and choice < 4:
            if choice == 1:
                login_type = "admin"
                login(login_type.lower())
                break
            elif choice == 2:
                login_type = "staff"
                login(login_type.lower())
                break
            elif choice == 3:
                login_type = "user"
                login(login_type.lower())
                break
            else:
                print("Invalid choice!!")
                break
        else:
            print("Please select appropriate range")
    except ValueError:
        print("Please enter a valid integer.")
