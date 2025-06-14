# Woolf University. Python Programing Course. Homework – Working with Dates, Times, and Advanced String Manipulation

## Overview

This homework assignment consists of four independent tasks aimed at practicing Python's `datetime`, `random`, and `re` modules. The goal is to gain experience working with dates, time differences, string normalization, and basic logic implementation.

---

## Task 1 – Days Between Dates

### Description

Create a function `get_days_from_today(date)` that calculates the number of days between the given date and today.

### Requirements

* The function takes one parameter `date`: a string in the format `'YYYY-MM-DD'` (e.g., `'2020-10-09'`).
* Returns an integer representing the number of days from the given date to today. If the date is in the future, the result will be negative.
* Time (hours, minutes, seconds) is ignored — only days are considered.
* Use Python's `datetime` module.

### Implementation Tips

* Import the `datetime` module.
* Convert the input string to a `datetime` object.
* Use `datetime.today()` to get the current date.
* Calculate and return the difference in days as an integer.

### Evaluation Criteria

* Correctness: accurately calculates days between dates.
* Exception Handling: handles invalid date input formats.
* Readability: clean, well-documented code.

### Example

If today is May 5, 2021:

```python
get_days_from_today("2021-10-09")  # Output: -157
```

---

## Task 2 – Lottery Ticket Number Generator

### Description

Create a function `get_numbers_ticket(min, max, quantity)` to generate a set of unique random numbers for a lottery.

### Requirements

* Parameters:

  * `min`: minimum value (≥ 1)
  * `max`: maximum value (≤ 1000)
  * `quantity`: how many numbers to pick (must be within the `min` and `max` range)
* The function returns a **sorted list** of **unique** random numbers.
* If the parameters are invalid, return an empty list.

### Implementation Tips

* Validate input parameters.
* Use Python's `random` module.
* Use sets or other structures to ensure uniqueness.
* Sort and return the final list.

### Evaluation Criteria

* Validates input correctly.
* All returned numbers are unique.
* Returns a sorted list.
* Clean, documented code.

### Example

```python
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)
```

Sample Output:

```python
[4, 15, 23, 28, 37, 45]
```

---

## Task 3 – Phone Number Normalizer

### Description

Create a function `normalize_phone(phone_number)` that transforms phone numbers into a standard format suitable for SMS delivery.

### Requirements

* Accepts a string `phone_number` in various formats.
* Keeps only digits and optionally a leading `+`.
* Adds the country code `+38` (Ukraine) if it’s missing.
* Returns the normalized number as a string.

### Implementation Tips

* Use the `re` module (regular expressions) to remove unnecessary characters.
* Check for international code presence:

  * If starts with `380`, prepend `+`.
  * If no code, prepend `+38`.

### Evaluation Criteria

* Handles all common formats.
* Returns standardized, SMS-ready numbers.
* Uses regular expressions effectively.
* Clean and readable code.

### Example

```python
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS:", sanitized_numbers)
```

Output:

```python
['+380671234567', '+380952345678', '+380441234567', '+380501234567',
 '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']
```

---

## Task 4 – Upcoming Birthdays

### Description

Create a function `get_upcoming_birthdays(users)` to help identify coworkers who should be congratulated on their birthdays during the next 7 days (including today). If the birthday falls on a weekend, the greeting should be shifted to the next Monday.

### Requirements

* Input: list of dictionaries `users` where each dictionary has:

  * `name`: user’s name (string)
  * `birthday`: date string in format `'YYYY.MM.DD'`
* Returns: list of dictionaries with:

  * `name`: user’s name
  * `congratulation_date`: date string `'YYYY.MM.DD'` of when to congratulate

### Implementation Tips

* Convert birthday strings to `datetime` objects using `datetime.strptime(...).date()`.
* Use `datetime.today().date()` to get today’s date.
* Check if the birthday this year has passed — if so, consider next year.
* Adjust for weekends: if the birthday falls on a Saturday or Sunday, shift to Monday.
* Collect only users whose birthday is within the next 7 days.

### Evaluation Criteria

* Correct date range and weekend adjustments.
* Accurate output structure.
* Clean and maintainable code.

### Example

```python
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Birthdays this week:", upcoming_birthdays)
```

If today is `2024.01.22`, possible output:

```python
[
    {'name': 'John Doe', 'congratulation_date': '2024.01.23'},
    {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
]
```
