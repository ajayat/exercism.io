import re


class PhoneNumber:
    PATTERN = (r"^ *(?:\+1|1)?[ \.]*"
               r"\(?([2-9]\d{2})\)?[ \.]*([2-9]\d{2})[- \.]*(\d{4}) *$")

    def __init__(self, number: str):
        if regex := re.match(self.PATTERN, number):
            self.number = ''.join(regex.groups())
            self.area_code, self._local, self._suscriber = regex.groups()
        else:
            raise ValueError(f"{number} is not a valid phone number")

    def pretty(self) -> str:
        return f"({self.area_code})-{self._local}-{self._suscriber}"
