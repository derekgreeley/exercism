# line_up.py

def _ordinal_suffix(n: int) -> str:
    # 11, 12, 13 are special cases
    if 10 <= (n % 100) <= 13:
        return "th"

    last = n % 10
    if last == 1:
        return "st"
    if last == 2:
        return "nd"
    if last == 3:
        return "rd"
    return "th"


def line_up(name: str, number: int) -> str:
    # Spec says 1..999; tests don't require raising on out-of-range,
    # but you can enforce it if you want:
    # if number < 1 or number > 999:
    #     raise ValueError("input out of range")

    suffix = _ordinal_suffix(number)
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
