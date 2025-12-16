# allergies.py

class Allergies:
    _ALLERGENS = [
        ("eggs", 1),
        ("peanuts", 2),
        ("shellfish", 4),
        ("strawberries", 8),
        ("tomatoes", 16),
        ("chocolate", 32),
        ("pollen", 64),
        ("cats", 128),
    ]

    def __init__(self, score: int):
        # Ignore any bits beyond the known allergens (>= 256)
        self._score = score % 256
        self.lst = [name for name, bit in self._ALLERGENS if self._score & bit]

    def allergic_to(self, item: str) -> bool:
        return item in self.lst
