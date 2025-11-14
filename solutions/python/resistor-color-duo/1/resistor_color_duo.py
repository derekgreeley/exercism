def value(colors):
    color_codes = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    # Extract the numeric values of the first two colors
    first = color_codes[colors[0]]
    second = color_codes[colors[1]]

    return first * 10 + second