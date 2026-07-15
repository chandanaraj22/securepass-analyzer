import re

def analyze_complexity(password):
    """
    Analyze password complexity based on character composition.
    Returns a dictionary containing individual checks.
    """

    result = {
        "length": len(password) >= 12,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digits": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    result["score"] = sum(result.values())

    return result