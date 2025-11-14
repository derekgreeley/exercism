def saddle_points(matrix):
    if not matrix:
        return []

    # Check for irregular matrix
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("irregular matrix")

    result = []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for row_index in range(num_rows):
        row = matrix[row_index]
        max_in_row = max(row)

        for col_index in range(num_cols):
            value = matrix[row_index][col_index]

            # Must be max in its row
            if value != max_in_row:
                continue

            # Must be min in its column
            col_values = [matrix[r][col_index] for r in range(num_rows)]
            min_in_col = min(col_values)

            if value == min_in_col:
                result.append({"row": row_index + 1, "column": col_index + 1})

    return result