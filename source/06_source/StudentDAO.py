from Student import Student
import re
from StudentGenerator import StudentGenerator
from StudentIterator import StudentIterator


class StudentDAO:
    def __init__(self):
        self.students = [
            Student("Alice", 20, "S001", "it", 10),
            Student("Bob", 22, "S002", "accountant", 90),
            Student("Charlie", 19, "S003", "marketing", 75),
            Student("David", 21, "S004", "it", 95),
            Student("Eva", 23, "S005", "marketing", 80),
        ]

    def show_all(self):
        for patient in StudentIterator(self.students):
            print(patient)

    def input_student_code(self, isRequired=True, checkExist=True):
        # r => raw string
        pattern = re.compile(r"^S[0-9]{3}$")
        while 1:
            code = input("Nhập mã sinh viên (SXXX): ")

            if not isRequired and len(code) == 0:
                return None

            if not pattern.match(code):
                print("Mã sinh viên không hợp lệ. Phải có ở dạng SXXX. VD: S001\n")
            elif checkExist and self.findStudentByCode(code):
                print("Mã số sinh viên đã tồn tại từ trước!")
            else:
                return code

    def findStudentByCode(self, code):
        for student in self.students:
            if student.student_code == code:
                return student
        return None

    def input_name(self, isRequired=True):
        while True:
            name = input("Enter the name: ").strip()
            if not isRequired and len(name) == 0:
                return None

            if 2 <= len(name) <= 20:
                return name
            print("Name must be between 2 and 20 characters.\n")

    def input_age(self, isRequired=True):
        while True:
            age = input("Enter the age: ")
            if not isRequired and len(age) == 0:
                return 0
            age = int(age)
            if 18 <= age <= 30:
                return age
            else:
                print("Age must be between 18 and 30.\n")

    def input_faculty(self, isRequired=True):
        while True:
            faculty = (
                input("Enter the faculty (IT|Accountant|Marketing): ").strip().lower()
            )
            if not isRequired and len(faculty) == 0:
                return None

            if faculty in ["it", "accountant", "marketing"]:
                return faculty
            print("Faculty must be one of the following: IT, Accountant, Marketing.\n")

    def input_score(self, label="Enter the score: ", isRequired=True):
        while True:
            score = input(label)

            if not isRequired and len(score) == 0:
                return 0

            score = int(score)
            if 10 <= score <= 100:
                return score
            else:
                print("Score must be between 10 and 100.\n")

    def create_student(self):
        id = self.input_student_code()
        name = self.input_name()
        age = self.input_age()
        faculty = self.input_faculty()
        score = self.input_score()

        newStudent = {
            "id": id,
            "name": name,
            "age": age,
            "faculty": faculty,
            "score": score,
        }

        newStudent = Student(id, name, age, faculty, score)
        self.students.append(newStudent)
        print("Created new student succeed")

    def update_student(self):
        code = input("Enter the student code to update: ").strip()
        student = self.findStudentByCode(code)
        if student:
            print("Enter new details (leave blank to keep current value):")
            name = self.input_name(isRequired=False)
            age = self.input_age(isRequired=False)
            faculty = self.input_faculty(isRequired=False)
            score = self.input_score(isRequired=False)

            if name:
                student.name = name
            if age:
                student.age = int(age)
            if faculty:
                student.faculty = faculty
            if score:
                student.score = int(score)

            print(f"Update successfully.")
        else:
            print(f"No student found with code {code}.")

    def display_above_average_students(self):
        studentGen = StudentGenerator(self.students)
        for student in studentGen:
            if student.score >= 70:
                print(student)

    def add_score(self):
        code = self.input_student_code(checkExist=False)
        student = self.findStudentByCode(code)
        if student:
            while True:
                additional_score = self.input_score(
                    "Enter the additional score to add: "
                )

                if (student.score + additional_score) > 100:
                    print("Total score cannot greater 100.")
                    continue
                break

            student.score += additional_score
            print(f"Added score successfully.")
        else:
            print(f"No student found with code {code}.")

    def delete_student(self):
        code = self.input_student_code(checkExist=False)
        student = self.findStudentByCode(code)
        if student:
            self.students.remove(student)
            print(f"Student with code {code} has been deleted.")
        else:
            print(f"No student found with code {code}.")

    def filter_students(self):
        while True:
            min_score = self.input_score("Enter minimum score: ")
            max_score = self.input_score("Enter maximum score: ")
            if min_score <= max_score:
                break
            print("Min score must be less than or equal to max score.\n")

        filtered_students = []
        for student in self.students:
            if min_score <= student.score <= max_score:
                filtered_students.append(student)
        if len(filtered_students) > 0:
            for student in filtered_students:
                print(student)
        else:
            print("No students found within the specified score range.")
