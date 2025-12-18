import os
from datetime import date
from functions.cli_utils import clear_screen

# File paths for storing data (in parent directory's cred_files folder)
user_file = "functions/cred_files/user.txt"
TRANSACTION_FILE = "functions/cred_files/transaction.txt"


def parse_customer_data(content):
    """
    Parse customer data from file content.
    Returns a list of customer dictionaries with default values.
    """
    records = content.split("---\n")
    customers = []

    for record in records:
        record = record.strip()
        if not record:
            continue

        # Initialize with default values
        customer_data = {
            "account_number": "",
            "email": "",
            "name": "",
            "account_type": "",
            "password": "",
            "balance": "0",
            "created_on": "",
            "last_logged_in": "Never",
        }

        lines = record.split("\n")

        for line in lines:
            if "=" in line:
                key, value = line.split("=", 1)
                if key in customer_data:
                    customer_data[key] = value

        if customer_data["account_number"]:  # Only add if account number exists
            customers.append(customer_data)

    return customers


def save_customer_data(customers):
    """
    Save all customer data back to file.
    """
    with open(user_file, "w") as f:
        for customer in customers:
            for key, value in customer.items():
                f.write(f"{key}={value}\n")
            f.write("---\n")


def save_transaction(account_number, transaction_type, amount):
    """
    Save transaction in key=value format (single write).
    """
    os.makedirs(os.path.dirname(TRANSACTION_FILE), exist_ok=True)

    transaction_block = (
        f"account_number={account_number}\n"
        f"type={transaction_type}\n"
        f"amount={amount}\n"
        f"date={date.today().strftime('%Y-%m-%d')}\n"
        "---\n"
    )

    with open(TRANSACTION_FILE, "a") as f:
        f.write(transaction_block)


def parse_transactions(account_number):
    """
    Parse transactions from file for a specific account.
    Returns list of transaction dictionaries.
    """
    transactions = []

    if not os.path.exists(TRANSACTION_FILE):
        return transactions

    with open(TRANSACTION_FILE, "r") as f:
        content = f.read().strip()

    if not content:
        return transactions

    records = content.split("---\n")

    for record in records:
        record = record.strip()
        if not record:
            continue

        # Initialize transaction data
        transaction_data = {"account_number": "", "type": "", "amount": "0", "date": ""}

        lines = record.split("\n")
        for line in lines:
            if "=" in line:
                key, value = line.split("=", 1)
                if key in transaction_data:
                    transaction_data[key] = value

        # Only add if it matches the account number
        if transaction_data["account_number"] == account_number:
            transactions.append(transaction_data)

    return transactions


def deposit():
    """
    Deposit money into customer account.
    """
    acc = input("Enter your account number: ")
    amount = int(input("Deposit amount: "))

    if amount <= 0:
        print("Invalid amount!")
        return

    # Read all customer data
    if not os.path.exists(user_file):
        print(f"ERROR: File does not exist at: {user_file}")
        print("Please make sure you have registered customers first!")
        return

    with open(user_file, "r") as f:
        content = f.read().strip()

    if not content:
        print(f"ERROR: File is empty at: {user_file}")
        print("Please register customers first!")
        return

    # Parse customers
    customers = parse_customer_data(content)

    if not customers:
        print("ERROR: Could not parse customer data!")
        print("File content preview:")
        print(content[:200])
        return

    found = False

    # Find and update customer
    for customer in customers:
        if customer["account_number"] == acc:
            found = True
            current_balance = int(customer["balance"])
            new_balance = current_balance + amount
            customer["balance"] = str(new_balance)
            customer["last_logged_in"] = date.today().strftime("%Y-%m-%d")

            # Save updated data
            save_customer_data(customers)

            # Record transaction
            save_transaction(acc, "DEPOSIT", amount)

            print(f"\n✅ Deposited Rs. {amount} successfully!")
            print(f"New Balance: Rs. {new_balance}")
            break

    if not found:
        print(f"Account {acc} not found!")
        print(f"\nAvailable accounts:")
        for customer in customers:
            print(f"  - {customer['account_number']} ({customer['name']})")
    


def withdraw():
    """
    Withdraw money from customer account.
    """
    acc = input("Enter your account number: ")
    amount = int(input("Withdraw amount: "))

    if amount <= 0:
        print("Invalid amount!")
        return

    # Read all customer data
    if not os.path.exists(user_file):
        print(f"ERROR: File does not exist at: {user_file}")
        return

    with open(user_file, "r") as f:
        content = f.read().strip()

    if not content:
        print(f"ERROR: File is empty at: {user_file}")
        return

    # Parse customers
    customers = parse_customer_data(content)
    found = False

    # Find and update customer
    for customer in customers:
        if customer["account_number"] == acc:
            found = True
            current_balance = int(customer["balance"])

            if current_balance < amount:
                print("Insufficient balance!")
                return

            new_balance = current_balance - amount
            if new_balance < 500:
                print("Cannot withdraw! Minimum balance of Rs. 500 must be maintained.")
                return

            customer["balance"] = str(new_balance)
            customer["last_logged_in"] = date.today().strftime("%Y-%m-%d")

            # Save updated data
            save_customer_data(customers)

            # Record transaction
            save_transaction(acc, "WITHDRAW", amount)

            print(f"\nWithdrawn Rs. {amount} successfully!")
            print(f"New Balance: Rs. {new_balance}")
            clear_screen()
            break

    if not found:
        print(f"Account {acc} not found!")


def check_balance():
    """
    Check customer account balance.
    """
    acc = input("Enter your account number: ")

    # Read all customer data
    if not os.path.exists(user_file):
        print(f"ERROR: File does not exist at: {user_file}")
        return

    with open(user_file, "r") as f:
        content = f.read().strip()

    if not content:
        print(f"ERROR: File is empty at: {user_file}")
        return

    # Parse customers
    customers = parse_customer_data(content)
    found = False

    # Find customer
    for customer in customers:
        if customer["account_number"] == acc:
            found = True
            print(f"\n--- Account Details ---")
            print(f"Account Number: {customer['account_number']}")
            print(f"Name: {customer['name']}")
            print(f"Account Type: {customer['account_type']}")
            print(f"Balance: Rs. {customer['balance']}")
            break

    if not found:
        print(f"Account {acc} not found!")


def print_statement():
    """
    Print customer transaction statement.
    """
    acc = input("Enter your account number: ")

    # Find customer details
    customer_name = "Unknown"
    customer_balance = "0"

    if os.path.exists(user_file):
        with open(user_file, "r") as f:
            content = f.read().strip()
            customers = parse_customer_data(content)

            for customer in customers:
                if customer["account_number"] == acc:
                    customer_name = customer["name"]
                    customer_balance = customer["balance"]
                    break

    # Print statement header
    print("\n" + "=" * 80)
    print(f"TRANSACTION STATEMENT")
    print("=" * 80)
    print(f"Account Number: {acc}")
    print(f"Customer Name: {customer_name}")
    print(f"Current Balance: Rs. {customer_balance}")
    print("=" * 80)
    print(f"{'Date':<15} {'Type':<15} {'Amount':<15}")
    print("=" * 80)

    # Get transactions for this account
    transactions = parse_transactions(acc)

    total_dep = 0
    total_wd = 0

    for transaction in transactions:
        transaction_date = transaction["date"]
        transaction_type = transaction["type"]
        transaction_amount = transaction["amount"]

        print(
            f"{transaction_date:<15} {transaction_type:<15} Rs. {transaction_amount:<12}"
        )

        if transaction_type == "DEPOSIT":
            total_dep += int(transaction_amount)
        else:
            total_wd += int(transaction_amount)

    # Print footer
    print("=" * 80)
    print(f"Total Transactions: {len(transactions)}")
    print(f"Total Deposited: Rs. {total_dep}")
    print(f"Total Withdrawn: Rs. {total_wd}")
    print("=" * 80)
    clear_screen


def change_password():
    """
    Changing the  customer's password.
    """
    acc = input("Enter your account number: ")
    old_pw = input("Enter old password: ")
    new_pw = input("Enter new password: ")

    # Read all customer data
    if not os.path.exists(user_file):
        print(f"ERROR: File does not exist at: {user_file}")
        return

    with open(user_file, "r") as f:
        content = f.read().strip()

    if not content:
        print(f"ERROR: File is empty at: {user_file}")
        return

    # Parse customers
    customers = parse_customer_data(content)
    found = False

    # Find and update customer
    for customer in customers:
        if customer["account_number"] == acc:
            found = True

            if customer["password"] != old_pw:
                print("Incorrect old password!")
                return

            customer["password"] = new_pw

            # Save updated data
            save_customer_data(customers)

            print("\n Password changed successfully!")
            clear_screen()
            break

    if not found:
        print(f"Account {acc} not found!")


def user_menu():
    """
    Main user menu interface.
    """
    while True:
        print("\n========== USER MENU ==========")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Print Statement")
        print("5. Change Password")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            print_statement()
        elif choice == "5":
            change_password()
        elif choice == "6":
            print("User logged out.")
            break
        else:
            print("Invalid choice. Try again.")
