def resistor_label(colors):
    digit_values = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }

    tolerance_values = {
        "grey": "±0.05%", "violet": "±0.1%", "blue": "±0.25%", "green": "±0.5%",
        "brown": "±1%", "red": "±2%", "gold": "±5%", "silver": "±10%"
    }

    if len(colors) == 1:
        return f"{digit_values[colors[0]]} ohms"

    if len(colors) == 4:
        val1 = digit_values[colors[0]]
        val2 = digit_values[colors[1]]
        multiplier = 10 ** digit_values[colors[2]]
        tolerance = tolerance_values[colors[3]]
        value = (val1 * 10 + val2) * multiplier

    elif len(colors) == 5:
        val1 = digit_values[colors[0]]
        val2 = digit_values[colors[1]]
        val3 = digit_values[colors[2]]
        multiplier = 10 ** digit_values[colors[3]]
        tolerance = tolerance_values[colors[4]]
        value = (val1 * 100 + val2 * 10 + val3) * multiplier
    else:
        raise ValueError("Invalid number of color bands")

    if value >= 1_000_000:
        label = f"{value / 1_000_000:.2f}".rstrip("0").rstrip(".") + " megaohms"
    elif value >= 1_000:
        label = f"{value / 1_000:.2f}".rstrip("0").rstrip(".") + " kiloohms"
    else:
        label = f"{int(value)} ohms"

    return f"{label} {tolerance}"