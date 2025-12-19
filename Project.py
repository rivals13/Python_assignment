from functions.logins import admin_login, staff_login, user_login
from functions.cli_utils import clear_screen #contains the function to clear the screen
import time

# this is the main file  of the project
# We have our  functions stored in the functions directory, so  we
# are just importing the functions in the program.
isLoggedin = False  # Initial status of Login


def welcome_display():

    
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




if not isLoggedin: #show welcome display only when not logged in
    welcome_display()


def login(type_var):
    # Clear the terminal before showing the login prompt
    clear_screen()
    if type_var == "admin":
        print()
        print(f"you are trying to login in as: '{type_var}'")
        print("--" * 20)
        admin_login()  ## this is the  entry  point of the  function!!!
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


# clear_screen()


login_type = ""
while True:
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
