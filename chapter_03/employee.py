class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary
    
    def set_name(self, name):
        if len(name) > 0:
            self.__name = name
            print(f"Name has been updated to: {self.__name}")
        else:
            print("Name cannot be empty.")

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
            print(f"Salary has been updated to: ${self.__salary}")
        else:
            print("Salary cannot be negative.")

    def display_employee_info(self):
        print(f"Employee Name: {self.__name}")
        print(f"Employee Salary: ${self.__salary}") 

emp1 = Employee("Alice", 50000)
emp1.display_employee_info()
print(f"Getting name: {emp1.get_name()}")
emp1.set_name("Alice Smith")
emp1.set_salary(55000) 
emp1.set_salary(-1000)  # Attempt to set a negative salary, which should be rejected
emp1.display_employee_info()
