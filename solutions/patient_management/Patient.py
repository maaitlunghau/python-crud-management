class Patient:
    def __init__(self, id, name, age, faculty, gender):
        self.id = id
        self.name = name
        self.age = age
        self.faculty = faculty
        self.gender = gender
        
    def __str__(self):
        return f"Id: {self.id} | Name: {self.name} | age: {self.age} | Faculty: {self.faculty} | Gender: {self.gender}"