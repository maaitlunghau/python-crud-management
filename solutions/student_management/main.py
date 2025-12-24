from StudentDAO import StudentDAO

def menu():
    DAO = StudentDAO()
    
    while True:
        print("--------------- Student Management ---------------")
        print("1. Show all student")
        print("2. Add new student")
        print("3. Update student information")
        print("4. Delete student")
        print("5. Show students with above-average academic performance.")
        print("6. Add score for student")
        print("7. Filter students with score min to max")
        print("8. Exit")
        print("------------------------------------------------\n")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            DAO.show_all_student()
        elif choice == "2":
            DAO.create_student()
        elif choice == "3":
            DAO.update_student()
        elif choice == "4":
            DAO.delete_student()
        elif choice == "5":
            DAO.show_above_average_students()
        elif choice == "6":
            DAO.add_score()
        elif choice == "7":
            DAO.filter_students_by_score()
        elif choice == "8":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.\n")

menu()