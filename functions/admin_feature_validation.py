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
    age,
):
    errors = []
    
    # Name validation
    if name.isdigit():
        errors.append("Error: Name cannot be digits")
    if len(name) < 2:
        errors.append("Error: Name is too short")
    if not all(c.isalpha() or c.isspace() for c in name):
        errors.append("Error: Name can only contain letters and spaces")

    # Email validation
    if email in staff_emails:
        errors.append("Error: Staff email already exists!")
    if email.isdigit():
        errors.append("Error: Invalid email format")

    # Contact validation
    if not contact_number.isdigit():
        errors.append("Error: Contact number must contain only digits")
    if len(contact_number) != 10:
        errors.append("Error: Contact number must be exactly 10 digits")
    if contact_number in staff_contact:
        errors.append("Error: Contact number already exists!")

    # Password validation
    if password in staff_passwords:
        errors.append("Error: Password already in use!")
    # staff_id validation
    if password in staff_ids:
        errors.append("Error: Staff id  already exists!")

    # Citizenship validation
    if citizenship_number in staff_citizenship:
        errors.append("Error: Citizenship number already exists!")
    if not citizenship_number.isdigit():
        errors.append("Error: Citizenship number must contain only digits")
    if len(citizenship_number) < 5:
        errors.append("Error: Citizenship number is too short")

    # Address validation
    if address.isdigit():
        errors.append("Error: Address cannot be only digits")
    if len(address) < 3:
        errors.append("Error: Address is too short")

    # Nationality validation
    if nationality.isdigit():
        errors.append("Error: Nationality cannot be only digits")
    if len(nationality) < 3:
        errors.append("Error: Nationality is too short")
    if not all(c.isalpha() or c.isspace() for c in nationality):
        errors.append("Error: Nationality can only contain letters and spaces")

    # Age validation
    try:
        age_int = int(age)
        if age_int <= 18:
            errors.append("Error: Age must be greater than 18")
        if age_int >= 60:
            errors.append("Error: Age must be less than 60")
    except ValueError:
        errors.append("Error: Age must be a valid number")

    # Empty field checks
    if not name.strip():
        errors.append("Error: Name cannot be empty")
    if not email.strip():
        errors.append("Error: Email cannot be empty")
    if not password.strip():
        errors.append("Error: Password cannot be empty")
    if not address.strip():
        errors.append("Error: Address cannot be empty")
    if not nationality.strip():
        errors.append("Error: Nationality cannot be empty")
    if not age.strip():
        errors.append("Error: Age cannot be empty")

    # validating the  email address of the new staff:

    valid_tlds = ["com", "info", "org", "net", "edu"]

    # length check FIRST
    if len(email) < 4:
        errors.append("Email is too short")

    # must contain exactly one @
    if email.count("@") != 1:
        errors.append("Email must contain exactly one '@'")
    else:
        atpos = email.find("@")

        # '@' position check
        if atpos < 1:
            errors.append("Invalid position of '@'")

        # must contain dot
        if "." not in email:
            errors.append("Email must contain a dot (.)")

        # now SAFE to split
        username, domain_part = email.split("@")

        if not username:
            errors.append("Username part is missing")

        if "." not in domain_part:
            errors.append("Domain part is invalid")

        domain, tld = domain_part.rsplit(".", 1)
        # this  has been done to ensure that  we can work  easily  with email addresses having
        # multiple dots within the e-mail.

        if not domain:
            errors.append("Domain name is missing")

        if tld not in valid_tlds:
            errors.append("Invalid top-level domain")

    # checking if the email exists in user list
    if email in staff_emails or email in admin_emails or email in user_emails:
        errors.append("The  email already exists!")

    if errors:
        for error in errors:
            print('\n')
            print(error)
        return False
    return True
