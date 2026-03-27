# camicia.py

from collections import deque

PAYMENT = {"J": 1, "Q": 2, "K": 3, "A": 4}
NUMBER = "N"


def _normalize_card(card: str) -> str:
    return card if card in PAYMENT else NUMBER


def _loop_state(player_a: deque, player_b: deque, starter: int):
    return (
        tuple(_normalize_card(c) for c in player_a),
        tuple(_normalize_card(c) for c in player_b),
        starter,
    )


def simulate_game(player_a, player_b):
    a = deque(player_a)
    b = deque(player_b)

    total_cards = len(a) + len(b)
    cards_played = 0
    tricks = 0

    # Player A starts the first round.
    current = 0
    seen_round_starts = set()

    while True:
        state = _loop_state(a, b, current)
        if state in seen_round_starts:
            return {"status": "loop", "cards": cards_played, "tricks": tricks}
        seen_round_starts.add(state)

        pile = []
        penalty_due = 0
        last_payment_player = None

        while True:
            current_deck = a if current == 0 else b
            other = 1 - current

            # If the current player cannot play, the other player collects the pile.
            if not current_deck:
                collector = other
                if collector == 0:
                    a.extend(pile)
                else:
                    b.extend(pile)

                tricks += 1

                if len(a) == total_cards or len(b) == total_cards:
                    return {
                        "status": "finished",
                        "cards": cards_played,
                        "tricks": tricks,
                    }

                current = collector
                break

            card = current_deck.popleft()
            pile.append(card)
            cards_played += 1

            if card in PAYMENT:
                # A new payment card always hands the penalty to the opponent.
                penalty_due = PAYMENT[card]
                last_payment_player = current
                current = other
                continue

            if penalty_due > 0:
                # The same player keeps paying until the penalty is satisfied.
                penalty_due -= 1
                if penalty_due == 0:
                    collector = last_payment_player
                    if collector == 0:
                        a.extend(pile)
                    else:
                        b.extend(pile)

                    tricks += 1

                    if len(a) == total_cards or len(b) == total_cards:
                        return {
                            "status": "finished",
                            "cards": cards_played,
                            "tricks": tricks,
                        }

                    current = collector
                    break

                # Continue paying with the same player.
                continue

            # Ordinary play without penalty: switch turns.
            current = other