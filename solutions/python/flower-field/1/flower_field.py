def annotate(garden: list[str]) -> list[str]:

    err = "The board is invalid with current input."

    # Empty board is valid
    if garden == []:
        return []

    # Type and rectangularity checks; charset validation
    if not isinstance(garden, list):
        raise ValueError(err)

    width = None
    for row in garden:
        if not isinstance(row, str):
            raise ValueError(err)
        width = len(row) if width is None else width
        if len(row) != width:
            raise ValueError(err)
        # Only ' ' and '*'
        if any(ch not in (" ", "*") for ch in row):
            raise ValueError(err)

    rows, cols = len(garden), width

    # Zero-width rows are valid; return as-is
    if cols == 0:
        return garden[:]

    def in_bounds(r: int, c: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols

    out = []
    for r in range(rows):
        new_row = list(garden[r])
        for c in range(cols):
            if new_row[c] == "*":
                continue
            # Count adjacent flowers
            count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    rr, cc = r + dr, c + dc
                    if in_bounds(rr, cc) and garden[rr][cc] == "*":
                        count += 1
            if count > 0:
                new_row[c] = str(count)
        out.append("".join(new_row))
    return out