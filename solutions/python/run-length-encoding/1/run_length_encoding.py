# run_length_encoding.py

def encode(s: str) -> str:
    if not s:
        return ""

    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            # Append count ONLY if >1
            if count > 1:
                result.append(str(count))
            result.append(s[i - 1])
            count = 1

    # Handle last run
    if count > 1:
        result.append(str(count))
    result.append(s[-1])

    return "".join(result)


def decode(s: str) -> str:
    if not s:
        return ""

    result = []
    count = ""

    for ch in s:
        if ch.isdigit():
            count += ch
        else:
            # If no count stored, the count is 1
            num = int(count) if count else 1
            result.append(ch * num)
            count = ""

    return "".join(result)
