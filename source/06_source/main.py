from StudentDAO import StudentDAO


def menu():
    dao = StudentDAO()

    while True:
        print("1. Show all student")
        print("2. Add new student")
        print("3. Delete student")
        print("4. Update student information")
        print("5. Show students with above-average academic performance.")
        print("6. Add score for student")
        print("7. Filter students with score min to max")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            dao.show_all()
        elif choice == "2":
            dao.create_student()
        elif choice == "3":
            dao.delete_student()
        elif choice == "4":
            dao.update_student()
        elif choice == "5":
            dao.display_above_average_students()
        elif choice == "6":
            dao.add_score()
        elif choice == "7":
            dao.filter_students()

        elif choice == "8":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.\n")


menu()
