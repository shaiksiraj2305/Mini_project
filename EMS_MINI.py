#Initialize employee data
employees = {
    101:{'name':'Satya','age':27,'department':'HR','salary':50000},
    102: {'name': 'Ravi', 'age': 30, 'department': 'Finance', 'salary': 60000},
    103: {'name': 'Anu', 'age': 25, 'department': 'IT', 'salary': 45000}
}

#Function to display the main menu

def main_menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1.Add Employee")
        print("2.View All Employees")
        print("3.Search for Employee")
        print("4.Exit")

        #Get user choice
        choice = input("Enter your choice(1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice =='4':
            print("Thank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 to 4.")


def add_employee():
    print("\n--- Add Employee ---")
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print(f"Employee ID {emp_id} already exitst. Please use a unique ID.")
            return

        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))

        #Add employee to the dictionary
        employees[emp_id] = {'name':name,'age':age,'department':department,'salary':salary}
        print(f"Employee {name}(ID:{emp_id})successfull added.")
    except ValueError:
        print("Invalid input. Please enter valid data.")

#Function to view all employees
def view_employees():
    print("\n --- ALL Employees ---")
    if not employees:
        print("No employees available.")
        return 

    # Display employees in a table-like format
    print(f"{'ID':<10}{'Name':<15}{'AGE':<5}{'Department':<15}{'Salary':<10}")
    print("-"*55)
    for emp_id , details in employees.items():
        print(f"{emp_id:<10}{details['name']:<15}{details['age']:<5}{details['department']:<15}{details['salary']:<10.2f}")

#Function to search for an employee by ID
def search_employee():
    print("\n --- Search Employee ----")
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            details  = employees[emp_id]
            print(f"\nEmployee Details (ID:{emp_id}): ")
            print(f"Name:{details['name']}")
            print(f"Age:{details['age']}")
            print(f"Department:{details['department']}")
            print(f"Salary:{details['salary']:.2f}")
        else:
            print(f"Employee with ID{emp_id} not found.")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")

#Run the program
if __name__ == "__main__":
    main_menu()

