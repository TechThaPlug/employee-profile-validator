
import unittest
from datetime import date, timedelta

from validator import (
    validate_name,
    validate_email,
    validate_phone,
    validate_employee_id,
    validate_age,
    validate_salary,
    validate_department,
    validate_job_title,
    validate_employment_date,
    validate_employee,
)

from report import validate_profile


class TestEmployeeValidator(unittest.TestCase):

    def test_valid_name(self):
        self.assertEqual(validate_name("alice"), "Alice")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            validate_name("A")

    def test_valid_email(self):
        self.assertEqual(
            validate_email("ALICE@example.com"),
            "alice@example.com"
        )

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            validate_email("invalid-email")

    def test_valid_phone(self):
        self.assertEqual(
            validate_phone("+254 712 345 678"),
            "+254712345678"
        )

    def test_invalid_phone(self):
        with self.assertRaises(ValueError):
            validate_phone("123")

    def test_valid_employee_id(self):
        self.assertEqual(
            validate_employee_id("emp001"),
            "EMP001"
        )

    def test_invalid_employee_id(self):
        with self.assertRaises(ValueError):
            validate_employee_id("A!")

    def test_valid_age(self):
        self.assertEqual(validate_age(28), 28)

    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            validate_age(15)

    def test_age_rejects_boolean(self):
        with self.assertRaises(TypeError):
            validate_age(True)

    def test_valid_salary(self):
        self.assertEqual(validate_salary(75000), 75000.0)

    def test_invalid_salary(self):
        with self.assertRaises(ValueError):
            validate_salary(-100)

    def test_valid_department(self):
        self.assertEqual(
            validate_department(" Engineering "),
            "Engineering"
        )

    def test_invalid_department(self):
        with self.assertRaises(ValueError):
            validate_department("")

    def test_valid_job_title(self):
        self.assertEqual(
            validate_job_title("Software Developer"),
            "Software Developer"
        )

    def test_invalid_job_title(self):
        with self.assertRaises(ValueError):
            validate_job_title("")

    def test_valid_employment_date(self):
        self.assertEqual(
            validate_employment_date("2024-01-15"),
            "2024-01-15"
        )

    def test_future_employment_date(self):
        future_date = (date.today() + timedelta(days=1)).isoformat()

        with self.assertRaises(ValueError):
            validate_employment_date(future_date)

    def test_complete_employee_profile(self):
        employee = {
            "employee_id": "EMP001",
            "first_name": "Alice",
            "last_name": "Johnson",
            "email": "alice@example.com",
            "phone": "+254712345678",
            "age": 28,
            "salary": 75000,
            "department": "Engineering",
            "job_title": "Software Developer",
            "employment_date": "2024-01-15",
        }

        result = validate_employee(employee)

        self.assertEqual(result["employee_id"], "EMP001")
        self.assertEqual(result["email"], "alice@example.com")

    def test_missing_employee_field(self):
        with self.assertRaises(ValueError):
            validate_employee({})

    def test_validation_report_detects_errors(self):
        employee = {
            "employee_id": "EMP001",
            "first_name": "Alice",
            "last_name": "Johnson",
            "email": "invalid-email",
            "phone": "123",
            "age": 28,
            "salary": 75000,
            "department": "Engineering",
            "job_title": "Developer",
            "employment_date": "2024-01-15",
        }

        result = validate_profile(employee)

        self.assertFalse(result["valid"])
        self.assertIn("email", result["errors"])
        self.assertIn("phone", result["errors"])


if __name__ == "__main__":
    unittest.main()
