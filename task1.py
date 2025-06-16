from datetime import datetime

def get_days_from_today(date_str: str) -> int:
    """
    Calculate the number of days between a given date and the current date.

    Args:
        date_str (str): A date string in 'YYYY-MM-DD' format.

    Returns:
        int: The difference in days: positive if the given date is in the past,
             negative if it's in the future.

    Raises:
        ValueError: If date_str is not in the correct format.
    """
    try:
        given_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid format, use 'YYYY-MM-DD'")

    return (datetime.today() - given_date).days


if __name__ == "__main__":
    # Example usage
    print(get_days_from_today("2021-10-09"))
