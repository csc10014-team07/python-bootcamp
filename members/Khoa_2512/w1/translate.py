"""Generate all prime numbers less than n."""


def primes_up_to_n(n: int) -> list[int]:
    """Return a list of prime numbers less than n.

    Args:
        n: The exclusive upper limit for finding prime numbers.

    Returns:
        A list of prime integers smaller than n.
    """
    not_prime: list[int] = []
    primes: list[int] = []

    for x in range(2, n):
        if x in not_prime:
            continue
        primes.append(x)
        count = 2
        while count * x < n:
            not_prime.append(count * x)
            count += 1

    return primes


print(primes_up_to_n(100))

"""In C++, the return type is a vector; in Python, it is a list."""

