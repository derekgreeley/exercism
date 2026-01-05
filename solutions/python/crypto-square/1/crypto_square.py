# crypto_square.py

import math


def cipher_text(plain_text: str) -> str:
    # Normalize: keep only alphanumeric, lowercase
    normalized = "".join(ch.lower() for ch in plain_text if ch.isalnum())
    if not normalized:
        return ""

    n = len(normalized)

    # Find r and c such that:
    # r * c >= n, c >= r, and c - r <= 1, with smallest possible c
    r = int(math.isqrt(n))
    c = r if r * r >= n else r + 1
    if r * c < n:
        r += 1  # now r is either c or c-1 (since we only bumped r once)

    # Build rectangle rows, pad the last row on the right with spaces
    rows = []
    for i in range(0, n, c):
        row = normalized[i : i + c]
        if len(row) < c:
            row = row + (" " * (c - len(row)))
        rows.append(row)

    # Read down columns to produce c chunks of length r
    chunks = []
    for col in range(c):
        chunk_chars = []
        for row in rows:
            chunk_chars.append(row[col])
        chunks.append("".join(chunk_chars))

    return " ".join(chunks)
