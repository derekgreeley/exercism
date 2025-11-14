class Luhn:
    def __init__(self, s: str) -> None:
        self.s = s

    def valid(self) -> bool:
        # Remove spaces
        digits_only = self.s.replace(" ", "")

        # Must be > 1 char and all digits
        if len(digits_only) <= 1 or not digits_only.isdigit():
            return False

        total = 0
        # Process from right to left; double every second digit
        # rightmost has idx 0, next has idx 1 (double), etc.
        for idx, ch in enumerate(reversed(digits_only)):
            d = ord(ch) - 48  # faster than int(ch) and safe since isdigit() checked
            if idx % 2 == 1:
                d *= 2
                if d > 9:
                    d -= 9
            total += d

        return total % 10 == 0