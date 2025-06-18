#                   === Employee Data System for HR in NGO ===

# Greetings
def greetings():
    print('=== Welcome to Employee Data System for HR ===\n')

    user_hr = 'user123'
    pass_hr = 'program'

    # User login
    while True:
        user_input = str(input('Please enter your username: '))
        pass_input = str(input('Please enter your password: '))

        if user_input == user_hr and pass_input == pass_hr:
            print('Login successful!')
            print('-'*30)
            break
        else:
            print('Incorrect username or password! Please try again.\n')

# Choose menu options
def list_menu():
    while True:
        print('\nPlease select an option from the menu below.')
        print('Menu:')
        print('1. View All Employee List')
        print('2. Search Employee')
        print('3. Add New Employee')
        print('4. Update Employee')
        print('5. Delete Employee')
        print('6. Exit Program')
        input_menu = input('Select an Option (1-5): ')
        if input_menu == '1':
            read_emp()
        elif input_menu == '2':
            search_emp()
        elif input_menu == '3':
            add_emp()
        elif input_menu == '4':
            update_emp()
        elif input_menu == '5':
            delete_emp()
        elif input_menu == '6':
            print('Thank you for using the system!')
            break
        else:
            print('Invalid option. Please enter a number between 1 and 5.')


# Variables
first_name = ['Luthfia','Aji','Alya','Ririn','Budi','Fajar','Siti','Intan','Putri','Muhammad']
last_name = ['Amalia','Nugroho','Dzakia','Ayudia','Setiawan','Nugroho','Nurhaliza','Permatasari',
             'Amalia','Fadilah']
position = ['Research Officer', 'Data Officer','Finance Officer','Field Facilitator',
            'Communication Officer','Policy & Advocacy Manager','Food Policy Analyst',
            'Project Officer','Communication Officer','Talent Development Officer']
department = ['Research & Dev','Information & Tech','Finance','Program Implementation','Communication','Policy Unit',
              'Policy Unit','Program Implementation','Communication','Human Resources']
salary = [6500000,6000000,5000000,5000000,6000000,9000000,8000000,7000000,6000000,5000000]
emp_status = ['Active','Active','Leave','Active','Resign','Active','Leave',
              'Resign','Active','Active']
birthdate = ['2002-04-01','1999-10-03','1998-12-22','2000-05-30','1995-07-26','1996-11-14','2000-09-08','1996-08-19','1999-04-01','1998-01-12']
emp_id = []

# Auto-generated employee ID based on Department-First Name-Last Name-Birthdate
def make_emp_id(department, first_name, last_name, birthdate):
    dep_as = department[0:3].upper()
    name_as = first_name[0].upper() + last_name[0].upper()
    
    year = birthdate[0:4]   
    month = birthdate[5:7] 
    day = birthdate[8:10]
    birth_as = year + month + day
    emp_id_birth = dep_as + '-' + name_as + '-' + birth_as
    
    return emp_id_birth

for eid in range(len(first_name)):
    emp_id.append(make_emp_id(department[eid], first_name[eid], last_name[eid], birthdate[eid]))

#  Make table from variables
def table_emp():
    print(f'{'Employee ID':<15} {'First Name':<10} {'Last Name':<12}{'Job Position':<27} {'Department':<25} {'Salary':<10} {'Status':<7} {'Birthdate':<12}')
    print('-'*122)
    for t in range(len(emp_id)):
        print(f'{emp_id[t]:<15} {first_name[t]:<10} {last_name[t]:<12} {position[t]:<27} {department[t]:<25} {salary[t]:<10,} {emp_status[t]:<7} {birthdate[t]:<12}')


# CRUD 1: Read - View All Employee List
def read_emp():
    print('\n=== Here is the full list of employees ===\n')
    table_emp()
    list_menu()

# CRUD 1: Read - Search Employee Based on Employee ID
def search_emp():
    while True:
        print('\n=== Search Employee ===')
        print('\nSearch by:')
        print('1. Employee ID')
        print('2. Back to Main Menu')

        search_opt = input('Choose option between 1 or 2: ')

        if search_opt == '1':
            search_id = input('Enter Employee ID to search: ').upper()
            for si in range(len(emp_id)):
                if emp_id[si] == search_id:
                    print('\nEmployee found:\n')
                    print(f'{"Employee ID":<15} {"First Name":<10} {"Last Name":<12} {"Job Position":<27} {"Department":<25} {"Salary":<10} {"Status":<7} {"Birthdate":<12}')
                    print('-' * 122)
                    print(f'{emp_id[si]:<15} {first_name[si]:<10} {last_name[si]:<12} {position[si]:<27} {department[si]:<25} {salary[si]:<10,} {emp_status[si]:<7} {birthdate[si]:<12}')
                    break
                else:
                    print('\nNo employee found with that ID.')
                    break
    
        elif search_opt == '2':
            list_menu()

        else:
            print('Invalid option. Please enter an option between 1 or 2.')

# CRUD 2: Create - Add Employee
def add_emp():
    print('\n=== Add New Employee ===')
    while True:
        print('1. Add New Employee')
        print('2. Back to main menu')     

        input_add = input('Choose option between 1 or 2: ')
        if input_add == '1':
            print('=== Add New Employee ===')
            print('\n')
            table_emp()

            while True:
                emp_first_input = (input(f"Please enter the employee's first name: ")).capitalize()
                if emp_first_input != '':
                    break
                else:
                    print('Name cannot be empty!')

            while True:
                emp_last_input = str(input(f"Please enter the employee's last name: ")).capitalize()
                if emp_last_input != '':
                    break
                else:
                    print('Name cannot be empty!')

            while True:
                position_input = str(input(f"Please enter the employee's position/job title: ")).title()
                if position_input != '':
                    break
                else:
                    print('Position cannot be empty!')

            while True:
                department_input = str(input(f"Please enter the employee's department/division: ")).title()
                if department_input != '':
                    break
                else:
                    print('Department cannot be empty!')

            while True:
                salary_input = int(input(f"Please enter the employee's salary (ex. 7000000): "))
                if salary_input != '':
                    break
                else:
                    print('Status cannot be empty!')
        
            while True:
                emp_status_input = str(input(f"Please enter the employee's status (Active/Resigned/Leave): ")).capitalize()
                if emp_status_input != '':
                    break
                else:
                    print('Status cannot be empty!')
            
            while True:
                emp_birthdate_input = (input(f"Please enter the employee's birthdate (format: YYYY-MM-DD): "))
                if emp_birthdate_input != '':
                    break
                else:
                    print('Birthdate cannot be empty!')
            
             # Generate new employee ID
            new_emp_id = make_emp_id(department_input, emp_first_input, emp_last_input, emp_birthdate_input)

            if new_emp_id in emp_id:
                print(f"\nSorry, an employee with the ID '{new_emp_id}' already exists.")
            else:
                print('\nConfirmation:')
                print('1. Yes')
                print('2. No')

                while True:
                    confirm_add = input('Are you sure you want to add and save this employee? (choose between 1 or 2): ')
                    if confirm_add == '1':
                        first_name.append(emp_first_input)
                        last_name.append(emp_last_input)
                        position.append(position_input)
                        department.append(department_input)
                        salary.append(salary_input)
                        emp_status.append(emp_status_input)
                        birthdate.append(emp_birthdate_input)
                        emp_id.append(new_emp_id)

                        print('\n')
                        print(f'Employee data has been successfully added with ID: {new_emp_id}')
                        table_emp()

                        print('Do you want to add another employee?')
                        print('1. Yes')
                        print('2. No')
                        add_more_emp = input('Choose the option between 1 or 2: ')
                        if add_more_emp == '1':
                            break  
                        elif add_more_emp == '2':
                            list_menu()
                        else:
                            print('Invalid input! Please enter the option between 1 or 2.')

        elif input_add == '2':
            print('Employee addition cancelled')
            break
        else:
            print('Invalid input! Please enter the option between 1 or 2.') 

# CRUD 3: Update - Update Employee Data
def update_emp():
    table_emp()
    print('\n')
    search_id = input('Enter the Employee ID you want to update: ').upper()

    found_emp = False

    for u in range(len(emp_id)):
        if emp_id[u] == search_id:
            found_emp = True
            print(f'\nEmployee found: {first_name[u]} {last_name[u]} with ID {emp_id[u]}\n')
            while True:
                print("Are you sure you want to update this employee's data?")
                print('1. Yes')
                print('2. No')
                valid_update = input('Choose an option between 1 or 2: ')
                if valid_update == '1':
                    print(f'You are updating the data for employee {first_name[u]} {last_name[u]} with ID {emp_id[u]}')
                    while True:
                        print('Please choose the data you want to update:')
                        print('1. First Name')
                        print('2. Last Name')
                        print('3. Position')
                        print('4. Department')
                        print('5. Salary')
                        print('6. Status')
                        print('7. Birthdate')
                        print('8. Finish Update')
                        input_menu_update = input('Enter menu number (1-8): ')

                        if input_menu_update == '1':
                            input_first_name_update = input('Enter new first name: ').capitalize()
                            first_name[u] = input_first_name_update
                        elif input_menu_update == '2':
                            input_last_name_update = input('Enter new last name: ').capitalize()
                            last_name[u] = input_last_name_update
                        elif input_menu_update == '3':
                            input_update_position = input('Enter new position: ').title()
                            position[u] = input_update_position
                        elif input_menu_update == '4':
                            input_update_department = input('Enter new department: ').title()
                            department[u] = input_update_department
                        elif input_menu_update == '5':
                            input_update_salary = int(input('Enter new salary (ex. 7000000): '))
                            salary[u] = input_update_salary
                        elif input_menu_update == '6':
                            input_update_status = input('Enter new status: ')
                            emp_status[u] = input_update_status 
                        elif input_menu_update == '7':
                            input_update_birthdate = input('Enter new birthdate (format YYYY-MM-DD): ')
                            birthdate[u] = input_update_birthdate 
                        elif input_menu_update == '8':
                            print('\nEmployee data has been successfully updated!')
                            print('\nUpdated employee data:\n')
                            table_emp()
                            list_menu()
                            return
                        else:
                            print('Invalid menu! Choose a number between 1-8.')
                elif valid_update == '2':
                    print('Employee update cancelled.')
                    return
                else:
                    print('Invalid input. Please enter 1 or 2.')

    if not found_emp:
        print('Employee ID not found. Please check and try again.')


# CRUD 4: Delete - Delete Employee Data
def delete_emp():
    table_emp()
    input_del = input('Please enter the Employee ID you want to delete: ').upper()
    
    for deleted in range(len(emp_id)):
        if emp_id[deleted] == input_del:
            deleted_id = emp_id[deleted]
            deleted_first_name = first_name[deleted]
            deleted_last_name = last_name[deleted]
            while True:
                print(f'Are you sure you want to delete employee {deleted_first_name} {deleted_last_name} with ID {deleted_id}?')
                print('1. Yes')
                print('2. No')
                valid_del = input('Choose an option between 1 or 2: ')
                if valid_del == '1':
                    del first_name[deleted]
                    del last_name[deleted]
                    del position[deleted]
                    del department[deleted]
                    del salary[deleted]
                    del emp_status[deleted]
                    del birthdate[deleted]
                    del emp_id[deleted]
                    print(f'Employee data for {deleted_first_name} {deleted_last_name} with ID {deleted_id} has been deleted.')
                    table_emp()
                    return 
                elif valid_del == '2':
                    print('Employee deletion cancelled.')
                    return
                else:
                    print('Invalid input. Please enter an option between 1 or 2.')
    else:
        print('Employee ID not found. Please check and try again.')

greetings()
list_menu()