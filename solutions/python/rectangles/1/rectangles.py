# rectangles.py

from typing import List


def rectangles(strings: List[str]) -> int:
    if not strings:
        return 0
    if strings[0] == "":
        return 0

    rows = len(strings)
    cols = len(strings[0])

    # Collect '+' locations per row
    plus_in_row = []
    for r in range(rows):
        row_pluses = [c for c, ch in enumerate(strings[r]) if ch == "+"]
        plus_in_row.append(row_pluses)

    def horiz_ok(r: int, c1: int, c2: int) -> bool:
        """Top/bottom edge must be all '-' or '+' between corners."""
        if c2 <= c1:
            return False
        for c in range(c1 + 1, c2):
            ch = strings[r][c]
            if ch not in "-+":
                return False
        return True

    def vert_ok(c: int, r1: int, r2: int) -> bool:
        """Left/right edge must be all '|' or '+' between corners."""
        if r2 <= r1:
            return False
        for r in range(r1 + 1, r2):
            ch = strings[r][c]
            if ch not in "|+":
                return False
        return True

    count = 0

    # For each possible top edge (r1, c1, c2), find matching bottom edges.
    for r1 in range(rows):
        pluses = plus_in_row[r1]
        n = len(pluses)
        for i in range(n):
            c1 = pluses[i]
            for j in range(i + 1, n):
                c2 = pluses[j]

                # Validate top edge
                if not horiz_ok(r1, c1, c2):
                    continue

                # Search for a bottom row
                for r2 in range(r1 + 1, rows):
                    if strings[r2][c1] != "+" or strings[r2][c2] != "+":
                        continue
                    if not horiz_ok(r2, c1, c2):
                        continue
                    if not vert_ok(c1, r1, r2):
                        continue
                    if not vert_ok(c2, r1, r2):
                        continue
                    count += 1

    return count
