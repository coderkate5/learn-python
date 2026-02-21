# two parent classes and one child class that inherits from both parents
class Student:
    def __init__(self, student_id, major):
        self.student_id = student_id
        self.major = major

    def study(self):
        print(f"Student {self.student_id} is studying {self.major}")

    def attend_class(self):
        print(f"Student {self.student_id} is attending class")

class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def work(self):
        print(f"Employee {self.employee_id} is working as a {self.position}.")

    def attend_meeting(self):
        print(f"Employee {self.employee_id} is attending a work meeting.")

class WorkingStudent(Student, Employee):
    def __init__(self, name, student_id, major, employee_id, position):
        self.name = name
        Student.__init__(self, student_id, major)
        Employee.__init__(self, employee_id, position)

    def balance_life(self):
        print(f"Name: {self.name} is balancing working as a {self.position} and studying {self.major}.")
        
person1 = WorkingStudent("Alice Brown", "S123", "Computer Science", "E456", "Software Engineer")
print(f"Name: {person1.name}")
person1.study()  # Output: Student S123 is studying Computer Science
person1.work()  # Output: Employee E456 is working as a Software Engineer.
person1.balance_life()  # Output: Name: Alice is balancing working as a Software Engineer and studying Computer Science