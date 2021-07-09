def is_armstrong_number(number):
    digits = str(number)
    armstrong = sum(int(digit) ** len(digits) for digit in digits)
    return armstrong == number
