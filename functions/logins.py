from functions.mail_checker import email_checker
from functions.username_checker import (
    password_checker_admin,
    username_checker_staff,
    username_checker_user,
)


def admin_login():
    print("new function being executed!!")
    # creds!!  username,email and password hunxa!!
    # sabai chai correct format ma  hunu paryo!!tries chai  three  times
    tries = 0
    while tries < 3:
        email = str(input("Please enter the valid  email:"))
        password = input("\nPlease enter your username(LBEF-adXXXXXX):")

        # things to check in email:
        # position of @,.com,
        email_response = email_checker(email)
        password_response = password_checker_admin(password)
        # username_response = username_checker(username)
        print(email_response, password_response)
        if email_response == True and password_response == True:
            print(" admin e-mail verified!!")
            print("\ncurrent satus: 🟢")
            ## we can keep  functions for the task  now:
            print(
                " Hello!! यति भयेसि  amdin login भयो । अब आफ़्नो  फ़िचर्स हरु add गर्न मिल्छ।"
            )

            break
        else:
            print("Try again!!")
            print(f"current try: {tries+1}")
        tries += 1


def staff_login():
    tries = 0
    print("staff login  function executed")
    if tries == 3:
        print("Thank you  so much  for using the management tool")
    while tries < 3:
        username = input("\nPlease enter your username(LBEF-stf XXXXXX):")
        email = str(input("Please enter the valid  email:"))
        email_response = email_checker(email)
        username_response = username_checker_staff(username)
        # print(email_response, username_response:kept  for  uncommenting when  required  for  testing
        # purposes
        if email_response == True and username_response == True:
            print("staff mail verified!!")
            print("\ncurrent satus: 🟢")
            isLoggedin = True
            # print("यति भयेसि staff login भयो । अब आफ़्नो  फ़िचर्स हरु add गर्न मिल्छ।")

            break

        else:
            print("Try again!!")
            print(f"current try: {tries+1}")
            isLoggedin = False
            tries += 1


def user_login():
    tries = 0
    print("staff login  function executed")
    if tries == 3:
        print("Thank you  so much  for using the management tool")
    while tries < 3:
        username = input("\nPlease enter your username(LBEF-usr XXXXXX):")
        email = str(input("Please enter the valid  email:"))
        email_response = email_checker(email)
        username_response = username_checker_staff(username)
        # print(email_response, username_response:kept  for  uncommenting when  required  for  testing
        # purposes
        if email_response == True and username_response == True:
            print("staff mail verified!!")
            print("\ncurrent satus: 🟢")
            isLoggedin = True
            # print("यति भयेसि user login भयो । अब आफ़्नो  फ़िचर्स हरु add गर्न मिल्छ।")

            break

        else:
            print("Try again!!")
            print(f"current try: {tries+1}")
            isLoggedin = False
            tries += 1
