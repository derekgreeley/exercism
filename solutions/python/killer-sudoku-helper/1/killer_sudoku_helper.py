# killer_sudoku_helper.py
from itertools import combinations as combs


def combinations(cage_sum: int, cage_size: int, excluded: list[int]) -> list[list[int]]:
    excluded_set = set(excluded)

    # digits are 1..9, no repeats in a cage
    available = [d for d in range(1, 10) if d not in excluded_set]

    results: list[list[int]] = []
    for tup in combs(available, cage_size):
        if sum(tup) == cage_sum:
            results.append(list(tup))

    # itertools.combinations yields tuples in sorted order; we also return results sorted
    return results
