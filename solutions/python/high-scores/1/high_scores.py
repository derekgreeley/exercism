# high_scores.py

class HighScores:
    def __init__(self, scores: list[int]):
        self.scores = scores

    def latest(self) -> int:
        """Return the most recently added score."""
        return self.scores[-1]

    def personal_best(self) -> int:
        """Return the highest score."""
        return max(self.scores)

    def personal_top_three(self) -> list[int]:
        """Return the top three scores in descending order."""
        return sorted(self.scores, reverse=True)[:3]
