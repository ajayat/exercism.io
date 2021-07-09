def leap_year(year) -> bool:
    if year % 4 or year % 100 == 0 and year % 400:
        return False
    return True
