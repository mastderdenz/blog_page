import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

def is_valid_password(password):
    # Define password criteria using regular expressions
    # At least one uppercase letter, one lowercase letter, one digit, one special character
    # Minimum length of 8 characters
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

    if pattern.match(password):
        return True
    else:
        return False
