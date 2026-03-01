# Class Variables vs Instance Variables a demonstration.
# Instance Variables belong to a specific object.
# Class Variables belong to the class itself and therefore to all objects of that class.
class Student:
    school_name = "Atlanta High School"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print("Name: " + self.name)
        print("Grade: " + str(self.grade))
        print("School: " + Student.school_name)
        print()


# create objects
student1 = Student("Shaniqua", 10)
student2 = Student("Brian", 12)

student1.display_info()
student2.display_info()

Student.school_name = "New York City High School"

print("After changing the school name:")
student1.display_info()
student2.display_info()