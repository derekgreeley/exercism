"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else: return int(card)



def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return card_one, card_two
        


def value_of_ace(card_one, card_two):
    # If any card is an Ace, return 1 for the new Ace
    if card_one == 'A' or card_two == 'A':
        return 1
    
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    # Calculate the current hand value
    current_hand_value = value_one + value_two
    
    # If the current hand value + 11 is 21 or less, the ace should be 11
    if current_hand_value + 11 <= 21:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    ten_cards = ['10', 'J', 'Q', 'K']
    return (card_one == 'A' and card_two in ten_cards) or (card_two == 'A' and card_one in ten_cards)


def can_split_pairs(card_one, card_two):
    # Both cards are face cards and considered as 10 for splitting pairs
    face_cards = ['J', 'Q', 'K']
    if card_one in face_cards and card_two in face_cards:
        return True
    # Directly compare values
    return card_one == card_two



def can_double_down(card_one, card_two):
    total_value = value_of_card(card_one) + value_of_card(card_two)
    return total_value in [9, 10, 11]
