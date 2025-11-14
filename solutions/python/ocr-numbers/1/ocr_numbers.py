DIGITS = {
    # keys are 4-line tuples (each 3 chars wide)
    (
        " _ ",
        "| |",
        "|_|",
        "   ",
    ): "0",
    (
        "   ",
        "  |",
        "  |",
        "   ",
    ): "1",
    (
        " _ ",
        " _|",
        "|_ ",
        "   ",
    ): "2",
    (
        " _ ",
        " _|",
        " _|",
        "   ",
    ): "3",
    (
        "   ",
        "|_|",
        "  |",
        "   ",
    ): "4",
    (
        " _ ",
        "|_ ",
        " _|",
        "   ",
    ): "5",
    (
        " _ ",
        "|_ ",
        "|_|",
        "   ",
    ): "6",
    (
        " _ ",
        "  |",
        "  |",
        "   ",
    ): "7",
    (
        " _ ",
        "|_|",
        "|_|",
        "   ",
    ): "8",
    (
        " _ ",
        "|_|",
        " _|",
        "   ",
    ): "9",
}


def convert(rows: list[str]) -> str:
    """
    Convert a grid of OCR digits (pipes/underscores/spaces) into a string.

    - Input lines must be a multiple of 4.
    - Each line must have the same length, and the number of columns must
      be a multiple of 3.
    - Unknown glyphs map to '?'.
    - Multiple 4-line blocks are joined by commas.
    """
    # Validation: number of lines must be multiple of 4
    if len(rows) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    # Allow completely empty input -> empty string
    if not rows:
        return ""

    width = len(rows[0])

    # All rows must have equal length
    if any(len(r) != width for r in rows):
        raise ValueError("Number of input columns is not a multiple of three")

    # Columns must be a multiple of 3
    if width % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    out_lines = []

    # Process in chunks of 4 rows (one "line" of digits per chunk)
    for block_start in range(0, len(rows), 4):
        block = rows[block_start:block_start + 4]
        digits = []
        # Slice each 3-column glyph across the width
        for col in range(0, width, 3):
            glyph = tuple(line[col:col + 3] for line in block)
            digits.append(DIGITS.get(glyph, "?"))
        out_lines.append("".join(digits))

    # Join multiple 4-row blocks with commas
    return ",".join(out_lines)
