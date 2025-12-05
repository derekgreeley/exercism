# phone_number.py

class PhoneNumber:
    def __init__(self, raw: str):
        # First, check for letters & invalid punctuation
        digits = []
        for ch in raw:
            if ch.isalpha():
                # letters anywhere are not permitted
                raise ValueError("letters not permitted")
            elif ch.isdigit():
                digits.append(ch)
            elif ch in " .-+()":
                # allowed formatting characters - ignore
                continue
            elif ch.isspace():
                # spaces are fine
                continue
            else:
                # anything else is disallowed punctuation
                raise ValueError("punctuations not permitted")

        num = "".join(digits)

        # Length checks
        if len(num) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(num) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(num) == 11:
            if num[0] != "1":
                raise ValueError("11 digits must start with 1")
            # strip country code
            num = num[1:]

        # Now must be exactly 10 digits
        area = num[0:3]
        exchange = num[3:6]

        # Area code rules
        if area[0] == "0":
            raise ValueError("area code cannot start with zero")
        if area[0] == "1":
            raise ValueError("area code cannot start with one")

        # Exchange code rules
        if exchange[0] == "0":
            raise ValueError("exchange code cannot start with zero")
        if exchange[0] == "1":
            raise ValueError("exchange code cannot start with one")

        self.number = num  # cleaned 10-digit string

    @property
    def area_code(self) -> str:
        return self.number[0:3]

    def pretty(self) -> str:
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:10]}"
