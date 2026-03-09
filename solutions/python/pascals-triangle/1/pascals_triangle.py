# pascals_triangle.py

def rows(n):
    if n < 0:
        raise ValueError("number of rows is negative")

    # base cases
    if n == 0:
        return []
    if n == 1:
        return [[1]]

    # recursive call
    triangle = rows(n - 1)
    prev_row = triangle[-1]

    # build next row
    new_row = [1]
    for i in range(len(prev_row) - 1):
        new_row.append(prev_row[i] + prev_row[i + 1])
    new_row.append(1)

    triangle.append(new_row)
    return triangle