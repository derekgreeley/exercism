def label(colors):
    color_map = {
        "black": 0, "brown": 1, "red": 2, "orange": 3,  "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8,  "white": 9
    }

    first = color_map[colors[0]]
    second = color_map[colors[1]]
    multiplier = color_map[colors[2]]

    value = int(f"{first}{second}") * (10 ** multiplier)

    if value >= 1_000_000_000:
        return f"{value// 1_000_000_000} gigaohms"
    elif value >= 1_000_000:
        return f"{value// 1_000_000} megaohms"
    elif value >= 1_000:
        return f"{value// 1_000} kiloohms"
    else:
        return f"{value} ohms"