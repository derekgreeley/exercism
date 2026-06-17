def slices(series: str, length: int) -> list[str]:
    # Validation in the order specified in the instructions/tests

    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    if not series:
        raise ValueError("series cannot be empty")

    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    # Build all contiguous substrings of the given length
    return [series[i:i + length] for i in range(len(series) - length + 1)]
