# Direction constants
NORTH = "NORTH"
EAST = "EAST"
SOUTH = "SOUTH"
WEST = "WEST"

# Order matters for rotation (clockwise)
_DIRS = (NORTH, EAST, SOUTH, WEST)
# Movement deltas per direction
_DELTAS = {
    NORTH: (0, 1),
    EAST:  (1, 0),
    SOUTH: (0, -1),
    WEST:  (-1, 0),
}


class Robot:
    def __init__(self, direction, x, y):
        if direction not in _DIRS:
            raise ValueError("Invalid direction")
        self._dir_idx = _DIRS.index(direction)
        self._x = x
        self._y = y

    @property
    def direction(self):
        return _DIRS[self._dir_idx]

    @property
    def coordinates(self):
        return (self._x, self._y)

    def move(self, instructions: str):
        for ch in instructions:
            if ch == "R":
                self._dir_idx = (self._dir_idx + 1) % 4
            elif ch == "L":
                self._dir_idx = (self._dir_idx - 1) % 4
            elif ch == "A":
                dx, dy = _DELTAS[self.direction]
                self._x += dx
                self._y += dy
            else:
                # If you prefer to ignore invalid chars, remove the error.
                raise ValueError(f"Invalid instruction: {ch}")
