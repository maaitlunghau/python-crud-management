from PatientDAO import PatientDAO

def menu():
    DAO = PatientDAO("patient_data.csv")
    
    while True:
        print("1. Show all patients")
        print("2. Add new patient")
        print("3. Update a patient")
        print("4. Delete a patient")
        print("5. Save patient to file")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            DAO.show_all_patients()
        elif choice == "2":
            DAO.add_patient()
        elif choice == "3":
            DAO.update_patient()
        elif choice == "4":
            DAO.update_patient()
        elif choice == "5":
            DAO.save_file()

        elif choice == "6":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice! Please try again...\n")

menu()