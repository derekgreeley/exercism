# go_counting.py
from __future__ import annotations

from collections import deque
from typing import Dict, Iterable, List, Set, Tuple

WHITE = "W"
BLACK = "B"
NONE = " "


Coord = Tuple[int, int]


class Board:
    def __init__(self, board: List[str]):
        self._rows = board
        self._h = len(board)
        self._w = len(board[0]) if self._h else 0

    def _in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self._w and 0 <= y < self._h

    def _at(self, x: int, y: int) -> str:
        return self._rows[y][x]

    def _neighbors4(self, x: int, y: int) -> Iterable[Coord]:
        if x > 0:
            yield (x - 1, y)
        if x + 1 < self._w:
            yield (x + 1, y)
        if y > 0:
            yield (x, y - 1)
        if y + 1 < self._h:
            yield (x, y + 1)

    def territory(self, x: int, y: int) -> Tuple[str, Set[Coord]]:
        if not self._in_bounds(x, y):
            raise ValueError("Invalid coordinate")

        # If it's a stone, it's not a territory query.
        if self._at(x, y) in (BLACK, WHITE):
            return (NONE, set())

        region: Set[Coord] = set()
        bordering: Set[str] = set()

        q = deque([(x, y)])
        region.add((x, y))

        while q:
            cx, cy = q.popleft()
            for nx, ny in self._neighbors4(cx, cy):
                cell = self._at(nx, ny)
                if cell == NONE:
                    if (nx, ny) not in region:
                        region.add((nx, ny))
                        q.append((nx, ny))
                elif cell in (BLACK, WHITE):
                    bordering.add(cell)

        if len(bordering) == 1:
            owner = next(iter(bordering))
            return (owner, region)

        return (NONE, region)

    def territories(self) -> Dict[str, Set[Coord]]:
        # Build sets for each owner by scanning empty regions.
        out: Dict[str, Set[Coord]] = {BLACK: set(), WHITE: set(), NONE: set()}
        visited: Set[Coord] = set()

        for y in range(self._h):
            for x in range(self._w):
                if self._at(x, y) != NONE:
                    continue
                if (x, y) in visited:
                    continue

                owner, region = self.territory(x=x, y=y)
                visited |= region
                out[owner] |= region

        return out
