class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

    def promote(self):
        self.grade += 1
        print(f"{self.name} has been promoted to grade {self.grade}!")

student1 = Student("Alice", 15, 10)
student2 = Student("Bob", 16, 9)

print("Student 1 Information:")
student1.display_info()
print()

print("Student 2 Information:")
student2.display_info()
print()

print("Promoting Alice:")
student1.promote()
print()