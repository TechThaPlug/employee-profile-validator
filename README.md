# Employee Profile Validator

A Python command-line application that validates employee profile information, identifies invalid fields, and generates detailed validation reports.

## Features

- Employee ID validation
- First and last name validation
- Email address validation
- International phone number validation
- Age validation
- Salary validation
- Department validation
- Job title validation
- Employment date validation
- Detailed field-by-field validation reports
- Input normalization and error handling
- Automated unit tests

## Project Structure

```text
employee-profile-validator/
├── tests/
│   └── test_validator.py
├── validation_reports/
│   └── .gitkeep
├── main.py
├── employee.py
├── validator.py
├── report.py
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3.13 or later
- Visual Studio Code (recommended)

This project uses Python's standard library. No third-party packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/TechThaPlug/employee-profile-validator.git
```

Enter the project directory:

```bash
cd employee-profile-validator
```

Create a virtual environment:

```bash
py -3.13 -m venv .venv
```

Activate it on Windows:

```cmd
.venv\Scripts\activate
```

## Run the Application

```bash
python main.py
```

Follow the prompts to enter employee information.

The application validates all required fields and displays a report showing which fields passed or failed.

## Run Automated Tests

```bash
python -m unittest discover -s tests -v
```

## Example Validation Report

```text
=======================================================
       EMPLOYEE PROFILE VALIDATION REPORT
=======================================================

[PASS] employee_id: Valid
[PASS] first_name: Valid
[PASS] last_name: Valid
[PASS] email: Valid
[PASS] phone: Valid
[PASS] age: Valid
[PASS] salary: Valid
[PASS] department: Valid
[PASS] job_title: Valid
[PASS] employment_date: Valid

Fields passed: 10
Fields failed: 0

FINAL RESULT: VALID
=======================================================
```

## Security and Privacy

- Input is validated before an employee object is created.
- Invalid values are rejected with descriptive error messages.
- Generated validation reports are excluded from Git.
- Virtual environments and local environment files are excluded from Git.
- Employee information should be handled according to applicable privacy and data-protection requirements.

## Technology Stack

- Python
- Regular Expressions
- Object-Oriented Programming
- Python unittest
- Command-Line Interface

## Author

**Anthony W. Maina**

GitHub: [TechThaPlug](https://github.com/TechThaPlug)

Portfolio: [TechThaPlug](https://techthaplug.github.io/)

## License

This project is licensed under the MIT License.
