import random
import string


class Cipher:
    def __init__(self, key: str | None = None):
        if key is None:
            # Generate a random key of at least 100 lowercase letters
            self.key = "".join(random.choice(string.ascii_lowercase) for _ in range(100))
        else:
            if not key.islower() or not key.isalpha():
                raise ValueError("Key must contain only lowercase letters")
            self.key = key

    def encode(self, plaintext: str) -> str:
        return self._translate(plaintext, encode=True)

    def decode(self, ciphertext: str) -> str:
        return self._translate(ciphertext, encode=False)

    def _translate(self, text: str, encode: bool) -> str:
        result = []
        key_len = len(self.key)

        for i, char in enumerate(text):
            text_val = ord(char) - ord("a")
            key_val = ord(self.key[i % key_len]) - ord("a")

            if encode:
                shifted = (text_val + key_val) % 26
            else:
                shifted = (text_val - key_val) % 26

            result.append(chr(shifted + ord("a")))

        return "".join(result)
