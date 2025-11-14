COLOR_CODES = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

def color_code(color):
    color = color.lower()
    if color in COLOR_CODES:
        return COLOR_CODES[color]
    else:
        raise ValueError(f"'{color}' is not a valid resistor color.")


def colors():
    return [color for color, value in sorted(COLOR_CODES.items(), key=lambda x: x[1])]
