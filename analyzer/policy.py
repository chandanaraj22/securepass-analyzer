def check_policy(password):
    """
    Enterprise password policy validation.
    """

    policy = {
        "Minimum Length (12)": len(password) >= 12,
        "Uppercase": any(c.isupper() for c in password),
        "Lowercase": any(c.islower() for c in password),
        "Digit": any(c.isdigit() for c in password),
        "Special Character": any(not c.isalnum() for c in password)
    }

    return policy