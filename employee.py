
from validator import validate_employee


class Employee:
    """Represent a fully validated employee profile."""

    def __init__(self, employee_data):
        self.details = validate_employee(employee_data)

    @property
    def full_name(self):
        return (
            f"{self.details['first_name']} "
            f"{self.details['last_name']}"
        )

    def get_details(self):
        """Return a copy of validated employee information."""
        return self.details.copy()
