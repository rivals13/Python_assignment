def password_checker_admin(password):
    digits = ""
    user_tag = password.rstrip("0123456789")
    for u in password:
        if u.isdigit():
            digits += u
    # print(digits)
    # print(user_tag)
    if digits != "123" and user_tag != "LBEF-ad":
        print("(error):-the tag or the number is not matching!!")
        return False
    else:
        return True


def username_checker_staff(username):
    digits = ""
    user_tag = username.rstrip("0123456789")
    for u in username:
        if u.isdigit():
            digits += u
    # print(digits)
    # print(user_tag)
    if digits != "123" and user_tag != "LBEF-stf":
        print("(error):-the tag or the nunber is not matching!!")
        return False
    else:
        return True


def username_checker_user():
    digits = ""
    user_tag = username.rstrip("0123456789")
    for u in username:
        if u.isdigit():
            digits += u
    # print(digits)
    # print(user_tag)
    if digits != "123" and user_tag != "LBEF-usr":
        print("(error):-the tag or the nunber is not matching!!")
        return False
    else:
        return True
