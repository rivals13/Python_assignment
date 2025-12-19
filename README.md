# Banking Management System
A comprehensive CLI-based banking application built in Python that simulates a complete banking system with multiple user roles and secure authentication.

## 📋 Table of Contents

- [Features](#features)
- [User Roles](#user-roles)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Team Members](#team-members)
- [Contributing](#contributing)

## ✨ Features

### 🔐 Authentication & Security
- Secure login system with email and password validation
- Multiple login attempts with lockout protection
- Role-based access control (Admin, Staff, Customer)

### 👨‍💼 Admin Features
- Create and manage staff accounts
- View all staff and customer details
- Print formatted customer records
- Search records by ID or email
- Update/delete staff information

### 👨‍💼 Staff Features
- Register new customers
- Update customer information
- View customer details
- Manage customer accounts

### 👤 Customer Features
- Secure account access
- Balance inquiry
- Deposit and withdrawal operations
- Transaction history
- Password management
- Account statements

### 🛡️ Data Validation
- Comprehensive input validation for all fields
- Email format validation
- Age restrictions (18-59 years)
- Duplicate prevention
- Strong password requirements

## 👥 User Roles

### Administrator
- **Username Format**: admin@domain.com
- **Password Format**: LBEF-adXXXXXX
- **Permissions**: Full system access, staff management

### Staff Member
- **Username Format**: staff@domain.com
- **Password Format**: LBEF-stfXXXXXX
- **Permissions**: Customer management, account operations

### Customer
- **Username Format**: customer@domain.com
- **Password Format**: LBEF-usrXXXXXX
- **Permissions**: Personal account management

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only standard library)

### Setup Instructions

1. **Clone or Download the Project**
   ```bash
   git clone <repository-url>
   cd Python_group_project_LBEF
   ```

2. **Ensure Python is Installed**
   ```bash
   python3 --version
   ```

3. **Run the Application**
   ```bash
   python3 Project.py
   ```

## 📖 Usage

### Starting the Application
Run the main file to start the banking system:
```bash
python3 Project.py
```

### Login Process
1. Choose your user type (1-Admin, 2-Staff, 3-Customer)
2. Enter valid email and password
3. Access role-specific menu options

### Example Workflow
```
Welcome to the banking management system
============================================================
Group details:
TEAM-6
Satyaraj joshi(NP070996)
Rajkumar Tiruwa(NP070980)
Sansar chhetri(NP070995)
============================================================

select one option
------------------------------------------------------------
1 |Admin login 👨🏻‍💻|
2 |Staff Login 👨🏻‍💼|
3 |user Login 👨🏻‍💼|

current status: (Not logged in)
------------------------------------------------------------
enter the choice(integers only): 1
```

## 📁 Project Structure

```
Python_group_project_LBEF/
│
├── Project.py                    # Main entry point
├── sample_test.py               # Test/demo script
├── README.md                    # Project documentation
│
├── functions/                   # Core functionality modules
│   ├── admin_feature.py         # Admin operations
│   ├── admin_feature_validation.py  # Staff validation
│   ├── staff_feature.py         # Staff operations
│   ├── user_details_validation.py   # Customer validation
│   ├── customer_features.py     # Customer operations
│   ├── logins.py                # Authentication system
│   ├── password_checker.py      # Password validation
│   ├── initial_login_mail_checker.py  # Email validation
│   └── cli_utils.py             # CLI utilities
│
└── cred_files/                  # Data storage (text files)
    ├── admin.txt                # Admin credentials
    ├── staff.txt                # Staff data
    ├── user.txt                 # Customer data
    └── transaction.txt          # Transaction records
```

## 🛠️ Technologies Used

- **Language**: Python 3.7+
- **Data Storage**: Text files (.txt)
- **Interface**: Command Line Interface (CLI)
- **Authentication**: Custom validation system
- **Date/Time**: Python datetime module
- **Random Generation**: Python random module

## 👨‍💻 Team Members

- **Satyaraj Joshi** (NP070996)
- **Rajkumar Tiruwa** (NP070980)
- **Sansar Chhetri** (NP070995)


## 📝 Notes

- All data is stored in plain text files for simplicity
- Passwords are stored in hashed format for security
- The system includes comprehensive error handling and validation
- Age validation ensures users are between 18-59 years old
- Email validation supports common TLDs (.com, .org, .net, .edu, .info)



**Python Version**: 3.7+
**Last Updated**: 19 December 2025
