# connect.py

from collections import deque


class ConnectGame:
    def __init__(self, board):
        """
        board: multiline string, rows separated by newlines,
               cells separated by spaces ('.', 'X', 'O')
        """
        # Normalize the board into a 2D list of cells
        rows = [
            line.strip()
            for line in board.splitlines()
            if line.strip() != ""
        ]
        self.grid = [row.split() for row in rows]
        self.height = len(self.grid)
        self.width = len(self.grid[0]) if self.height > 0 else 0

    def get_winner(self):
        # By convention in the Exercism problem, O (top→bottom) is checked first
        if self._has_path('O'):
            return 'O'
        if self._has_path('X'):
            return 'X'
        return ""

    # ---- Internal helpers ----

    def _neighbors(self, r, c):
        """
        Return list of valid neighbor coordinates for hex grid in this layout.
        Adjacency pattern (row, col):
        - left:        (r, c-1)
        - right:       (r, c+1)
        - up:          (r-1, c)
        - down:        (r+1, c)
        - up-right:    (r-1, c+1)
        - down-left:   (r+1, c-1)
        """
        candidates = [
            (r, c - 1),
            (r, c + 1),
            (r - 1, c),
            (r + 1, c),
            (r - 1, c + 1),
            (r + 1, c - 1),
        ]
        return [
            (rr, cc)
            for rr, cc in candidates
            if 0 <= rr < self.height and 0 <= cc < self.width
        ]

    def _has_path(self, player):
        """
        Determine if `player` has a connecting path.
        - 'X': left to right
        - 'O': top to bottom
        """
        if self.height == 0 or self.width == 0:
            return False

        visited = set()
        queue = deque()

        if player == 'X':
            # Start from all X stones on the left edge (col = 0)
            for r in range(self.height):
                if self.grid[r][0] == 'X':
                    queue.append((r, 0))
                    visited.add((r, 0))

            target_col = self.width - 1

            while queue:
                r, c = queue.popleft()
                if c == target_col:
                    return True
                for nr, nc in self._neighbors(r, c):
                    if (nr, nc) not in visited and self.grid[nr][nc] == 'X':
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return False

        elif player == 'O':
            # Start from all O stones on the top edge (row = 0)
            for c in range(self.width):
                if self.grid[0][c] == 'O':
                    queue.append((0, c))
                    visited.add((0, c))

            target_row = self.height - 1

            while queue:
                r, c = queue.popleft()
                if r == target_row:
                    return True
                for nr, nc in self._neighbors(r, c):
                    if (nr, nc) not in visited and self.grid[nr][nc] == 'O':
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return False

        # Unknown player symbol (shouldn't happen in tests)
        return False
