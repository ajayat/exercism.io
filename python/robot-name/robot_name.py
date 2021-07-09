from random import choices
from string import ascii_uppercase, digits


class Robot:
    def __init__(self):
        self.name = None
        self._names = set()
        self.reset()

    def _generate_name(self) -> str:
        return "".join(choices(ascii_uppercase, k=2) + choices(digits, k=3))

    def reset(self) -> None:
        while (name := self._generate_name()) in self._names:
            pass
        self._names.discard(self.name)
        self._names.add(name)
        self.name = name
