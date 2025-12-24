# import
import re

employees = []

def show_menu():
    print("\n---------- Employee Management System ----------")
    print("1. Display the employee list")
    print("2. Update the employee")
    print("3. Add the new employee")
    print("4. Display the senior employees")
    print("5. Search employees by name")
    print("6. Sort by salary")
    print("7. Deduct the employee salaries")
    print("8. Exit program")
    print("--------------------------------------------------")
    
    choice = int(input("Enter your choice: "))
    return choice


def input_code():
    while True:
        code = input("Enter the code (Exxx): ")
        pattern = r"^E\d{3}$"
        
        if not code.strip():
            print("❌ Code don't allowed to be blank.\n")
            continue
        elif re.match(pattern, code):
            break
        else:
            print(f"❌ Code {code} was not matched with format 'Exxx'\n")
            continue
        
    return code


def input_name():
    while True:
        name = input("Enter the name: ")
        
        if not name.strip():
            print("❌ Name don't allowed to be blank.\n")
            continue
        elif 2 <= len(name) <= 12:
            break
        else:
            print(f"❌ Name {name} only allowed to contain 2 to 12 characters.\n")
            continue
        
    return name


def input_email():
    while True:
        email = input("Enter the email: ")
        pattern = r"^\w+@\w+\.\w+$"
        
        if not email.strip():
            print("❌ Email don't allowed to be blank.\n")
            continue
        elif re.match(pattern, email):
            break
        else:
            print(f"❌ Email {email} was not matched with format 'xxx@xxx.com'\n")
            continue
        
    return email


def input_age():
    while True:
        age = input("Enter the age (18 to 60): ")
        
        if not age.strip():
            print("❌ Age don't allowed to be blank.\n")
            continue
        elif 18 <= int(age) <= 60:
            break
        else:
            print(f"❌ Age {age} only allowed to enter 18 to 60 years old.\n")
            continue
        
    return int(age)


def input_salary():
    while True:
        salary = input("Enter the salary (1000$ to 8000$): ")
        
        if not salary.strip():
            print("❌ Age don't allowed to be blank.\n")
            continue
        elif 1000 <= float(salary) <= 8000:
            break
        else:
            print(f"❌ Salary {salary} only allowed to enter from 1000 to 8000 dollars.\n")
            continue
        
    return float(salary)


def input_gender():
    while True:
        gender = input("Enter the gender (Female | Male | Other): ")
        
        if not gender.strip():
            print("❌ Gender don't allowed to be blank.\n")
            continue
        elif gender.lower() in ["female", "male", "other"]:
            break
        else:
            print(f"❌ Gender {gender} only allowed to enter is 'Female' or 'Male' or 'Other'.\n")
            continue
            
    return gender


def createNewEmployee():
    print("\nAdd the new employee")
    
    code = input_code()
    name = input_name()
    email = input_email()
    age = input_age()
    salary = input_salary()
    gender = input_gender()
    
    try: 
        newEmployee = {
            "code": code,
            "name": name,
            "email": email,
            "age": age,
            "salary": salary,
            "gender": gender
        }
        
        employees.append(newEmployee)
        
    except Exception:
        print("❌ Failed to create new employee.\n")
    
    # notification
    print("✅ Added new employee successfully")


def updateEmployee():
    if not employees:
        print("❌ Sorry... The employee list is actual empty.")
        return
    
    # code input (updated)
    code_updated = input_code()
    
    hasFound = False
    for emp in employees:
        if emp["code"] == code_updated:
            emp["name"] = input_name()
            emp["email"] = input_email()
            emp["age"] = input_age()
            emp["salary"] = input_salary()
            emp["gender"] = input_gender()
                            
            # notification
            print("✅ Updated employee succeed")
            
            hasFound = True
            break
    
    if not hasFound:        
        print(f"❌ Employee with code '{code_updated} not found....'\n")


def displaySingleEmployee(employee_list):
    count = 0
    
    for (index, emp) in enumerate(employee_list):
        print(f"Employee {index + 1}: Code: {emp['code']} - Name: {emp['name']} - Salary: {emp['salary']} - Gender: {emp['gender']}")
        count += 1
        
    return count


def displayAllEmployees():
    if not employees:
        return print("Sorry... The employee list is actual empty!")

    # display
    employees_iter = iter(employees)
    quantityEmployee = displaySingleEmployee(employees_iter)
    
    # count
    return print(f"Current employee list have {quantityEmployee} employees")


def generateSenior():
    if not employees:
        print("Sorry... The employe list is actual empty.")
        return
    
    for emp in employees:
        if emp["salary"] >= 3000:
            yield emp


def searchEmployeesByName():
    if not employees:
        print("Sorry... The employee list is actual empty.")
        return
    
    # name to search
    name_search = input_name();

    hasFound = False
    count = 0
    search_list = []
    
    for emp in employees:
        if name_search.lower() in emp["name"].lower():
            search_list.append(emp)

            hasFound = True
            count += 1

    if len(search_list) > 0:
        print(f"Have {count} employee match with '{name_search}'")
        displaySingleEmployee(search_list)
    
    if not hasFound:
        print(f"Not found any employee match with name '{name_search}'")


def sub_menu():
    print("\n------- Sort Option  -------")
    print("1. Ascending")
    print("2. Descending")
    print("3. Back to menu")

    sub_choice = input("Enter the option: ")
    return sub_choice


def input_sort_option():
    while True:
        sort_option = sub_menu()
        
        if not sort_option.strip():
            print("Option must be required.")
            continue
        else: 
            break
    
    return int(sort_option)


def sortEmployeeBySalary():
    if not employees:
        print("Sorry... The employee list is actual empty.")
        return
    
    # get option
    sort_option = input_sort_option()
    
    if sort_option == 1:
        employees.sort(key=lambda emp: emp["salary"])
        displaySingleEmployee(employees)
        
    elif sort_option == 2: 
        employees.sort(key=lambda emp: emp["salary"], reverse=True)
        displaySingleEmployee(employees)

    elif sort_option == 3:
        return


def deductSalary():
    if not employees:
        print("❌ Sorry... The employee list is actual empty.")
        return
    
    # get code employee 
    code_deduct = input_code()
    
    hasFound = False
    for emp in employees:
        if emp["code"] == code_deduct:
            # get salary want to deduct
            salary_deduct = input_salary()
            
            if salary_deduct > emp["salary"]:
                print("❌ Salary deduct muts be less than salary of employee ")
                return
            else: 
                emp["salary"] = emp["salary"] - salary_deduct
                
                print("✅ Deducted salary employee succeed")
                print(f"The current salary of employee '{code_deduct}' is {emp["salary"]}")
                
            hasFound = True
            break
            
    if not hasFound:
        print(f"❌ Not found any employee with code '{code_deduct}'")


def main():
    while True:
        choice = show_menu()

        if choice == 1:
            displayAllEmployees()
            
        elif choice == 2:
            updateEmployee()
            
        elif choice == 3:
            createNewEmployee()
            
        elif choice == 4:
            senior_emps = generateSenior()
            count = displaySingleEmployee(senior_emps)
            print(f"Total senior employees: {count} employees")
            
        elif choice == 5:
            searchEmployeesByName()
            
        elif choice == 6:
            sortEmployeeBySalary()
            
        elif choice == 7:
            deductSalary()
        
        elif choice == 8:
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice! Please try again...")
    
    
if __name__ == "__main__":
    main()