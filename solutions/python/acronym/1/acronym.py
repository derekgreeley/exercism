# acronym.py

import re

def abbreviate(phrase: str) -> str:
    # Hyphens should behave like spaces, but other punctuation should be removed.
    # Replace hyphens with spaces first.
    cleaned = phrase.replace("-", " ")

    # Remove all punctuation except letters, digits, and spaces.
    cleaned = re.sub(r"[^A-Za-z0-9 ]", "", cleaned)

    # Split into words
    words = cleaned.split()

    # Take the first letter of each word, uppercase
    acronym = "".join(word[0].upper() for word in words if word)

    return acronym
