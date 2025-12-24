from Person import Person

class Student(Person):
    def __init__(self, name, age, student_code, faculty, score):
        super().__init__(name, age)
        
        self.student_code = student_code
        self.faculty = faculty
        self.score = score
        
    @property
    def student_code(self):
        return self._student_code
    
    @property
    def faculty(self):
        return self._faculty
    
    @property
    def score(self):
        return self._score
    
    @student_code.setter
    def student_code(self, value):
        self._student_code = value
        
    @faculty.setter
    def faculty(self, value):
        self._faculty = value
        
    @score.setter
    def score(self, value):
        self._score = value
        
    def __str__(self):
        return f"Student Code: {self.student_code}, Name: {self.name}, Age: {self.age}, Faculty: {self.faculty}, Score: {self.score}"