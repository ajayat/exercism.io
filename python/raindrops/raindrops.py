def convert(number: int) -> str:
    return ''.join(
        d for d, f in (("Pling", 3), ("Plang", 5), ("Plong", 7))
        if number % f == 0
    ) or str(number)
