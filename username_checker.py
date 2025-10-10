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
        return False
    else:
        return True
