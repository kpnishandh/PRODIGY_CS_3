import re

def assess_password_strength(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."

    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."

    if not re.search(r'[0-9]', password):
        return "Password must contain at least one digit."

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special character."

    return "Your password is strong!"

# Example usage:
password = input("Enter a password: ")
print(assess_password_strength(password))
