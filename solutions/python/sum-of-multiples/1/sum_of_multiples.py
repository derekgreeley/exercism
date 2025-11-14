def sum_of_multiples(limit: int, factors: list[int]) -> int:
    """
    Return the sum of all unique multiples of the given factors that are less than `limit`.

    Rules:
      - Consider multiples of each factor strictly less than `limit`.
      - Combine and deduplicate all multiples across factors.
      - Factor 0 contributes nothing (its only multiple is 0).
      - Empty factor list yields 0.

    Assumptions (per problem statement):
      - limit is a non-negative int.
      - factors is a list of unique, sorted non-negative ints.
    """
    if not factors:
        return 0

    multiples = set()
    for f in factors:
        if f == 0:
            # The only multiple is 0; it doesn't change the sum.
            continue
        multiples.update(range(f, limit, f))

    return sum(multiples)