COMMON_SEQUENCES = [
    "123456",
    "abcdef",
    "qwerty",
    "asdf",
    "password"
]

def detect_patterns(password):
    """
    Detect weak password patterns.
    """

    issues = []

    lower = password.lower()

    for seq in COMMON_SEQUENCES:
        if seq in lower:
            issues.append(f"Contains common sequence: {seq}")

    if len(set(password)) <= 2:
        issues.append("Too many repeated characters")

    return issues