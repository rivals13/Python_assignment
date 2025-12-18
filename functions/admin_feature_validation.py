import string
from functions.initial_login_mail_checker  import email_checker

admin_path = "functions/cred_files/admin.txt"
staff_path = "functions/cred_files/staff.txt"
user_path = "functions/cred_files/user.txt"

# User details
user_emails = []
user_names = []
user_passwords = []
user_citizenship = []
user_contact = []

# Admin details
admin_emails = []
admin_names = []
admin_passwords = []

# Staff details
staff_emails = []
staff_names = []
staff_passwords = []
staff_citizenship = []
staff_contact = []
staff_ids = []

# Read admin file
with open(admin_path, "r") as admin_file:
    lines = admin_file.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith("email="):
            ignored_value, value = line.split("=", 1)
            admin_emails.append(value)
        if line.startswith("password="):
            ignored_value, value = line.split("=", 1)
            admin_passwords.append(value)
        if line.startswith("name="):
            ignored_value, value = line.split("=", 1)
            admin_names.append(value)

# Read staff file
with open(staff_path, "r") as staff_file:
    lines = staff_file.readlines()
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
        if line.startswith("citizenship="):
            ignored_value, value = line.split("=", 1)
            staff_citizenship.append(value)
        if line.startswith("contact="):
            ignored_value, value = line.split("=", 1)
            staff_contact.append(value)

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

        if line.startswith("staff_id="):
            ignored_value, value = line.split("=", 1)
            staff_ids.append(value)



def validate_staff_details(
    name,
    email,
    contact_number,
    password,
    citizenship_number,
    address,
    nationality,
    staff_id,
):
    # Name validation
    if name.isdigit():
        print("Error: Name cannot be digits")
        return False
    if len(name) < 2:
        print("Error: Name is too short")
        return False
    if not all(c.isalpha() or c.isspace() for c in name):
        print("Error: Name can only contain letters and spaces")
        return False

    # Email validation
    if email in staff_emails:
        print("Error: Staff email already exists!")
        return False
    if email.isdigit():
        print("Error: Invalid email format")
        return False


    # Contact validation
    if not contact_number.isdigit():
        print("Error: Contact number must contain only digits")
        return False
    if len(contact_number) != 10:
        print("Error: Contact number must be exactly 10 digits")
        return False
    if contact_number in staff_contact:
        print("Error: Contact number already exists!")
        return False

    # Password validation
    if password in staff_passwords:
        print("Error: Password already in use!")
        return False
    # staff_id validation
    if password in staff_ids:
        print("Error: Staff id  already exists!")
        return False

    # Citizenship validation
    if citizenship_number in staff_citizenship:
        print("Error: Citizenship number already exists!")
        return False
    if not citizenship_number.isdigit():
        print("Error: Citizenship number must contain only digits")
        return False
    if len(citizenship_number) < 5:
        print("Error: Citizenship number is too short")
        return False

    # Address validation
    if address.isdigit():
        print("Error: Address cannot be only digits")
        return False
    if len(address) < 3:
        print("Error: Address is too short")
        return False

    # Nationality validation
    if nationality.isdigit():
        print("Error: Nationality cannot be only digits")
        return False
    if len(nationality) < 3:
        print("Error: Nationality is too short")
        return False
    if not all(c.isalpha() or c.isspace() for c in nationality):
        print("Error: Nationality can only contain letters and spaces")
        return False

    # Empty field checks
    if not name.strip():
        print("Error: Name cannot be empty")
        return False
    if not email.strip():
        print("Error: Email cannot be empty")
        return False
    if not password.strip():
        print("Error: Password cannot be empty")
        return False
    if not address.strip():
        print("Error: Address cannot be empty")
        return False
    if not nationality.strip():
        print("Error: Nationality cannot be empty")
        return False

    # validating the  email address of the new staff:

    valid_tlds = ["com", "info", "org", "net", "edu"]
    first_stage = True

    # length check FIRST
    if len(email) < 4:
        print("Email is too short")
        return False

    # must contain exactly one @
    if email.count("@") != 1:
        print("Email must contain exactly one '@'")
        return False

    atpos = email.find("@")

    # '@' position check
    if atpos < 1:
        print("Invalid position of '@'")
        return False

    # must contain dot
    if "." not in email:
        print("Email must contain a dot (.)")
        return False

    # now SAFE to split
    username, domain_part = email.split("@")

    if not username:
        print("Username part is missing")
        return False

    if "." not in domain_part:
        print("Domain part is invalid")
        return False

    domain, tld = domain_part.rsplit(".", 1)
    # this  has been done to ensure that  we can work  easily  with email addresses having
    # multiple dots within the e-mail.

    if not domain:
        print("Domain name is missing")
        return False

    if tld not in valid_tlds:
        print("Invalid top-level domain")
        return False

    # checking if the email exists in user list
    if email in staff_emails or email in admin_emails or email in user_emails:
    
        print("The  email already exists!")
        return False

    return True
