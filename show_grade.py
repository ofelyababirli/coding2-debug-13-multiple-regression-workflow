"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "ed2ca28d3bd1ff22030284b4db353d0f"
GRADE_HASH = "b1b2dd187161bac8b10dab649366e4d4ae09806632117feee241cbcc7f78d70b"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
