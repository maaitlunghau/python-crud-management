import re
import csv
from Patient import Patient
from PatientIterator import PatientIterator

class PatientDAO:
    def __init__(this, filename):
        this.filename = filename
        this.patients = this.load_file()
            
    # validates
    def find_patient_by_id(this, id):
        for patient in this.patients:
            if patient.id == id:
                return patient
        return None
    
    def is_duplicate_id(this, id):
        for patient in this.patients:
            if patient.id == id:
                return True
        return False
    
    def input_id(this):
        while True:
            id = input("Enter the patient ID: ").strip()
            
            if not re.match(r"^P\d{3}$", id):
                print("Id must be Pxxx\n")
            elif this.is_duplicate_id(id):
                print("Id is duplicated! Try another...\n")
            else:
                return id 
    
    def input_name(this, is_required =False):
        while True:
            name = input("Enter name: ").strip()
            
            if is_required and len(name) == 0:
                return None
            if 2 <= len(name) <= 10:
                return name        
            else:
                print("Name must be 2-10 characters.\n")   
    
    def input_age(this):
        while True:
            try:
                age = int(input("Enter age: ").strip())
                
                if 18 <= age <= 30:
                    return age
                print("Age must be between [18-30] years old.\n")
            except Exception:
                print("Age must be a number")
    
    def input_faculty(self):
        while True:
            faculty = input("Enter faculty: ").strip().lower()
            
            if faculty in ["tim","gan","hiv","phoi"]:
                return faculty
            print("faculty must be [tim|gan|hiv|phoi]\n")
    
    def input_gender(this):
        while True:
            gender = input("Enter gender: ").strip().lower()
            
            if gender in ["male","female"]:
                return gender
            print("Gender must be [male|female]\n")
    
    # functions
    def show_all_patients(this):
        for patient in PatientIterator(this.patients):
            print(patient)
            
    def add_patient(this):
        id = this.input_id()
        name = this.input_name()
        age = this.input_age()
        faculty = this.input_faculty()
        gender = this.input_gender()
        
        new_patient = Patient(id,name,age,faculty,gender)
        this.patients.append(new_patient)
        
        print("✅ Added new patient successfully")
        
    def update_patient(this):
        id = input("Enter id to update: ").strip()
        patient = this.find_patient_by_id(id)
        
        if not patient:
            print("Not found a patient\n")
            return 
        
        name = this.input_name(is_required=False)
        age = this.input_age()
        faculty = this.input_faculty()
        gender = this.input_gender()
        
        if name:
            patient.name = name
            
        patient.age = age
        patient.faculty = faculty
        patient.gender = gender
        
        print("✅ Updated patient successfully")
        
    def delete_patient(this):
        id = input("Enter id to delete: ").strip()
        patient = this.find_patient_by_id(id)
        
        if not patient:
            print("Not found a patient\n")
            return 
        
        this.patients.remove(patient)
        print("✅ Deleted patient successfully")
    
    def load_file(this):
        loaded_patients = []
        
        try:
            with(open(this.filename, mode="r", newline="") as file):
                reader = csv.reader(file)
                
                for row in reader:
                    if len(row) == 5:
                        patient = Patient(row[0], row[1], row[2], row[3], row[4])
                        loaded_patients.append(patient)
                        
                print("✅ Loaded all patients to file (csv) successfully")
                    
        except Exception:
            print("Failed to load file...")
            
        return loaded_patients
    
    def save_file(this):
        with open(this.filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            
            for patient in this.patients:
                writer.writerow([
                    patient.id, 
                    patient.name, 
                    patient.age, 
                    patient.faculty, 
                    patient.gender
                ])