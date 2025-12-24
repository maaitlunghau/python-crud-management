class Patient:
    # Id Pxxx (bat Trung Id)
    # name 2-10 characters
    # age [18-30]
    # faculty: Tim|Gan|Pheo|Phoi
    # gender Female|Male
    
    def __init__(self,id,name,age,faculty,gender):
        self.id = id
        self.name = name
        self.age = age
        self.faculty = faculty
        self.gender = gender
        
    def __str__(self):
        return f"Patient-  Id: {self.id}  Name: {self.name} age: {self.age} Faculty: {self.faculty} Gender: {self.gender}"