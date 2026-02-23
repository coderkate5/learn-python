class UniversityMember:
    def __init__(self, name, age, member_id):
        self.name = name
        self.age = age
        self.member_id = member_id

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Member ID: {self.member_id}"
    
class Student(UniversityMember):
    def __init__(self, name, age, member_id, major, year):
        super().__init__(name, age, member_id)
        self.major = major
        self.year = year
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)
        print(f"{self.name} has enrolled in {course}.")

    def display_info(self):
        base_info = super().display_info()
        print(f"{base_info}, Major: {self.major}, Year: {self.year}")
        print(f"Courses: {', '.join(self.courses) if self.courses else 'No courses enrolled.'}")
    
class Professor(UniversityMember):
    def __init__(self, name, age, member_id, department, specialization):
        super().__init__(name, age, member_id)
        self.department = department
        self.specialization = specialization
        self.teaching_courses = []

    def assign_course(self, course):
        self.teaching_courses.append(course)
        print(f"Professor {self.name} is teaching {course} in the {self.department} department.")

    def display_info(self):
        base_info = super().display_info()
        print(f"{base_info}, Department: {self.department}, Specialization: {self.specialization}")
        print(f"Teaching Courses: {', '.join(self.teaching_courses) if self.teaching_courses else 'No courses assigned.'}")


# Example usage
student1 = Student("Alice Johnson", 22, "S1234501", "Computer Science", 3)
student1.enroll_course("Data Structures")
student1.enroll_course("Algorithms")
student1.display_info()
print()  # Just for separation of output
professor1 = Professor("Dr. Robert Brown", 47, "P678901", "Computer Science", "Artificial Intelligence")
professor1.assign_course("Artificial Intelligence 101")
professor1.assign_course("Neural Networks")
professor1.display_info()
