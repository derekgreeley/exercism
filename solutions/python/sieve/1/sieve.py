def primes(limit):
    """Return a list of all prime numbers less than or equal to `limit`."""
    if limit < 2:
        return []

    # Initialize a boolean array marking all numbers as potentially prime
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    # Sieve process: mark multiples of each prime
    for n in range(2, int(limit ** 0.5) + 1):
        if is_prime[n]:
            for multiple in range(n * n, limit + 1, n):
                is_prime[multiple] = False

    # Collect all primes
    return [i for i, prime in enumerate(is_prime) if prime]
