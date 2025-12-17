import  string
from functions.mail_checker import email_checker
admin_path = "functions/cred_files/admin.txt"
staff_path = "functions/cred_files/staff.txt"
user_path = "functions/cred_files/user.txt"

# Staff details
staff_emails = []
staff_names = []
staff_passwords = []
staff_citizenship=[]
staff_contact=[]

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


def validate_staff_details(name, email, contact_number, password,
                           citizenship_number, address, nationality):
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
        print('Error: Staff email already exists!')
        return False
    if email.isdigit():
        print("Error: Invalid email format")
        return False
    if not email_checker(email):
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
        print('Error: Contact number already exists!')
        return False

    # Password validation
    if password in staff_passwords:
        print('Error: Password already in use!')
        return False
    if len(password) < 8:
        print("Error: Password must be at least 8 characters")
        return False
    if not any(c.isupper() for c in password):
        print("Error: Password must contain at least one uppercase letter")
        return False
    if not any(c.islower() for c in password):
        print("Error: Password must contain at least one lowercase letter")
        return False
    if not any(c.isdigit() for c in password):
        print("Error: Password must contain at least one digit")
        return False
    if not any(c in string.punctuation for c in password):
        print("Error: Password must contain at least one special character")
        return False

    # Citizenship validation
    if citizenship_number in staff_citizenship:
        print('Error: Citizenship number already exists!')
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

    return True

