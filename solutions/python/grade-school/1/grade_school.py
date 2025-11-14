class School:
    def __init__(self):
        # grade -> set of student names
        self._grades = {}
        # student name -> grade (to prevent duplicates across the whole roster)
        self._student_to_grade = {}
        # record of results (True/False) for each add_student call
        self._added_results = []

    def add_student(self, *, name: str, grade: int) -> None:
        """
        Attempt to add a student to a grade.
        Records True if added, False if the student already exists in any grade.
        """
        if name in self._student_to_grade:
            # cannot add same student again (same or different grade)
            self._added_results.append(False)
            return

        # add student
        self._student_to_grade[name] = grade
        self._grades.setdefault(grade, set()).add(name)
        self._added_results.append(True)

    def added(self):
        """
        Return the list of booleans corresponding to each call to add_student,
        in order.
        """
        return self._added_results

    def roster(self):
        """
        Return a flat list of all students across all grades,
        with grades sorted ascending and names within a grade sorted alphabetically.
        """
        all_students = []
        for g in sorted(self._grades):
            all_students.extend(sorted(self._grades[g]))
        return all_students

    def grade(self, n: int):
        """
        Return a list of students in grade n, sorted alphabetically.
        If no students in that grade, return [].
        """
        return sorted(self._grades.get(n, set()))
