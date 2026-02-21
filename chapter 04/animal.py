class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")   


my_dog = Dog("Buddy", 3)
my_dog.eat()  # Output: Buddy is eating
my_dog.sleep()  # Output: Buddy is sleeping
my_dog.bark()  # Output: Buddy is barking

