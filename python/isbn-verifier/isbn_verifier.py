import re


def is_valid(isbn: str) -> bool:
    if match := re.match(r"^(\d{9}[0-9X])$", isbn.replace('-', '')):
        isbn = list(match.group(1))
        if isbn[-1] == 'X':
            isbn[-1] = 10
        if sum(int(n)*(10-i) for i, n in enumerate(isbn)) % 11 == 0:
            return True
    return False
