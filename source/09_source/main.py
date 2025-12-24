from PatientDao import PatientDao

def menu():
    dao = PatientDao("patient.csv")
    while True:
        
        print("***PATIENT MANAGEMENT***")
        print("1. Show all patients")
        print("2. Add a patient")
        print("3. Delete a patient")
        print("4. Update a patient")
        print("5. Save patient to file")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            dao.show_all()
        elif choice == "2":
            dao.add_patient()
        elif choice == "5":
            dao.save_file()     
        elif choice == "4":
            dao.update_patient()        
        elif choice == "6":
            return
        else:
            print("Your choice went wrong. Try it again")
            
if __name__=="__main__":
    menu()
