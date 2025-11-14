def commands(binary_str):
    actions = [
        "wink",
        "double blink",
        "close your eyes",
        "jump"
    ]

    number = int(binary_str, 2)

    result = []

    for i in range(4):
        if number & (1 << i):
            result.append(actions[i])

    if number & (1 << 4):
        result.reverse()

    return result