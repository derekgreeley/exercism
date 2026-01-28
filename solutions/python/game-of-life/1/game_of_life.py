# game_of_life.py

def tick(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    def live_neighbors(r: int, c: int) -> int:
        count = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr = r + dr
                cc = c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    count += 1 if matrix[rr][cc] == 1 else 0
        return count

    next_gen = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            n = live_neighbors(r, c)
            if matrix[r][c] == 1:
                next_gen[r][c] = 1 if n in (2, 3) else 0
            else:
                next_gen[r][c] = 1 if n == 3 else 0

    return next_gen
