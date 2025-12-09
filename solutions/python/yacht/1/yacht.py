# yacht.py
from collections import Counter

# Category constants (values themselves don't matter, only identity)
YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full_house"
FOUR_OF_A_KIND = "four_of_a_kind"
LITTLE_STRAIGHT = "little_straight"
BIG_STRAIGHT = "big_straight"
CHOICE = "choice"


def score(dice, category):
    counts = Counter(dice)

    if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        face_value = {
            ONES: 1,
            TWOS: 2,
            THREES: 3,
            FOURS: 4,
            FIVES: 5,
            SIXES: 6,
        }[category]
        return face_value * counts[face_value]

    if category == YACHT:
        return 50 if len(counts) == 1 else 0

    if category == FULL_HOUSE:
        # Need exactly a 3-of-a-kind and a 2-of-a-kind, not five of a kind
        values = sorted(counts.values())
        return sum(dice) if values == [2, 3] else 0

    if category == FOUR_OF_A_KIND:
        # At least four of the same value; Yacht counts as four of a kind too
        for face, cnt in counts.items():
            if cnt >= 4:
                return face * 4
        return 0

    if category == LITTLE_STRAIGHT:
        return 30 if set(dice) == {1, 2, 3, 4, 5} else 0

    if category == BIG_STRAIGHT:
        return 30 if set(dice) == {2, 3, 4, 5, 6} else 0

    if category == CHOICE:
        return sum(dice)

    # If somehow an unknown category is passed (not expected in the tests)
    return 0
