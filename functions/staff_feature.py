"""
Staff Features Module

This module contains functions for staff operations in the banking management system.
Includes customer registration, account management, updates, and viewing functionality.

Functions:
- generate_account_number(): Generate unique account numbers
- register_customer(): Register new customers with validation
- update_customer_details(): Update or delete customer records
- view_all_customers(): Display all customer details
"""

import random as rd
from datetime import date, datetime
import os
from  functions.user_details_validation import  validate_user_details
from functions.cli_utils import clear_screen
# File paths for storing data
staff_file = 'functions/cred_files/staff.txt'
user_file = "functions/cred_files/user.txt"
TRANSACTION_FILE = "functions/cred_files/transaction.txt"


# ============ STAFF FUNCTIONS ============

def generate_account_number():
    """
    Generate a unique 10-digit account number for new customers.
    Simply generates a random 10-digit number.

    Returns:
        int: A 10-digit account number
    """
    # Generate random 10-digit number (1000000000 to 9999999999)
    account_number = rd.randint(1000000000, 9999999999)
    return account_number


def register_customer():
    """
    Register a new customer by collecting their details and saving to file.

    Collects customer information including personal details, validates input,
    generates unique account number and password, and saves to file if valid.
    """
    print("\n--- Register Customer ---")

    # Collect customer information
    name = input("Customer Name: ")
    email = input("Customer Email: ")
    account_type = input("Account Type (Savings/Current): ")
    address = input("Enter the address of the customer: ")
    contact_number = input("Enter the contact number of the customer: ")
    nationality = input("Enter the nationality of the customer: ")
    citizenship_number = input("Enter the citizenship number of the customer: ")
    age = input("Enter the age of the customer: ")
    # Generate account credentials
    account_number = generate_account_number()
    password_value = rd.randint(1000, 9999)
    default_password = f"LBEF-usr{password_value}"

    # Set initial account details
    balance = 0
    created_date = date.today().strftime("%Y-%m-%d")

    # Create directory if it doesn't exist
    os.makedirs('cred_files', exist_ok=True)
    write_response = validate_user_details(name, email, contact_number, default_password, citizenship_number, address, nationality, age)

    # Write customer data to file in proper format
    if write_response:
        with open(user_file, "a") as f:
            f.write(
            f"account_number={account_number}\n"
            f"email={email}\n"
            f"name={name}\n"
            f"account_type={account_type}\n"
            f"password={default_password}\n"
            f"balance={balance}\n"
            f"created_on={created_date}\n"
            f"last_logged_in={created_date}\n"
            f"age={age}\n"
            "---\n"
        )

    # Display success message with account details
        print(f"\nCustomer registered successfully!")
        print(f"Account Number: {account_number}")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Default Password: {default_password}")
        print(f"Initial Balance: Rs. {balance}")
    else:
        print('couldn\'t write data on the  file')



def update_customer_details():
    """
    Update or delete existing customer details such as account type, password, or email.
    Searches for customer by account number and allows modification or deletion.
    """
    acc = input("Enter customer account number: ")

    # Check if customer file exists
    if not os.path.exists(user_file):
        print("No customer records found.")
        return

    # Read all customer records
    with open(user_file, "r") as f:
        content = f.read().strip()

    if not content:
        print("No customer records found.")
        return

    # Parse records separated by "---"
    records = content.split("---\n")
    updated_records = []
    found = False

    # Loop through each customer record
    for record in records:
        record = record.strip()
        if not record:
            continue

        # Parse the record into a dictionary
        customer_data = {}
        lines = record.split("\n")
        for line in lines:
            if "=" in line:
                key, value = line.split("=", 1)
                customer_data[key] = value

        # Check if this is the account to update
        if customer_data.get('account_number') == acc:
            found = True
            print(f"\nFound customer: {customer_data.get('name')}")

            # Display update options
            print("\n1. Update Account Type")
            print("2. Update Password")
            print("3. Update Email")
            print("4. Delete Customer")
            choice = input("\nChoose: ")

            if choice == "4":
                print("Customer deleted successfully.")
                continue  # Skip adding to updated_records

            # Update based on user choice
            if choice == "1":
                new_type = input("Enter new account type (Savings/Current): ")
                customer_data['account_type'] = new_type
                print("Account type updated!")
            elif choice == "2":
                new_pw = input("Enter new password: ")
                if len(new_pw) != 12 or not new_pw.startswith("LBEF-usr") or not new_pw[8:].isdigit() or len(new_pw[8:]) != 4:
                    print("Invalid password format! Password must be in the format LBEF-usrXXXX (where XXXX are 4 digits).")
                else:
                    customer_data['password'] = new_pw
                    print("Password updated!")
            elif choice == "3":
                new_email = input("Enter new email: ")
                customer_data['email'] = new_email
                print("Email updated!")
            else:
                print("Invalid choice.")

        # Rebuild the record in proper format
        record_str = ""
        for key, value in customer_data.items():
            record_str += f"{key}={value}\n"
        updated_records.append(record_str)

    # Check if account was found
    if not found:
        print("Account not found.")
        return

    # Write all records back to file
    with open(user_file, "w") as f:
        for record in updated_records:
            f.write(record)
            f.write("---\n")

    if choice != "4":  # Only print if not deleted
        print("\n✅ Customer details updated successfully.")


def generate_statement():
    """
    Generate account statement for a customer within a specified date range.
    Shows all transactions (deposits and withdrawals) and calculates totals.
    """
    acc = input("Enter customer account number: ")
    start = input("Start date (YYYY-MM-DD): ")
    end = input("End date (YYYY-MM-DD): ")

    # Validate date format
    try:
        sd = datetime.strptime(start, "%Y-%m-%d")
        ed = datetime.strptime(end, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD format.")
        return

    # Find customer details from user file
    customer_name = "Unknown"
    customer_balance = 0

    if os.path.exists(user_file):
        with open(user_file, "r") as f:
            content = f.read().strip()
            records = content.split("---\n")

            # Search for customer by account number
            for record in records:
                if not record.strip():
                    continue
                lines = record.strip().split("\n")
                customer_data = {}

                for line in lines:
                    if "=" in line:
                        key, value = line.split("=", 1)
                        customer_data[key] = value

                # If found, extract customer details
                if customer_data.get('account_number') == acc:
                    customer_name = customer_data.get('name', 'Unknown')
                    customer_balance = customer_data.get('balance', 0)
                    break

    # Print statement header
    print("\n" + "=" * 80)
    print(f"CUSTOMER STATEMENT")
    print("=" * 80)
    print(f"Account Number: {acc}")
    print(f"Customer Name: {customer_name}")
    print(f"Period: {start} to {end}")
    print(f"Current Balance: Rs. {customer_balance}")
    print("=" * 80)
    print(f"{'Date':<15} {'Type':<15} {'Amount':<15} {'Balance':<15}")
    print("=" * 80)

    # Initialize transaction counters
    total_dep = 0
    total_wd = 0
    transaction_count = 0

    # Read and display transactions within date range
    if os.path.exists(TRANSACTION_FILE):
        with open(TRANSACTION_FILE, "r") as f:
            content = f.read().strip()
        
        if content:
            records = content.split("---\n")
            
            for record in records:
                record = record.strip()
                if not record:
                    continue
                
                # Parse transaction data
                transaction_data = {
                    'account_number': '',
                    'type': '',
                    'amount': '0',
                    'date': ''
                }
                
                lines = record.split("\n")
                for line in lines:
                    if "=" in line:
                        key, value = line.split("=", 1)
                        if key in transaction_data:
                            transaction_data[key] = value
                
                # Check if transaction belongs to this account
                if transaction_data['account_number'] == acc:
                    try:
                        dt = datetime.strptime(transaction_data['date'], "%Y-%m-%d")
                        
                        # Check if transaction is within date range
                        if sd <= dt <= ed:
                            transaction_count += 1
                            amt = transaction_data['amount']
                            ttype = transaction_data['type']
                            d = transaction_data['date']
                            print(f"{d:<15} {ttype:<15} Rs. {amt:<12} ")
                            
                            # Update totals based on transaction type
                            if ttype == "DEPOSIT":
                                total_dep += int(amt)
                            else:
                                total_wd += int(amt)
                    except ValueError:
                        continue
        else:
            print("No transaction records found.")
    else:
        print("No transaction records found.")

    # Print statement footer with totals
    print("=" * 80)
    print(f"Total Transactions: {transaction_count}")
    print(f"Total Deposited: Rs. {total_dep}")
    print(f"Total Withdrawn: Rs. {total_wd}")
    print(f"Net Change: Rs. {total_dep - total_wd}")
    print("=" * 80)


def view_all_customers():
    """
    Display all registered customers in a formatted table.
    Shows account number, name, email, account type, and balance.
    """
    print("\n--- All Customers ---")

    # Check if customer file exists
    if not os.path.exists(user_file):
        print("No customer records found.")
        return

    # Read all customer data
    with open(user_file, "r") as f:
        content = f.read().strip()

    if not content:
        print("No customer records found.")
        return

    # Parse records
    records = content.split("---\n")
    customer_count = 0

    # Print table header
    print("\n" + "=" * 110)
    print(f"{'Account':<15} {'Name':<25} {'Email':<30} {'Type':<12} {'Balance':<15}")
    print("=" * 110)

    # Loop through and display each customer
    for record in records:
        record = record.strip()
        if not record:
            continue

        customer_count += 1

        # Initialize with default values
        account_number = ''
        name = ''
        email = ''
        account_type = ''
        balance = 0

        lines = record.split("\n")

        # Parse each line and assign to variables
        for line in lines:
            if "=" in line:
                key, value = line.split("=", 1)
                if key == 'account_number':
                    account_number = value
                elif key == 'name':
                    name = value
                elif key == 'email':
                    email = value
                elif key == 'account_type':
                    account_type = value
                elif key == 'balance':
                    balance = value

        # Display customer information
        print(
            f"{account_number:<15} "
            f"{name:<25} "
            f"{email:<30} "
            f"{account_type:<12} "
            f"Rs. {balance:<12}"
        )

    # Print table footer with total count
    print("=" * 110)
    print(f"\nTotal Customers: {customer_count}\n")

def staff_menu():
    """
    Main staff menu interface.
    Provides options for customer management and account operations.
    """
    while True:
        # Clear screen and display menu options
        
        print("\n========== STAFF MENU ==========")
        print("1. Register new Customer")
        print("2. Update Customer Details")
        print("3. Generate Statement of the Customer")
        print("4. View All Customers")
        print("5. Logout")

        choice = input("\nEnter your choice: ")

        # Handle user choice
        if choice == "1":
            register_customer()
        elif choice == "2":
            update_customer_details()
        elif choice == "3":
            generate_statement()
        elif choice == "4":
            view_all_customers()
        elif choice == "5":
            print("Staff logged out.")
            break
        else:
            print("Invalid choice. Try again.")

