from decimal import Decimal, getcontext


def calculate_pi_terms(num_terms: int) -> Decimal:
    """Calculate 4 times the first num_terms of the Leibniz series."""
    getcontext().prec = 30
    total = Decimal(0)
    sign = 1

    for i in range(num_terms):
        denominator = Decimal(2 * i + 1)
        term = Decimal(sign) / denominator
        total += term
        sign *= -1

    return total * 4


if __name__ == "__main__":
    result = calculate_pi_terms(1_000_000)
    print(result)
