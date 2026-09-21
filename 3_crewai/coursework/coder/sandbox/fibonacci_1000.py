def fibonacci_terms(n: int):
    a, b = 1, 1
    terms = []
    for _ in range(n):
        terms.append(a)
        a, b = b, a + b
    return terms


if __name__ == "__main__":
    terms = fibonacci_terms(1000)
    print(",".join(map(str, terms)))
