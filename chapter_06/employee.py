# Another example of using Class Variables
class Employee:
    total_employees = 0

    def __init__(self, name, position):
        self.name = name
        self.position = position
        Employee.total_employees = Employee.total_employees + 1
    
    def display_info(self):
        print("Name: " + self.name)
        print("Position: " + self.position)


# create objects
emp1 = Employee("Alyssah", "Chief Executive Officer")
emp2 = Employee("Janiqua", "Head of HR")
emp3 = Employee("Virgillia", "Head of Finance")

print("Total employees: ", Employee.total_employees)