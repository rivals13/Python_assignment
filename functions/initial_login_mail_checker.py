import os

admin_path = "functions/cred_files/admin.txt"
staff_path = "functions/cred_files/staff.txt"
user_path = "functions/cred_files/user.txt"

# Admin details
emails = []
ad_names = []
admin_passwords = []

# Staff details
staff_emails = []
staff_names = []
staff_passwords = []

# user details
user_names = []
user_passwords = []
user_emails = []

# Read admin file
with open(admin_path, "r") as admin_file:
    lines = admin_file.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith("email="):
            ignored_value, value = line.split("=", 1)
            emails.append(value)
        if line.startswith("password="):
            ignored_value, value = line.split("=", 1)
            admin_passwords.append(value)
        if line.startswith("name="):
            ignored_value, value = line.split("=", 1)
            ad_names.append(value)

# Read staff  file
with open(staff_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith("email="):
            ignored_value, value = line.split("=", 1)
            staff_emails.append(value)
        if line.startswith("password="):
            ignored_value, value = line.split("=", 1)
            staff_passwords.append(value)
        if line.startswith("name="):
            ignored_value, value = line.split("=", 1)
            staff_names.append(value)

# read users files
with open(user_path, "r") as user_file:
    lines = user_file.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith("email="):
            ignored_value, value = line.split("=", 1)
            user_emails.append(value)
        if line.startswith("password="):
            ignored_value, value = line.split("=", 1)
            user_passwords.append(value)
        if line.startswith("name="):
            ignored_value, value = line.split("=", 1)
            user_names.append(value)


def email_checker(email):
    valid_tlds = ["com", "info", "org", "net", "edu"]
    first_stage = True

    # length check FIRST
    if len(email) < 4:
        print("Email is too short")
        return 0

    # must contain exactly one @
    if email.count("@") != 1:
        print("Email must contain exactly one '@'")
        return 0

    atpos = email.find("@")

    # '@' position check
    if atpos < 1:
        print("Invalid position of '@'")
        return 0

    # must contain dot
    if "." not in email:
        print("Email must contain a dot (.)")
        return 0

    # now SAFE to split
    username, domain_part = email.split("@")

    if not username:
        print("Username part is missing")
        return 0

    if "." not in domain_part:
        print("Domain part is invalid")
        return 0

    domain, tld = domain_part.rsplit(".", 1)
    # this  has been done to ensure that  we can work  easily  with email addresses having
    # multiple dots within the e-mail.

    if not domain:
        print("Domain name is missing")
        return 0

    if tld not in valid_tlds:
        print("Invalid top-level domain")
        return 0

    # checking if the email exists in admin list
    if email in emails:
        email_index = emails.index(email)
        admin_name = ad_names[email_index]
        return 1, admin_name

    # checking if the email exists in user list
    elif email in staff_emails:
        email_index = staff_emails.index(email)
        staff_name = staff_names[email_index]
        return 1, staff_name
    # checking user emails:

    elif email in user_emails:
        email_index = user_emails.index(email)
        staff_name = user_names[email_index]
        return 1, staff_name

    # Email is valid but not registered
    else:
        print("Email not found in our records")
        return 0
