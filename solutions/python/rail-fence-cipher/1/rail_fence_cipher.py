# rail_fence_cipher.py

from typing import List


def _rail_pattern(length: int, rails: int) -> List[int]:
    """
    Returns a list of rail indices (0..rails-1) for each character position,
    following the zig-zag pattern.
    """
    if rails <= 1:
        return [0] * length

    pattern = []
    rail = 0
    direction = 1  # +1 going down, -1 going up

    for _ in range(length):
        pattern.append(rail)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return pattern


def encode(message: str, rails: int) -> str:
    if rails <= 1 or len(message) <= 1:
        return message

    pattern = _rail_pattern(len(message), rails)
    rows = [[] for _ in range(rails)]
    for ch, r in zip(message, pattern):
        rows[r].append(ch)

    return "".join("".join(row) for row in rows)


def decode(ciphertext: str, rails: int) -> str:
    if rails <= 1 or len(ciphertext) <= 1:
        return ciphertext

    n = len(ciphertext)
    pattern = _rail_pattern(n, rails)

    # Count how many chars go to each rail
    counts = [0] * rails
    for r in pattern:
        counts[r] += 1

    # Slice ciphertext into rail strings
    rails_strs = []
    idx = 0
    for c in counts:
        rails_strs.append(list(ciphertext[idx : idx + c]))
        idx += c

    # Reconstruct by walking the zig-zag and popping from each rail
    result = []
    rail_positions = [0] * rails
    for r in pattern:
        pos = rail_positions[r]
        result.append(rails_strs[r][pos])
        rail_positions[r] += 1

    return "".join(result)
