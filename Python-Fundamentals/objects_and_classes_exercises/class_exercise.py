class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count > 0:
            self.students.append(name)
            self.grades.append(grade)
            Class.__students_count -= 1

    def get_average_grade(self):
        result = round(sum(self.grades) / len(self.students), 2)
        return result

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"
