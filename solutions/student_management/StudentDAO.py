import re
from Student import Student

class StudentDAO:
    def __init__(self):
        self.students = [
            Student("Alice", 20, "S001", "it", 10),
            Student("Bob", 22, "S002", "accountant", 90),
            Student("Charlie", 19, "S003", "marketing", 75),
            Student("David", 21, "S004", "it", 95),
            Student("Eva", 23, "S005", "marketing", 80),
        ]
        
    # validates    
    def input_student_code(self, is_required=True, checkExist=True):
        pattern = re.compile(r"^S\d{3}$")
        
        while True:
            code = input("Enter the student code: ")
            
            if not is_required and len(code) == 0:
                return None
            
            if not code.strip():
                print("Student Code must be required.\n")
            elif not pattern.match(code):
                print("Student Code must be matched with format: Sxxx.\n")
            elif checkExist and self.find_student_by_code(code):
                print("Student Code already existed.\n")
            else:
                return code
    
    def find_student_by_code(self, code):
        for student in self.students:
            if student.student_code == code:
                return student
        
        return None
    
    def input_name(self, is_required=True):
        while True:
            name = input("Enter the student name: ")
            
            if not is_required and len(name) == 0:
                return None
            
            if not name.strip():
                print("Student Name must be required.\n")
            elif len(name) < 2 or len(name) > 10:
                print("Length of student name must be between 2 to 10 characters.\n")
            else:
                return name
    
    def input_age(self, is_required=True):
        while True:
            age = input("Enter the student age: ")
            
            if not is_required and len(age) == 0:
                return None
            
            if not age.isdigit():
                print("Student Age must be a number.\n")
            elif int(age) < 18 or int(age) > 30:
                print("Student Age must be between 18 to 30 years old.\n")
            else:
                return int(age)
    
    def input_faculty(self, is_required=True):
        while True:
            faculty = input("Enter the student faculty ('IT || Accountant || Marketing'): ")
            
            if not is_required and len(faculty) == 0:
                return None
            
            if not faculty.strip():
                print("Student Faculty must be required.\n")
            elif faculty.lower() not in ["it", "accountant", "marketing"]:
                print("Student Faculty must be in ['IT || Accountant || Marketing'].\n")
            else:
                return faculty.capitalize()
    
    def input_score(self, is_required=True):
        while True:
            score = input("Enter the student score: ")
        
            if not is_required and len(score) == 0:
                return None
            
            if not score.isdigit():
                print("Student Score must be a number.\n")
            elif int(score) < 10 or int(score) > 100:
                print("Student Score must be between 10 to 100 scores.\n")
            else:
                return int(score)
    
    # functions
    def show_all_student(self):
        pass
    
    def create_student(self):
        pass
    
    def update_student(self):
        pass
    
    def delete_student(self):
        pass
    
    def show_above_average_students(self):
        pass
    
    def add_score(self):
        pass
    
    def filter_students_by_score(self):
        pass