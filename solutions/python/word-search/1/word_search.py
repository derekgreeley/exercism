class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        return self.x == other.x and self.y == other.y


class WordSearch:
    DIRECTIONS = [
        (1, 0),    # Right
        (-1, 0),   # Left
        (0, 1),    # Down
        (0, -1),   # Up
        (1, 1),    # Down-right
        (-1, -1),  # Up-left
        (1, -1),   # Up-right
        (-1, 1),   # Down-left
    ]

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.height = len(puzzle)

    def search(self, word):
        if not word:
            return None

        for y in range(self.height):
            for x in range(len(self.puzzle[y])):

                if self.puzzle[y][x] != word[0]:
                    continue

                for dx, dy in self.DIRECTIONS:
                    if self._matches(word, x, y, dx, dy):
                        end_x = x + (len(word) - 1) * dx
                        end_y = y + (len(word) - 1) * dy

                        return (
                            Point(x, y),
                            Point(end_x, end_y)
                        )

        return None

    def _matches(self, word, x, y, dx, dy):
        for i, letter in enumerate(word):
            new_x = x + i * dx
            new_y = y + i * dy

            if new_y < 0 or new_y >= self.height:
                return False

            if new_x < 0 or new_x >= len(self.puzzle[new_y]):
                return False

            if self.puzzle[new_y][new_x] != letter:
                return False

        return True