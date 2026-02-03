# palindrome_products.py

from typing import Iterable, List, Optional, Tuple


def _is_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]


def _factor_pairs(value: int, min_factor: int, max_factor: int) -> List[List[int]]:
    """
    Return all factor pairs [a, b] such that:
      - a * b == value
      - min_factor <= a <= b <= max_factor
    """
    pairs: List[List[int]] = []

    # Only need to search a up to sqrt(value)
    a = min_factor
    while a * a <= value:
        if value % a == 0:
            b = value // a
            if min_factor <= b <= max_factor and a <= b:
                pairs.append([a, b])
        a += 1

    return pairs


def smallest(*, min_factor: int = 0, max_factor: int) -> Tuple[Optional[int], Iterable[Iterable[int]]]:
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    best_value: Optional[int] = None
    best_pairs: List[List[int]] = []

    # brute force ascending products implicitly by scanning i,j and tracking minimum palindrome
    for a in range(min_factor, max_factor + 1):
        for b in range(a, max_factor + 1):
            prod = a * b
            # If we already found a palindrome, skip products >= current best
            if best_value is not None and prod > best_value:
                break
            if _is_palindrome(prod):
                if best_value is None or prod < best_value:
                    best_value = prod
                    best_pairs = [[a, b]]
                elif prod == best_value:
                    best_pairs.append([a, b])

    if best_value is None:
        return None, []

    # Ensure we've got all pairs for that palindrome (sometimes multiple a,b hit it)
    # The loop above already collects them, but this guarantees correctness if logic changes.
    # Also removes any duplicates safely.
    all_pairs = _factor_pairs(best_value, min_factor, max_factor)
    # If best_pairs already correct, all_pairs will match; keep canonical all_pairs.
    return best_value, all_pairs


def largest(*, min_factor: int = 0, max_factor: int) -> Tuple[Optional[int], Iterable[Iterable[int]]]:
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    best_value: Optional[int] = None
    best_pairs: List[List[int]] = []

    # Search from high to low; for each a, b desc so we can prune quickly
    for a in range(max_factor, min_factor - 1, -1):
        for b in range(a, min_factor - 1, -1):
            prod = a * b
            # If we already found a palindrome, skip products <= current best
            if best_value is not None and prod < best_value:
                break
            if _is_palindrome(prod):
                if best_value is None or prod > best_value:
                    best_value = prod
                    best_pairs = [[b, a] if b <= a else [a, b]]
                elif prod == best_value:
                    pair = [b, a] if b <= a else [a, b]
                    best_pairs.append(pair)

    if best_value is None:
        return None, []

    # Collect all factor pairs for the palindrome within range
    return best_value, _factor_pairs(best_value, min_factor, max_factor)

