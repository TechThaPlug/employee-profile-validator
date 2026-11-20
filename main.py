
from employee import Employee
from report import validate_profile, format_report


def collect_employee_data():
    """Collect employee information from the user."""

    print("\nEMPLOYEE PROFILE VALIDATOR")
    print("=" * 40)

    data = {}

    data["employee_id"] = input("Employee ID: ")
    data["first_name"] = input("First name: ")
    data["last_name"] = input("Last name: ")
    data["email"] = input("Email address: ")
    data["phone"] = input("Phone number: ")

    age = input("Age: ")
    try:
        data["age"] = int(age)
    except ValueError:
        data["age"] = age

    salary = input("Annual salary: ")
    try:
        data["salary"] = float(salary)
    except ValueError:
        data["salary"] = salary

    data["department"] = input("Department: ")
    data["job_title"] = input("Job title: ")
    data["employment_date"] = input(
        "Employment date (YYYY-MM-DD): "
    )

    return data


def main():
    """Run the employee profile validation application."""

    employee_data = collect_employee_data()

    result = validate_profile(employee_data)

    print("\n")
    print(format_report(result))

    if result["valid"]:
        employee = Employee(result["validated_data"])

        print("\nEMPLOYEE PROFILE")
        print("-" * 40)
        print(f"Full name: {employee.full_name}")
        print(f"Employee ID: {employee.details['employee_id']}")
        print(f"Email: {employee.details['email']}")
        print(f"Department: {employee.details['department']}")
        print(f"Job title: {employee.details['job_title']}")

        print("\nEmployee profile validated successfully!")
    else:
        print("\nPlease correct the errors and try again.")


if __name__ == "__main__":
    main()
