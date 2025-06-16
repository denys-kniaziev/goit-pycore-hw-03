import random

def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list[int]:
    """
    Generate a sorted list of unique random numbers within a given range.

    Args:
        min_value (int): Minimum possible number (>= 1).
        max_value (int): Maximum possible number (<= 1000).
        quantity (int): How many numbers to pick.

    Returns:
        list[int]: Sorted unique random numbers if inputs are valid;
                   otherwise, an empty list.
    """
    # Validate inputs
    if min_value < 1 or max_value > 1000 or quantity < 1:
        return []
    if min_value > max_value or quantity > (max_value - min_value + 1):
        return []

    # Use random.sample to get unique numbers, then sort
    numbers = random.sample(range(min_value, max_value + 1), quantity)
    return sorted(numbers)

if __name__ == "__main__":
    # Example: pick 6 numbers from 1 to 49
    ticket = get_numbers_ticket(1, 49, 6)
    print("Your lottery numbers:", ticket)
