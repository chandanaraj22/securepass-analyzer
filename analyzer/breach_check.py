from pathlib import Path

DATASET = Path("datasets/common_passwords.txt")

with open(DATASET, "r") as f:
    BREACHED = set(line.strip().lower() for line in f)

def is_breached(password):
    return password.lower() in BREACHED
