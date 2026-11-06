class CustomSet:
    def __init__(self, elements=None):
        self.elements = []

        if elements is not None:
            for element in elements:
                self.add(element)

    def isempty(self):
        return len(self.elements) == 0

    def __contains__(self, element):
        return element in self.elements

    def add(self, element):
        if element not in self:
            self.elements.append(element)

    def issubset(self, other):
        return all(element in other for element in self.elements)

    def isdisjoint(self, other):
        return all(element not in other for element in self.elements)

    def __eq__(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented

        return (
            len(self.elements) == len(other.elements)
            and self.issubset(other)
        )

    def intersection(self, other):
        return CustomSet(
            element
            for element in self.elements
            if element in other
        )

    def __sub__(self, other):
        return CustomSet(
            element
            for element in self.elements
            if element not in other
        )

    def __add__(self, other):
        result = CustomSet(self.elements)

        for element in other.elements:
            result.add(element)

        return result