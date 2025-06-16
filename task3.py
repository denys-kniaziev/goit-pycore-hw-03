import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalize phone numbers by stripping unwanted characters
    and ensuring Ukrainian international format (+38...) if no '+' prefix.

    Args:
        phone_number (str): Raw phone string.

    Returns:
        str: Normalized phone number.
    """
    # Remove all characters except digits and '+'
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())

    if cleaned.startswith("+"):
        return cleaned
    if cleaned.startswith("380"):
        return "+" + cleaned
    return "+38" + cleaned

if __name__ == "__main__":
    # Example usage
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   "       
    ]

    normalized = [normalize_phone(n) for n in raw_numbers]
    print("Normalized for SMS:", normalized)
