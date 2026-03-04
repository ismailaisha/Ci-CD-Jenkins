def password_errors(password: str) -> list[str]:
    errors = []

    if len(password) < 8:
        errors.append("too_short")

    if " " in password:
        errors.append("contains_space")

    has_letter = any(ch.isalpha() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_symbol = any((not ch.isalnum()) and (ch != " ") for ch in password)

    if not has_letter:
        errors.append("no_letter")

    if not has_digit:
        errors.append("no_digit")

    return errors


def check_password(password: str) -> str:
    errors = password_errors(password)
    if errors:
        return "weak"

    has_symbol = any((not ch.isalnum()) and (ch != " ") for ch in password)
    return "strong" if has_symbol else "medium"


if __name__ == "__main__":
    samples = ["1234567", "password1", "Password1", "Password1!", "pass word1!"]
    for s in samples:
        print(s, "->", check_password(s), password_errors(s))