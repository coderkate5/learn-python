# Example of hybrid inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_personal_info(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying for exams.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, student_id, subject):
        Person.__init__(self, name, age)
        self.student_id = student_id
        self.subject = subject

    def assist(self):
        print(f"{self.name} is assisting in teaching {self.subject} while studying {self.subject}.")


# Example usage
ta = TeachingAssistant("Emily Davis", 25, "S789", "Mathematics")
ta.display_personal_info()  # Output: Hello, my name is Emily Davis and I am 25 years old.
ta.study()  # Output: Emily Davis is studying for exams.
ta.teach()  # Output: Emily Davis is teaching Mathematics.
ta.assist()  # Output: Emily Davis is assisting in teaching Mathematics while studying Mathematics.
