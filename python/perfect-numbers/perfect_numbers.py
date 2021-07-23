def divisors(n: int) -> set:
    """ Returns all divisors of n """
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        q, r = divmod(n, i)
        if r == 0:
            divisors |= {i, q}
    return divisors


def classify(number: int) -> str:
    if number <= 0:
        raise ValueError("Number must be positive")
    aliquot_sum = sum(divisors(number)) - number
    if aliquot_sum < number:
        return "deficient"
    elif aliquot_sum == number:
        return "perfect"
    else:
        return "abundant"
