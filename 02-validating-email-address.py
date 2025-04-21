import re

def is_valid_email(email):
    email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$"
    return re.match(email_pattern, email) is not None

print(is_valid_email("john.doe@example.com"))
print(is_valid_email("invalid_email"))