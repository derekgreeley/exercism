from functools import lru_cache
from collections import Counter
from itertools import combinations

# Price per single book in cents
BOOK_PRICE = 800

# Discount factors as integer percentages to stay in integer arithmetic
DISCOUNT_PERCENT = {
    1: 100,  # 0%
    2: 95,   # 5%
    3: 90,   # 10%
    4: 80,   # 20%
    5: 75,   # 25%
}


def total(basket):
    """
    Compute the minimal total price (in cents) for the given basket of books
    from a 5-title series, maximizing discount.

    basket: list of ints in 1..5, titles may repeat.
    returns: int (cents)
    """
    if not basket:
        return 0

    # Count how many copies of each of the 5 titles we have, keep a fixed order by title id
    counts_by_title = [0] * 5
    c = Counter(basket)
    for title in range(1, 6):
        counts_by_title[title - 1] = c.get(title, 0)

    counts = tuple(counts_by_title)

    @lru_cache(maxsize=None)
    def best_price(state):
        # state is a 5-tuple of remaining copies per title
        if sum(state) == 0:
            return 0

        # indices of titles that still have copies left
        available = [i for i, cnt in enumerate(state) if cnt > 0]

        best = float("inf")

        # Try all possible bundle sizes 1..min(5, len(available))
        for size in range(1, min(5, len(available)) + 1):
            for idxs in combinations(available, size):
                # Build the next state by removing one copy of each chosen distinct title
                nxt = list(state)
                for i in idxs:
                    nxt[i] -= 1
                nxt = tuple(nxt)

                # Price for this bundle (size books with discount), in cents
                bundle_price = size * BOOK_PRICE * DISCOUNT_PERCENT[size] // 100

                # Total price = this bundle + best of the remainder
                cand = bundle_price + best_price(nxt)
                if cand < best:
                    best = cand

        return best

    return best_price(counts)
