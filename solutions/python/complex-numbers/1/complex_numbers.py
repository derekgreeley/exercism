# complex_numbers.py

import math


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if not isinstance(other, ComplexNumber):
            return False
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        other = self._coerce(other)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other = self._coerce(other)
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __rsub__(self, other):
        other = self._coerce(other)
        return other.__sub__(self)

    def __mul__(self, other):
        other = self._coerce(other)
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real, imaginary)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        other = self._coerce(other)
        denom = other.real ** 2 + other.imaginary ** 2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denom
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denom
        return ComplexNumber(real, imaginary)

    def __rtruediv__(self, other):
        other = self._coerce(other)
        return other.__truediv__(self)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        factor = math.exp(self.real)
        return ComplexNumber(
            factor * math.cos(self.imaginary),
            factor * math.sin(self.imaginary),
        )

    def _coerce(self, value):
        if isinstance(value, ComplexNumber):
            return value
        return ComplexNumber(value, 0)