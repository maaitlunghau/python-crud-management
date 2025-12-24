from IdolManager import IdolManager


def submenu_sort(manager):
    while True:
        print("1. Sắp xếp theo follower tăng dần")
        print("2. Sắp xếp theo follower giảm dần")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            manager.sort_available_idols_by_follower(ascending=True)
            break
        elif choice == "2":
            manager.sort_available_idols_by_follower(ascending=False)
            break
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.\n")


def menu():
    manager = IdolManager()

    while True:
        print("1. Show all idol")
        print("2. Add new idol")
        print("3. Delete idol")
        print("4. Update idol information")
        print("5. Hiển thị idol chưa nhập kho")
        print("6. Nhập kho idol theo code")
        print("7. Sắp xếp idol chưa nhập kho theo follower")

        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manager.view_all()
        elif choice == "2":
            manager.create_idol()
        elif choice == "3":
            manager.delete_idol()
        elif choice == "4":
            manager.update_idol()
        elif choice == "5":
            manager.show_available_idols()
        elif choice == "6":
            manager.store_idol_by_code()
        elif choice == "7":
            submenu_sort(manager)
        elif choice == "8":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.\n")


menu()
