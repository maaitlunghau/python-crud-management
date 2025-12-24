
from Patient import Patient
import re
import csv

from PatientItertor import PatientIterator

class PatientDao:
    def __init__(this, filename):
        this.filename = filename
        this.patients = this.load_file()
        
    def show_all(self):
        for item in PatientIterator(self.patients):
            print(item)
            
    def get_patient(self,id):
        for pa in self.patients:
            if pa.id == id:
                return pa
        return None
    
    def is_duplicate_id(self,id):
        for item in self.patients:
            if item.id == id:
                return True
            return False
        
    def input_id(self):
        while True:
            id = input("Enter Id: ").strip()
            if not re.match(r"^P\d{3}$",id):
                print("Id must be Pxxx")
            elif self.is_duplicate_id(id):
                print("Id is duplicated. Try another")
            else:
                return id      

    def input_name(self,skip =False):
        while True:
            name = input("Enter name: ").strip()
            if skip:
                if len(name) == 0:
                    return None
            if 2 <= len(name) <=10:
                return name        
            else:
                print("Name must be 2-10 characters")   

    def input_age(self):
        while True:
            try:
                age = int(input("Enter age: ").strip())
                if 18<= age <= 30:
                    return age
                print("Age must be between [18-30] years old")
            except Exception:
                print("Age must be a number")
    
    def input_faculty(self):
        while True:
                faculty = input("Enter faculty: ").strip().lower()
                if faculty in ["tim","gan","hiv","phoi"]:
                    return faculty
                print("faculty must be [tim|gan|hiv|phoi]")
    
    def input_gender(self):
        while True:
                gender = input("Enter gender: ").strip().lower()
                if gender in ["male","female"]:
                    return gender
                print("gender must be [male|female")
    
    def add_patient(self):
        id = self.input_id()
        name = self.input_name()
        age = self.input_age()
        faculty = self.input_faculty()
        gender = self.input_gender()
        
        pa = Patient(id,name,age,faculty,gender)
        self.patients.append(pa)
    
    def update_patient(self):
        id = input("Enter id to update: ").strip()
        pa = self.get_patient(id)
        
        if not pa:
            print("Khong tim thay patient")
            return 
        
        name = self.input_name(skip=True)
        age = self.input_age()
        faculty = self.input_faculty()
        gender = self.input_gender()
        
        if name:
            pa.name = name
            
        pa.age = age
        pa.faculty = faculty
        pa.gender = gender
        print("update thanh cong")
    
    def load_file(self):
        patients = []
        
        try:
            with(open(self.filename,mode="r",newline="") as file):
                reader = csv.reader(file)
                for row in reader:
                    # Kiem tra neu row có đủ 5 phần tử (id,name,age,faculty,gender)
                    if len(row) == 5:
                        pa = Patient(row[0],row[1],int(row[2]),row[3],row[4])
                        patients.append(pa)
        except Exception:
            print("Loi doc file")
            
        return patients 
    
    def save_file(self):
        with open(self.filename, mode="w",newline="") as file:
            writer = csv.writer(file)
            
            for pa in self.patients:
                writer.writerow([pa.id,pa.name,pa.age, pa.faculty,pa.gender])