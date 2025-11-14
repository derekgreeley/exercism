"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card."""
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value."""
    value_one, value_two = value_of_card(card_one), value_of_card(card_two)
    if value_one == value_two:
        return card_one, card_two
    return card_one if value_one > value_two else card_two


def value_of_ace(card_one, card_two):
    """Determine the value of an ace."""
    if 'A' in [card_one, card_two]:
        return 1
    return 11 if value_of_card(card_one) + value_of_card(card_two) <= 10 else 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a blackjack."""
    ten_cards = ['10', 'J', 'Q', 'K']
    return (card_one == 'A' and card_two in ten_cards) or (card_two == 'A' and card_one in ten_cards)


def can_split_pairs(card_one, card_two):
    """Determine if the hand can be split into pairs."""
    return card_one == card_two or (card_one in ['J', 'Q', 'K'] and card_two in ['J', 'Q', 'K'])


def can_double_down(card_one, card_two):
    """Determine if the hand can be doubled down."""
    return value_of_card(card_one) + value_of_card(card_two) in [9, 10, 11]