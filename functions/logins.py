from functions.mail_checker import email_checker
from functions.password_checker import (
    password_checker_admin,
    password_checker_staff,
    password_checker_user,
)
from functions.admin_feature import admin_menu
from functions.staff_feature import staff_menu
from functions.customer_features import user_menu
from datetime import date

def admin_login():
    print("new function being executed!!")
    tries = 0
    while tries < 3:
        email = str(input("Please enter the valid email:"))
        password = input("\nPlease enter your Password(LBEF-adXXXXXX):")

        email_result = email_checker(email)

        # Handle different return types
        if email_result == 0:
            email_response = 0
            admin_name = None
            print("Email validation failed or not registered")
        else:
            email_response, admin_name = email_result
            print(f"Email found - Admin: {admin_name}")

        password_response = password_checker_admin(password)

        if email_response == 1 and password_response == 1:
            print("admin e-mail verified!!")
            print("\ncurrent status: loggedin(🟢)")
            print(f"Welcome, {admin_name}!")
            admin_menu()
            break
        else:
            print("Try again!!")
            tries += 1
            print(f"current try: {tries}")

    if tries == 3:
        print('Thank you for using the tool!')


def staff_login():
    tries = 0
    print("staff login function executed")

    while tries < 3:
        email = str(input("Please enter the valid email:"))
        password = input("\nPlease enter your Password(LBEF-stf XXXXXX):")

        email_result = email_checker(email)

        if email_result == 0:
            email_response = 0
            staff_name = None
            print("Email validation failed or not registered")
        else:
            email_response, staff_name = email_result
            print(f"Email found - Staff: {staff_name}")

        password_response = password_checker_staff(password)

        if email_response == 1 and password_response == 1:
            print("staff mail verified!!")
            print("\ncurrent status:  loggedin(🟢)")
            print(f"Welcome, {staff_name}!")
            staff_menu()
            break
        else:
            print("Try again!!")
            tries += 1
            print(f"current try: {tries}")

    if tries == 3:
        print('Thank you for using the tool!')


def user_login():
    tries = 0
    print("user login function executed")

    while tries < 3:
        email = str(input("Please enter the valid email:"))
        password = input("\nPlease enter your password(LBEF-usr XXXXXX):")

        email_result = email_checker(email)

        if email_result == 0:
            email_response = 0
            user_name = None
            print("Email validation failed or not registered")
        else:
            email_response, user_name = email_result
            print(f"Email found - User: {user_name}")

        password_response = password_checker_user(password)

        if email_response == 1 and password_response == 1:
            print("user mail verified!!")
            print("\ncurrent status: loggedin(🟢)")
            print(f"Welcome, {user_name}!")
            user_menu()
            break
        else:
            print("Try again!!")
            tries += 1
            print(f"current try: {tries}")

    if tries == 3:
        print('Thank you for using the tool!')