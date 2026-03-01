# Example of Aggregation in Python. It is similar to composition but the objects can exist independently of the container object.
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    
    def teach(self):
        print(self.name + " is teaching " + self.subject + ".")

class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(teacher.name + " has been added to " + self.school_name + ".")

    def conduct_classes(self):
        print("Classes at " + self.school_name + ":")
        for teacher in self.teachers:
            teacher.teach()


#create objects
teacher1 = Teacher("Mr. Smith", "Mathematics")
teacher2 = Teacher("Mrs. Johnson", "Science")
school = School("Atlanta High School")

school.add_teacher(teacher1)
school.add_teacher(teacher2)
school.conduct_classes()
