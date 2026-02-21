class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")

    def work(self):
        print(f"{self.name} is working")

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.department = department

    def conduct_meeting(self):
        print(f"Manager {self.name} is conducting a meeting with the {self.department} team.")


manager1 = Manager("Sarah Johnson", "M101", 75000, "Marketing")
manager1.display_info()
manager1.work()
manager1.conduct_meeting()

