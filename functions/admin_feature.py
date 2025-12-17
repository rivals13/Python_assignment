import random as rd
from datetime import date
import os
from functions.admin_feature_validation import  validate_staff_details

staff_file = "functions/cred_files/staff.txt"
user_file = "functions/cred_files/user.txt"


def create_staff():
    account_created_date = date.today().strftime("%Y-%m-%d")
    #  few basic and  must be validated   for each entries
    staff_fixed_value = "LBEF-stf"
    password_value = rd.randint(1000, 9999)
    password = staff_fixed_value + str(password_value)
    staff_id = rd.randint(100000, 999999)

    print("\n---Staff Account creation portal ---")
    name = input("Enter the name of the employee: ")
    email = input("Enter the email address of the employee: ")
    address =input("Enter the address of the employee: ")
    contact_number = input("Enter the contact number of the employee: ")
    nationality = input("Enter the nationality of the employee: ")
    citizenship_number = input("Enter the citizenship number of the employee: ")
    write_response= validate_staff_details(name,email,contact_number, password, citizenship_number,address,nationality)
    if write_response:

        with open(staff_file, "a") as user_details:
            user_details.write(
                f"staff_id={staff_id}\n"
                f"email={email}\n"
                f"name={name}\n"
                f"password={password}\n"
                f"created_on={account_created_date}\n"
                f"last_logged_in={date.today()}\n"
                f"address={address}\n"
                f"Contact_number={contact_number}\n"
                f"nationality={nationality}\n"
                f"Citizenship={citizenship_number}\n"
                "---\n"
            )

    # supposed to   use the writing once!!
# validation  is needed for each entries!!!

            print(f"\nStaff account created successfully!")
            print(f"Staff ID: {staff_id}")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Your password: {password}")
    else:
        print('Data couldn\'t be  written to the file!')


def view_all_details():
    print("Choose appropriate option:")
    print("1. View staff details")
    print("2. View users details")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\n--- Staff Details ---")
        if os.path.exists(staff_file):
            with open(staff_file, "r") as file:
                content = file.read().strip()
                if content:
                    print("\n" + "=" * 60)
                    print(content)
                    print("=" * 60)
                else:
                    print("No staff data in the file!")
        else:
            print("Staff file does not exist!")

    elif choice == "2":
        print("\n--- User Details ---")
        if os.path.exists(user_file):
            with open(user_file, "r") as file:
                content = file.read().strip()
                if content:
                    print("\n" + "=" * 60)
                    print(content)
                    print("=" * 60)
                else:
                    print("No user data in the file!")
        else:
            print("User file does not exist!")

    else:
        print("Invalid input! Please enter 1 or 2.")


def print_customer_records():
    print("\n--- Print Customer Records ---")

    if not os.path.exists(user_file):
        print("No customer records found.")
        return

    with open(user_file, "r") as f:
        content = f.read().strip()

    if not content:
        print("No customer records found.")
        return

    # Parse and display records
    records = content.split("---\n")
    customer_count = 0

    print("\n" + "=" * 100)
    print(f" {'Name':<25} {'Email':<35} {'Created On':<15}")
    print("=" * 100)

    for record in records:
        record = record.strip()
        if not record:
            continue

        customer_count += 1
        customer_data = {}
        lines = record.split("\n")

        for line in lines:
            if "=" in line:
                key, value = line.split("=", 1)
                customer_data[key] = value

        print(

            f"{customer_data.get('name', 'N/A'):<25} "
            f"{customer_data.get('email', 'N/A'):<35} "
            f"{customer_data.get('created_on', 'N/A'):<15}"
        )

    print("=" * 100)
    print(f"\nTotal Customer Records: {customer_count}\n")


def search_by_id_or_email():
    key = input("Enter ID or Email to search: ")
    found = False

    print("\n--- Search in Staff ---")
    if os.path.exists(staff_file):
        with open(staff_file, "r") as f:
            content = f.read()
            records = content.split("---\n")
            for record in records:
                if key in record:
                    print("FOUND (Staff):")
                    print(record.strip())
                    print()
                    found = True
    else:
        print("Staff file does not exist.")

    print("\n--- Search in Customers ---")
    if os.path.exists(user_file):
        with open(user_file, "r") as f:
            content = f.read()
            records = content.split("---\n")
            for record in records:
                if key in record:
                    print("FOUND (Customer):")
                    print(record.strip())
                    print()
                    found = True
    else:
        print("Customer file does not exist.")

    if not found:
        print("No matching records found.")


def admin_menu():
    while True:
        print("\n========== ADMIN MENU ==========")
        print("1. Create Staff Account")
        print("2. View All Staff and Customer Details")
        print("3. Print Customer Records")
        print("4. Search by ID or Email")
        print("5. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            create_staff()
        elif choice == "2":
            view_all_details()
        elif choice == "3":
            print_customer_records()
        elif choice == "4":
            search_by_id_or_email()
        elif choice == "5":
            print("Admin logged out.")
            break
        else:
            print("Invalid choice. Try again.")


