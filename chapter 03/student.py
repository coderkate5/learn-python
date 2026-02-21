# This code defines a Student class with private attributes for name, age, and grade. It includes getter and setter methods for each attribute, along with validation to ensure that the name is a non-empty string and the age is a whole number between 5 and 100. The class also has methods to display student information and promote the student to the next grade. Finally, two student instances are created, their information is displayed, and one student is promoted.
class Student:
    def __init__(self, name, age, grade):
        self.__name = name
        self.__age = age
        self.__grade = grade

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0: # isinstance(name, str) checks if the provided name is a string, and len(name) > 0 ensures that the name is not an empty string. If both conditions are met, the name is updated; otherwise, an error message is printed.
            self.__name = name
        else:
            print("Invalid name. Please provide a non-empty string.")

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and 5 <= age <= 100: # This condition checks if the provided age is an integer and falls within a reasonable range (between 5 and 100). If the age is valid, it is updated; otherwise, an error message is printed.
            self.__age = age
        else:
            print("Age must be a whole number between 5 and 100.")

    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, grade):
        valid_grades = ['A', 'B', 'C', 'D', 'E', 'F'] + list(range(1, 13)) # This list defines the valid grade levels for students. The setter method checks if the provided grade is in this list before updating the grade attribute. If the grade is valid, it is updated; otherwise, an error message is printed.
        if grade in valid_grades:
            self.__grade = grade
        else:
            print("Grade must be a valid letter grade (A-F).")
                  

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    
student1 = Student("Tom", 15, 'A')

print("Student 1 Information:")
student1.display_info()
print()
student1.name = "Tom Sanderson"
student1.age = 16
student1.grade = 'B'
print("Student 1 Information:")
student1.display_info()
print()
print("Attempting invalid updates:")
student1.name = ""
student1.age = 150
student1.grade = 'G'
print()