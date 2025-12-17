import os
admin_path='functions/cred_files/admin.txt'
staff_path='functions/cred_files/staff.txt'
user_path='functions/cred_files/user.txt'
emails=[]
admin_passwords=[]
staff_passwords=[]
staff_emails=[]
user_passwords=[]
user_emails=[]
with open(admin_path, "r") as file:
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith("email="):
            ignored_value, value = line.split("=", 1)
            emails.append(value)
        if line.startswith("password="):
            ignored_value, value = line.split("=", 1)
            admin_passwords.append(value)


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
with open(user_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith("email="):
            ignored_value, value = line.split("=", 1)
            user_emails.append(value)
        if line.startswith("password="):
            ignored_value, value = line.split("=", 1)
            user_passwords.append(value)




def password_checker_admin(password):
    if password not in admin_passwords:
        return  False

    else:
        return True


def password_checker_staff(username):
    if username not in staff_passwords:
        return  False
    else:
        return True


def password_checker_user(username):

    if username not in user_passwords:
        return False


    else:
        return True
