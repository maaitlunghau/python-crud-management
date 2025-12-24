from IdolManager import IdolManager

def sub_menu(manager):
    while True:
        print("1. Sort by follower in order ascending")
        print("2. Sort by follower in order descending")
        print("3. Back to menu")
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            manager.sort_all_idols_available_by_follower(option=False)
            break
        elif choice == "2":
            manager.sort_all_idols_available_by_follower(option=True)
            break
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.\n")

def menu():
    manager = IdolManager()
    
    while True:
        print("1. Show all idols")
        print("2. Add new idol")
        print("3. Update idol")
        print("4. Delete idol")
        print("5. Show all idols not yet been stored")
        print("6. Stored idol by code")
        print("7. Sort the idols not yet been stored by follower")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manager.show_all_idols()
        elif choice == "2":
            manager.create_idol()
        elif choice == "3":
            manager.update_idol()
        elif choice == "4":
            manager.delete_idol()
        elif choice == "5":
            manager.show_all_good_idols()
        elif choice == "6":
            manager.store_idol_by_code()
        elif choice == "7":
            sub_menu(manager)

        elif choice == "8":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice! Please try again...\n")

menu()