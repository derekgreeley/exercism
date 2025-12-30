from collections import Counter
from typing import List, Tuple

RANKS = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14,
}


def best_hands(hands: List[str]) -> List[str]:
    scored = [(hand_score(h), h) for h in hands]
    best = max(sc for sc, _ in scored)
    return [h for sc, h in scored if sc == best]


def hand_score(hand: str) -> Tuple[int, Tuple[int, ...]]:
    ranks, suits = parse_hand(hand)

    is_flush = len(set(suits)) == 1
    straight_high = straight_high_card(ranks)  # None if not straight
    counts = Counter(ranks)

    # Sort ranks by (count desc, rank desc) for many tie-break rules
    # Example: [A,A,A,9,9] -> [(3,A),(2,9)]
    groups = sorted(((cnt, r) for r, cnt in counts.items()), reverse=True)

    # Straight flush
    if is_flush and straight_high is not None:
        return (8, (straight_high,))

    # Four of a kind
    if groups[0][0] == 4:
        quad = groups[0][1]
        kicker = max(r for r in ranks if r != quad)
        return (7, (quad, kicker))

    # Full house
    if groups[0][0] == 3 and groups[1][0] == 2:
        trip = groups[0][1]
        pair = groups[1][1]
        return (6, (trip, pair))

    # Flush
    if is_flush:
        return (5, tuple(sorted(ranks, reverse=True)))

    # Straight
    if straight_high is not None:
        return (4, (straight_high,))

    # Three of a kind
    if groups[0][0] == 3:
        trip = groups[0][1]
        kickers = sorted((r for r in ranks if r != trip), reverse=True)
        return (3, (trip, *kickers))

    # Two pair
    if groups[0][0] == 2 and groups[1][0] == 2:
        high_pair = max(groups[0][1], groups[1][1])
        low_pair = min(groups[0][1], groups[1][1])
        kicker = max(r for r in ranks if r not in (high_pair, low_pair))
        return (2, (high_pair, low_pair, kicker))

    # One pair
    if groups[0][0] == 2:
        pair = groups[0][1]
        kickers = sorted((r for r in ranks if r != pair), reverse=True)
        return (1, (pair, *kickers))

    # High card
    return (0, tuple(sorted(ranks, reverse=True)))


def parse_hand(hand: str) -> Tuple[List[int], List[str]]:
    cards = hand.split()
    ranks = []
    suits = []
    for card in cards:
        suit = card[-1]
        rank_str = card[:-1]
        ranks.append(RANKS[rank_str])
        suits.append(suit)
    return ranks, suits


def straight_high_card(ranks: List[int]) -> int | None:
    uniq = sorted(set(ranks))
    if len(uniq) != 5:
        return None

    # Normal straight
    if uniq[-1] - uniq[0] == 4 and all(uniq[i] + 1 == uniq[i + 1] for i in range(4)):
        return uniq[-1]

    # Ace-low straight (A,2,3,4,5) treated as 5-high
    if uniq == [2, 3, 4, 5, 14]:
        return 5

    return None
