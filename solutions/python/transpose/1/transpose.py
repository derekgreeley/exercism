def transpose(text: str) -> str:
    if not text:
        return ""

    lines = text.splitlines()
    max_len = max(len(line) for line in lines)

    # Pad with a sentinel so we can distinguish padding from real spaces
    SENT = "\0"
    padded = [line.ljust(max_len, SENT) for line in lines]

    # Transpose
    transposed = ["".join(row[i] for row in padded) for i in range(max_len)]

    # Strip only sentinel padding (not spaces), then turn remaining sentinels into spaces
    transposed = [t.rstrip(SENT).replace(SENT, " ") for t in transposed]

    return "\n".join(transposed)
