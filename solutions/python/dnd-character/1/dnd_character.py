# dnd_character.py
import random
from math import floor

def modifier(score: int) -> int:
    """Ability modifier = floor((score - 10) / 2)."""
    return (score - 10) // 2  # integer floor for negatives too


class Character:
    """Random D&D character with six abilities and hitpoints."""

    @staticmethod
    def ability() -> int:
        """Roll 4d6 and sum the highest 3 dice."""
        rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(rolls, reverse=True)[:3])

    def __init__(self):
        # Generate each ability exactly once and store.
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

        # Hitpoints = 10 + CON modifier
        self.hitpoints = 10 + modifier(self.constitution)
