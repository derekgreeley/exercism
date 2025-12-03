# scrabble_score.py

def score(word: str) -> int:
    if not word:
        return 0

    values = {
        1: set("AEIOULNRST"),
        2: set("DG"),
        3: set("BCMP"),
        4: set("FHVWY"),
        5: set("K"),
        8: set("JX"),
        10: set("QZ"),
    }

    total = 0
    for ch in word.upper():
        for points, letters in values.items():
            if ch in letters:
                total += points
                break

    return total
