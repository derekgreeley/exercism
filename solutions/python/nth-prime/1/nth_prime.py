# nth_prime.py

def prime(n):
    """Return the nth prime number."""
    if n < 1:
        raise ValueError("there is no zeroth prime")

    primes = []
    num = 2  # Start checking from the first prime

    while len(primes) < n:
        if _is_prime(num):
            primes.append(num)
        num += 1

    return primes[-1]


def _is_prime(num):
    """Helper function to check primality."""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    limit = int(num ** 0.5) + 1
    for i in range(3, limit, 2):
        if num % i == 0:
            return False
    return True
