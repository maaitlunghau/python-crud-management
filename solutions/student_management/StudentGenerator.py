class StudentGenerator:
    def __init__(self, students):
        self.students = students
        
    def __iter__(self):
        for student in self.students:
            yield student