print('---Python OOP Project: Employee Management System---')

class Employee:
    def __init__(self, employee_id=0, name="Unknown", age=0, salary=0):
        self.__employee_id = employee_id
        self.name = name
        self.age = age
        self.__salary = salary
    def show_details(self):
        print("Employee Details:")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Salary :", self.get_salary())
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary
    def display(self):
        print("Person created with Name:", self.name,
          "and Age:", self.age)
    def __del__(self):
        print("Employee object deleted.")

class Developer(Employee):
    def __init__(self, employee_id, name, age, salary, language):
        super().__init__(employee_id, name, age, salary)
        self.language = language

    def display(self):
        print("Developer created with Name:", self.name,"Age:", self.age ,"ID:", self.get_employee_id(),"Salary:", self.get_salary(),"and Language:", self.language)
    def show_details(self):
        print("Developer Details:")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Salary :", self.get_salary())
        print("Language :", self.language)

class Manager(Employee):
    def __init__(self, employee_id, name, age, salary,Department):
        super().__init__(employee_id, name, age, salary)
        self.department = Department

    def display(self):
        print("Manager created with Name:", self.name,"Age:", self.age ,"ID:", self.get_employee_id(),"Salary:", self.get_salary(),"and Department:", self.department)
    def show_details(self):
        print("Manager Details:")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Salary :", self.get_salary())
        print("Department :", self.department)
e = None
d = None
m = None
while True:
    print("Choose an operation:")
    print("1.Create a Person")
    print("2.Create an employee")
    print("3.Create a Manager")
    print("4.Show Details")
    print("5.Exit")
        
    choice = int(input("Please Enter Your choice: "))

    if choice == 1:
        eid = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))

        e = Employee(eid, name, age, salary)
        e.display()
        print("-----Choose another operation-----")
    elif choice == 2:
        eid = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        lang = input("Enter Programming Language: ")

        d = Developer(eid, name, age, salary, lang)
        d.display()
    elif choice == 3:
        eid = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        dept = input("Enter Department: ")

        m = Manager(eid, name, age, salary, dept)
        m.display()
    elif choice == 4:
        print("Choose Details to Show")
        print("1.Person")
        print("2.Employee")
        print("3.Manager")
        option = int(input("Enter your option: "))
        if option == 1:
           if e:
            e.show_details()
           else:
            print("No employee record found.")
        if option==2:
           if d:
            d.show_details()
           else:
            print("No Developer record found.")
        if option==3:
           if m:
            m.show_details()
           else:
            print("No Manager record found.")
        
    elif choice == 5:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!")