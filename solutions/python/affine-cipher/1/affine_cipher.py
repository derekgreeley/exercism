from math import gcd

ALPHABET_SIZE = 26


def validate_key(a):
    if gcd(a, ALPHABET_SIZE) != 1:
        raise ValueError("a and m must be coprime.")


def encode(plain_text, a, b):
    validate_key(a)

    encrypted = ""

    for char in plain_text.lower():
        if char.isascii() and char.isalpha():
            x = ord(char) - ord("a")
            y = (a * x + b) % ALPHABET_SIZE
            encrypted += chr(y + ord("a"))

        elif char.isascii() and char.isdigit():
            encrypted += char

    return " ".join(
        encrypted[i:i + 5]
        for i in range(0, len(encrypted), 5)
    )


def decode(ciphered_text, a, b):
    validate_key(a)

    inverse_a = pow(a, -1, ALPHABET_SIZE)

    decrypted = ""

    for char in ciphered_text.lower():
        if char.isascii() and char.isalpha():
            y = ord(char) - ord("a")
            x = (inverse_a * (y - b)) % ALPHABET_SIZE
            decrypted += chr(x + ord("a"))

        elif char.isascii() and char.isdigit():
            decrypted += char

    return decrypted