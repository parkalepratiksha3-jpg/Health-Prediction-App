
import re
from datetime import datetime, date


def validate_patient(full_name, dob, email, glucose, haemoglobin, cholesterol):

    if not full_name.strip():
        return False, "Full Name is required."

    try:
        birth_date = datetime.strptime(dob, "%d.%m.%Y").date()

        if birth_date > date.today():
            return False, "Date of Birth cannot be in the future."

    except ValueError:
        return False, "Invalid DOB. Use DD.MM.YYYY format and enter a valid date."

    if not re.match(r"^[\w.+-]+@[\w-]+\.[\w.-]+$", email):
        return False, "Please enter a valid email address."

    try:
        values = [float(glucose), float(haemoglobin), float(cholesterol)]

        if any(value <= 0 for value in values):
            return False, "Blood values must be greater than zero."

    except (ValueError, TypeError):
        return False, "Glucose, Haemoglobin and Cholesterol must be numeric."

    return True, "Validation successful."

