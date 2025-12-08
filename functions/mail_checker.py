def email_checker(email):
    atpos = email.find("@")  ##possible values -1 or greater than this value
    dot_pos = email.find(".com")
    username_and_domain = email.split("@")
    username = str(username_and_domain[0])
    domain = str(username_and_domain[1]).rstrip(".com")
    tld = email[email.rfind(".") + 1 :]
    valid_tlds = ["com", "info", "org", "net", "edu"]

    if atpos == -1:
        print("Your email address is missing '@'")
        return False

    elif atpos < 1:
        print("The position of '@' is  not correct")
        return False

    elif dot_pos < 7:
        print("Please  check postion of the dot'.'")
        return False

    # elif dot_pos != -1:
    #     print(f"dot at:{dot_pos}")
    #     return False

    elif email.startswith(".") or email.endswith("."):
        # print("Wrong position of: .")
        return False

    elif email.count("@") == 2:
        # print("@ charcters exceeded")
        return False
    elif email.count(".") == 2:
        # print(". characters  exceeded!!")
        return False

    elif not username:
        # print("No username in the email!!")
        return False

    elif not domain:
        # print("domain(gmail) is missing")
        return False

    elif tld not in valid_tlds:
        # print("Invalid tld")
        return False
    else:
        return True
