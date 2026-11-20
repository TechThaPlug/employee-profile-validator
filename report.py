
from validator import (
    validate_employee_id,
    validate_name,
    validate_email,
    validate_phone,
    validate_age,
    validate_salary,
    validate_department,
    validate_job_title,
    validate_employment_date,
)


FIELD_VALIDATORS = {
    "employee_id": validate_employee_id,
    "first_name": validate_name,
    "last_name": validate_name,
    "email": validate_email,
    "phone": validate_phone,
    "age": validate_age,
    "salary": validate_salary,
    "department": validate_department,
    "job_title": validate_job_title,
    "employment_date": validate_employment_date,
}


def validate_profile(data):
    """Validate every employee field and collect all errors."""

    if not isinstance(data, dict):
        raise TypeError("Employee profile must be a dictionary.")

    validated_data = {}
    errors = {}

    for field, validator in FIELD_VALIDATORS.items():
        if field not in data:
            errors[field] = "Required field is missing."
            continue

        try:
            validated_data[field] = validator(data[field])
        except (TypeError, ValueError) as error:
            errors[field] = str(error)

    return {
        "valid": not errors,
        "validated_data": validated_data,
        "errors": errors,
    }


def format_report(result):
    """Create a readable employee validation report."""

    lines = [
        "=" * 55,
        "       EMPLOYEE PROFILE VALIDATION REPORT",
        "=" * 55,
        "",
    ]

    validated_data = result["validated_data"]
    errors = result["errors"]

    for field in FIELD_VALIDATORS:
        if field in errors:
            lines.append(f"[FAIL] {field}: {errors[field]}")
        else:
            lines.append(f"[PASS] {field}: Valid")

    passed = len(validated_data)
    failed = len(errors)

    lines.extend([
        "",
        "-" * 55,
        f"Fields passed: {passed}",
        f"Fields failed: {failed}",
        "",
        (
            "FINAL RESULT: VALID"
            if result["valid"]
            else "FINAL RESULT: INVALID"
        ),
        "=" * 55,
    ])

    return "\n".join(lines)
