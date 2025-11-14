class Garden:
    _PLANT_NAMES = {
        'G': 'Grass',
        'C': 'Clover',
        'R': 'Radishes',
        'V': 'Violets',
    }

    _DEFAULT_STUDENTS = [
        "Alice", "Bob", "Charlie", "David", "Eve", "Fred",
        "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"
    ]

    def __init__(self, diagram: str, students=None):
        self.rows = diagram.splitlines()
        self.students = sorted(students or self._DEFAULT_STUDENTS)

    def plants(self, student: str):
        """Return a list of plant names belonging to the given student."""
        index = self.students.index(student)
        cups = [self.rows[0][2 * index : 2 * index + 2],
                self.rows[1][2 * index : 2 * index + 2]]
        return [self._PLANT_NAMES[ch] for row in cups for ch in row]