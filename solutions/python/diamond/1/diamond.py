def rows(letter):
    if letter < 'A' or letter > 'Z':
        raise ValueError("Input must be a capital letter from A to Z.")

    size = ord(letter) - ord('A')
    width = size * 2 + 1
    result = []

    for i in range(size + 1):
        ch = chr(ord('A') + i)
        if i == 0:
            line = ch.center(width)
        else:
            inner_space = 2 * i - 1
            line = (ch + ' ' * inner_space + ch).center(width)
        result.append(line)

    # Add bottom half (excluding the middle line again)
    result += result[-2::-1]

    return result