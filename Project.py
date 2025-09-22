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
        admin_login()

    elif type_var == "staff":
        print()
        print(f"You are trying to login in as: {type_var}")
        print("--" * 20)

    elif type_var == "user":
        print()
        print(f"You are ttrying to login as: {type_var}")
        print("--" * 20)

    else:
        print("invalid type!!")
        print("--" * 20)


def email_checker(email):
    atpos = email.find("@")  ##possible values -1 or greater than this value
    dot_pos = email.find(".com")
    local_and_tld = email.split("@")
    print(f"@ at: {atpos}")
    print(f"dot at:{dot_pos}")


def username_checker(username):
    digits = ""
    user_tag = username.rstrip("0123456789")
    for u in username:
        if u.isdigit():
            digits += u
    print(digits)
    print(user_tag)
    if digits != "986532" and user_tag != "LBEF-ad":
        print("the tag or the nunber is not matching!!")


def admin_login():
    print("new function being executed!!")
    # creds!!  username,email and password hunxa!!
    # sabai chai correct format ma  hunu paryo!!tries chai  three  times
    tries = 0
    while tries < 3:
        username = input("\nPlease enter your username(LBEF-adXXXXXX):")
        email = str(input("Please enter your email:"))
        # things to check in email:
        # position of @,.com,
        email_response = email_checker(email)
        username_response = username_checker(username)
        print(f"current try: {tries+1}")
        tries += 1


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
