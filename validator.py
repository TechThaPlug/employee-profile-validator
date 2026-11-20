
import re
from datetime import date


def validate_name(name):
    """Validate an employee's first or last name."""
    if not isinstance(name, str):
        raise TypeError("Name must be text.")

    name = name.strip()

    if not name:
        raise ValueError("Name cannot be empty.")

    if len(name) < 2 or len(name) > 50:
        raise ValueError("Name must contain 2-50 characters.")

    if not re.fullmatch(r"[A-Za-z][A-Za-z '\-]*", name):
        raise ValueError("Name contains invalid characters.")

    return name.title()


def validate_email(email):
    """Validate and normalize an email address."""
    if not isinstance(email, str):
        raise TypeError("Email must be text.")

    email = email.strip().lower()

    pattern = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"

    if not re.fullmatch(pattern, email):
        raise ValueError("Please provide a valid email address.")

    return email


def validate_phone(phone):
    """Validate an international phone number."""
    if not isinstance(phone, str):
        raise TypeError("Phone number must be text.")

    phone = phone.strip()
    cleaned = re.sub(r"[\s().-]", "", phone)

    if not re.fullmatch(r"\+?[0-9]{7,15}", cleaned):
        raise ValueError("Phone number must contain 7-15 digits.")

    return cleaned


def validate_employee_id(employee_id):
    """Validate employee identification numbers."""
    if not isinstance(employee_id, str):
        raise TypeError("Employee ID must be text.")

    employee_id = employee_id.strip().upper()

    if not re.fullmatch(r"[A-Z0-9_-]{3,20}", employee_id):
        raise ValueError("Employee ID must contain 3-20 valid characters.")

    return employee_id


def validate_age(age):
    """Validate employee age."""
    if isinstance(age, bool) or not isinstance(age, int):
        raise TypeError("Age must be a whole number.")

    if not 18 <= age <= 100:
        raise ValueError("Employee age must be between 18 and 100.")

    return age


def validate_salary(salary):
    """Validate annual employee salary."""
    if isinstance(salary, bool) or not isinstance(salary, (int, float)):
        raise TypeError("Salary must be numeric.")

    if salary < 0 or salary > 1_000_000_000:
        raise ValueError("Salary is outside the accepted range.")

    return round(float(salary), 2)


def validate_department(department):
    """Validate an employee department."""
    if not isinstance(department, str):
        raise TypeError("Department must be text.")

    department = department.strip()

    if not department or len(department) > 60:
        raise ValueError("Department must contain 1-60 characters.")

    return department


def validate_job_title(job_title):
    """Validate an employee job title."""
    if not isinstance(job_title, str):
        raise TypeError("Job title must be text.")

    job_title = job_title.strip()

    if not job_title or len(job_title) > 80:
        raise ValueError("Job title must contain 1-80 characters.")

    return job_title


def validate_employment_date(value):
    """Validate an employment date in YYYY-MM-DD format."""
    if not isinstance(value, str):
        raise TypeError("Employment date must be text.")

    try:
        parsed_date = date.fromisoformat(value.strip())
    except ValueError:
        raise ValueError("Use the date format YYYY-MM-DD.")

    if parsed_date > date.today():
        raise ValueError("Employment date cannot be in the future.")

    return parsed_date.isoformat()


def validate_employee(data):
    """Validate a complete employee profile."""

    if not isinstance(data, dict):
        raise TypeError("Employee profile must be a dictionary.")

    required_fields = [
        "employee_id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "age",
        "salary",
        "department",
        "job_title",
        "employment_date",
    ]

    missing = [
        field for field in required_fields
        if field not in data
    ]

    if missing:
        raise ValueError(
            "Missing required fields: " + ", ".join(missing)
        )

    validated = {
        "employee_id": validate_employee_id(data["employee_id"]),
        "first_name": validate_name(data["first_name"]),
        "last_name": validate_name(data["last_name"]),
        "email": validate_email(data["email"]),
        "phone": validate_phone(data["phone"]),
        "age": validate_age(data["age"]),
        "salary": validate_salary(data["salary"]),
        "department": validate_department(data["department"]),
        "job_title": validate_job_title(data["job_title"]),
        "employment_date": validate_employment_date(
            data["employment_date"]
        ),
    }

    return validated
