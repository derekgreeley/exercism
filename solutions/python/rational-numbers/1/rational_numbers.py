from math import gcd


class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        if numerator == 0:
            self.numerator = 0
            self.denominator = 1
            return

        g = gcd(numerator, denominator)
        numerator //= g
        denominator //= g

        # Ensure denominator is positive
        if denominator < 0:
            numerator *= -1
            denominator *= -1

        self.numerator = numerator
        self.denominator = denominator

    # --------------------
    # Equality
    # --------------------
    def __eq__(self, other):
        return (
            isinstance(other, Rational)
            and self.numerator == other.numerator
            and self.denominator == other.denominator
        )

    # --------------------
    # String (optional debugging)
    # --------------------
    def __repr__(self):
        return f"Rational({self.numerator}, {self.denominator})"

    # --------------------
    # Arithmetic
    # --------------------
    def __add__(self, other):
        return Rational(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __sub__(self, other):
        return Rational(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __mul__(self, other):
        return Rational(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )

    def __truediv__(self, other):
        return Rational(
            self.numerator * other.denominator,
            self.denominator * other.numerator,
        )

    # --------------------
    # Absolute value
    # --------------------
    def __abs__(self):
        return Rational(abs(self.numerator), abs(self.denominator))

    # --------------------
    # Exponentiation (Rational ** int)
    # --------------------
    def __pow__(self, power):
        if power == 0:
            return Rational(1, 1)

        if power > 0:
            return Rational(
                self.numerator ** power,
                self.denominator ** power,
            )
        else:
            power = abs(power)
            return Rational(
                self.denominator ** power,
                self.numerator ** power,
            )

    # --------------------
    # Real number ** Rational
    # --------------------
    def __rpow__(self, base):
        return (base ** self.numerator) ** (1 / self.denominator)