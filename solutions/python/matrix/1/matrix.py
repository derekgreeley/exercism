# matrix.py

class Matrix:
    def __init__(self, matrix_string: str):
        # Split the string into rows, then split each row into integers
        self._rows = [
            [int(num) for num in line.split()]
            for line in matrix_string.strip().splitlines()
        ]

    def row(self, index: int) -> list[int]:
        """Return the given row (1-indexed)."""
        return self._rows[index - 1]

    def column(self, index: int) -> list[int]:
        """Return the given column (1-indexed)."""
        return [row[index - 1] for row in self._rows]
