class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")




# Example of Public Access to attributes
person1 = Person("Katasha", 25)
person1.display_info()
print()

# We can access the name directly since it's public, but it's not recommended to do so
print(f"Accessing name directly: {person1.name}")
print()

# We are directly changing the age attribute without using any method, which is not recommended as it can lead to unintended consequences
person1.age = 28
print(f"Altered age: {person1.age}")
print()
