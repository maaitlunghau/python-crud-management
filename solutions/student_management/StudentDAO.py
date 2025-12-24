import re
from Student import Student
from StudentIterator import StudentIterator
from StudentGenerator import StudentGenerator

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
                print("Student Age must be a integer number.\n")
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
    
    def input_score(self, label="Enter the student score: ", is_required=True):
        while True:
            score = input(label)
        
            if not is_required and len(score) == 0:
                return None
            
            if not score.isdigit():
                print("Student Score must be a integer number.\n")
            elif int(score) < 10 or int(score) > 100:
                print("Student Score must be between 10 to 100 scores.\n")
            else:
                return int(score)
    
    # functions
    def show_all_student(self):
        if not self.students:
            print("There are currently no students present.\n")
            return
        
        for student in StudentIterator(self.students):
            print(student)
            
        print("\n")
    
    def create_student(self):
        student_code = self.input_student_code()
        name = self.input_name()
        age = self.input_age()
        faculty = self.input_faculty()
        score = self.input_score()
        
        new_student = Student(name, age, student_code, faculty, score)
        self.students.append(new_student)
        
        print("✅ Created new student successfully")
    
    def update_student(self):
        if not self.students:
            print("Sorry... The student list is actually empty.")
            return
        
        code = input("Enter the student code to update: ")
        student = self.find_student_by_code(code)
        
        if student:
            print("Enter the new details (leave blank to keep current value): ")
            
            name = self.input_name(is_required=False)
            age = self.input_age(is_required=False)
            faculty = self.input_faculty(is_required=False)
            score = self.input_score(is_required=False)
            
            if name:
                student.name = name
            if age:
                student.age = int(age)
            if faculty:
                student.faculty = faculty
            if score:
                student.score = int(score)
                
            print("✅ Updated student successfully")
            
        else: 
            print(f"No student fond with code {code}.\n")
    
    def delete_student(self):
        if not self.students:
            print("Sorry... The student list is actually empty.\n")
            return
        
        code = input("Enter the student code to delete: ")
        student = self.find_student_by_code(code)
        
        if student:
            self.students.remove(student)
            print(f"✅ Deleted student with code {code} successfully\n")
        else:
            print(f"No student found with code {code}.\n")
    
    def show_above_average_students(self):
        students_generator = StudentGenerator(self.students)
        
        print("------ Above Average Students List ------")
        for student in students_generator:
            if student.score >= 70:
                print(student)
                
        print("\n")
    
    def add_score(self):
        if not self.students:
            print("Sorry... The student list is actually empty.\n")
            return
        
        code = input("Enter the student code to add score: ")
        student = self.find_student_by_code(code)
        
        if student:
            while True:
                add_score = self.input_score("Enter the add score: ")
                
                if (student.score + add_score > 100):
                    print("Total score cannot greater than 100.\n")
                    continue
                
                break
            
            student.score += add_score
            print(f"✅ Added score for student with code {code} successfully\n")
        else:
            print(f"No student found with code {code}.\n")
    
    def filter_students_by_score(self):
        while True:
            min_score = self.input_score("Enter the minimum score: ")
            max_score = self.input_score("Enter the maximum score: ")
            if min_score <= max_score:
                break
            
            print("Min score must be less than or equal to max score.")
            
        filtered_students = []
        
        for student in self.students:
            if min_score <= student.score <= max_score:
                filtered_students.append(student)
                
        if len(filtered_students) > 0:
            for student in filtered_students:
                print(student)
        else:
            print("No students found within the specified score range.")