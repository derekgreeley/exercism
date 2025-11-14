def spiral_matrix(size):
    """Return a size×size matrix filled in a clockwise spiral with natural numbers."""
    # Create an empty size×size matrix
    matrix = [[0] * size for _ in range(size)]

    num = 1
    top, bottom, left, right = 0, size - 1, 0, size - 1

    while top <= bottom and left <= right:
        # Move left → right across the top row
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Move top → bottom down the right column
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Move right → left across the bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        # Move bottom → top up the left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix
