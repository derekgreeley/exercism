# say.py

SMALL = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

TENS = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

SCALES = [
    (1_000_000_000, "billion"),
    (1_000_000, "million"),
    (1_000, "thousand"),
]


def say_under_1000(n: int) -> str:
    """Convert a number < 1000 into English words."""
    words = []

    # hundreds place
    if n >= 100:
        hundreds = n // 100
        words.append(f"{SMALL[hundreds]} hundred")
        n %= 100
        if n == 0:
            return " ".join(words)

    # tens / ones
    if n < 20:
        if n > 0:
            words.append(SMALL[n])
    else:
        tens_part = (n // 10) * 10
        ones_part = n % 10
        if ones_part == 0:
            words.append(TENS[tens_part])
        else:
            words.append(f"{TENS[tens_part]}-{SMALL[ones_part]}")

    return " ".join(words)


def say(number: int) -> str:
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    words = []

    # handle billions, millions, thousands
    for value, name in SCALES:
        if number >= value:
            count = number // value
            words.append(f"{say_under_1000(count)} {name}")
            number %= value

    # handle remainder under 1000
    if number > 0:
        words.append(say_under_1000(number))

    return " ".join(words)
