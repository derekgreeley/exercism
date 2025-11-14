def rotate(text, key):
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            rotated = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            result.append(rotated)
        elif 'A' <= char <= 'Z':
            rotated = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
            result.append(rotated)
        else:
            result.append(char)

    return ''.join(result)