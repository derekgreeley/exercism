# largest_series_product.py

from functools import reduce
from operator import mul

def largest_product(digits: str, span: int) -> int:
    # Validation
    if span < 0:
        raise ValueError("span must not be negative")
    if span > len(digits):
        raise ValueError("span must not exceed string length")
    if any(ch for ch in digits if not ch.isdigit()):
        raise ValueError("digits input must only contain digits")

    # Edge cases
    if span == 0:
        # Product of zero numbers is the multiplicative identity (1)
        return 1
    if span == 0 and digits == "":
        return 1
    if digits == "":
        # Covered above by span > len(digits) when span != 0, but keep for clarity
        return 0

    # Optimization: any window containing '0' has product 0,
    # so split the string on zeros and process only zero-free chunks.
    best = 0
    for block in digits.split('0'):
        if len(block) < span:
            continue
        # Convert once per block
        nums = list(map(int, block))
        # Compute initial window product
        prod = reduce(mul, nums[0:span], 1)
        best = max(best, prod)

        # Slide the window; since all digits in block are non-zero,
        # we can update product in O(1) by division and multiplication.
        for i in range(span, len(nums)):
            out = nums[i - span]
            inn = nums[i]
            prod = (prod // out) * inn
            if prod > best:
                best = prod

    return best
