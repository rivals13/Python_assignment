"""
Password Checker Module

This module provides password validation functions for different user types.
Loads stored passwords from credential files and checks input passwords against them.

Functions:
- password_checker_admin(): Validate admin passwords
- password_checker_staff(): Validate staff passwords
- password_checker_user(): Validate customer passwords
"""

import os

# File paths for credential storage
admin_path='functions/cred_files/admin.txt'
staff_path='functions/cred_files/staff.txt'
user_path='functions/cred_files/user.txt'

# Lists to store loaded credentials
emails=[]
admin_passwords=[]
staff_passwords=[]
staff_emails=[]
user_passwords=[]
user_emails=[]

# Load admin credentials
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

# Load staff credentials
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

# Load user credentials
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
    """
    Check if the provided password matches any stored admin password.

    Args:
        password (str): Password to check

    Returns:
        int: 1 if password is valid, 0 otherwise
    """
    if password not in admin_passwords:
        return  False

    else:
        return True


def password_checker_staff(password):
    """
    Check if the provided password matches any stored staff password.

    Args:
        password (str): Password to check

    Returns:
        bool: True if password is valid, False otherwise
    """
    if password not in staff_passwords:
        return False
    else:
        return True


def password_checker_user(password):
    """
    Check if the provided password matches any stored customer password.

    Args:
        password (str): Password to check

    Returns:
        bool: True if password is valid, False otherwise
    """
    if password not in user_passwords:
        return False
    else:
        return True
