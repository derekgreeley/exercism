def annotate(minefield):
    if not minefield:
        return []

    width = len(minefield[0])

    for row in minefield:
        if len(row) != width:
            raise ValueError("The board is invalid with current input.")
        if any(char not in " *" for char in row):
            raise ValueError("The board is invalid with current input.")

    height = len(minefield)
    result = []

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    for y in range(height):
        row_result = ""
        for x in range(width):
            if minefield[y][x] == "*":
                row_result += "*"
            else:
                count = 0
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < height and 0 <= nx < width:
                        if minefield[ny][nx] == "*":
                            count += 1
                row_result += str(count) if count > 0 else " "
        result.append(row_result)

    return result