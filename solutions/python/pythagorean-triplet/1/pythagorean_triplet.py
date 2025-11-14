from math import gcd, isqrt

def triplets_with_sum(N: int) -> list[list[int]]:
    """
    Return all Pythagorean triplets [a, b, c] with a < b < c and a + b + c = N.
    Uses Euclid's formula:
        a = k*(m^2 - n^2), b = k*(2mn), c = k*(m^2 + n^2)
        a + b + c = k * 2*m*(m + n) = N
    where m > n >= 1, gcd(m, n) = 1, and m-n is odd.
    """
    if N < 3:
        return []

    results = []

    # From 2*m*(m+n) <= N  -> m^2 + m*n <= N/2 -> m <= sqrt(N/2) is a safe bound
    # We'll use a slightly looser but simple bound:
    sm = N // 2
    m_max = isqrt(sm) + 1

    for m in range(2, m_max + 1):
        for n in range(1, m):
            if (m - n) % 2 == 0:   # must be opposite parity
                continue
            if gcd(m, n) != 1:     # must be coprime
                continue

            denom = 2 * m * (m + n)
            if N % denom != 0:
                continue

            k = N // denom
            a = k * (m*m - n*n)
            b = k * (2*m*n)
            c = k * (m*m + n*n)

            # ensure ascending order a < b < c
            trip = sorted([a, b, c])
            if trip[0] + trip[1] > trip[2]:  # (always true for Pythagorean, just defensive)
                results.append(trip)

    # Remove duplicates if any (shouldn't happen, but safe)
    # and return as a list of lists
    unique = {tuple(t) for t in results}
    return [list(t) for t in unique]