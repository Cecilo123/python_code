def is_leap_year(year):
    """
    Determines whether a given year is a leap year or not.

    A leap year is either:
    - Divisible by 4 but not by 100, OR
    - Divisible by 400

    Args:
        year: An integer representing the year to check.

    Returns:
        True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year.")
