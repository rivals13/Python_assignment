from functions.logins import admin_login, staff_login, user_login


isLoggedin = False


def welcome_display():
    print("Welcome to the banking management system")
    print("==" * 20)
    print("select one option")
    print("--" * 20)
    print("1 |Admin login 👨🏻‍💻|")
    print("\n2 |Staff Login 👨🏻‍💼|")
    print("\n3 |Customer Login 👨🏻‍|")
    print("\n current satus: 🔴")
    print("--" * 20)


if not isLoggedin:
    welcome_display()

# so login()  vanne function le chai  k garxa vanda hamilai chai.. kun type ko login garna lako vanera vandinxa!


def login(type_var):
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
