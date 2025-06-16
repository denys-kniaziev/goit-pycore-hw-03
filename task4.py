from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Determine which users have birthdays within the next 7 days (inclusive),
    shifting weekend birthdays to the next Monday.

    Args:
        users (list[dict]): List of dicts with 'name' and 'birthday' keys.
            'birthday' is a string in 'YYYY.MM.DD' format.

    Returns:
        list of dict: Each dict has:
            - 'name': user's name
            - 'congratulation_date': date string 'YYYY.MM.DD' to send greetings.
    """
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    results = []

    for user in users:
        name = user.get('name')
        
        # parse birthday and replace year with this year
        bday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        bday_current = bday.replace(year=today.year)

        # if already passed this year, use next year
        if bday_current < today:
            bday_current = bday_current.replace(year=today.year + 1)

        # if within next 7 days
        if today <= bday_current <= end_date:
            congratulation_date = bday_current

            # shift weekends to Monday
            if bday_current.weekday() >= 5:
                days_to_next_monday = 7 - bday_current.weekday()
                congratulation_date += timedelta(days=days_to_next_monday)

            results.append({
                'name': name,
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })

    # sort by date
    results.sort(key=lambda x: x['congratulation_date'])
    return results

if __name__ == '__main__':
    # Example usage
    sample_users = [
        {'name': 'John Doe', 'birthday': '1985.01.23'},
        {'name': 'Jane Smith', 'birthday': '1990.06.19'},
        {'name': 'Bob Brown', 'birthday': '1992.06.21'}
    ]
    print(get_upcoming_birthdays(sample_users))