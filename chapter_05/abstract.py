# Example of abstraction using Abstract Base Classes (ABC) in Python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"
    
    def move(self):
        return "The dog is running!"
    

class Bird(Animal):
    def sound(self):
        return "Chirp! Chirp!"
    
    def move(self):
        return "The bird is flying!"
    

# We cannot create an instance of the abstract class Animal, but we can create instances of its subclasses
# animal = Animal()  # This will raise an error because we cannot instantiate an abstract class

# Creating instances of Dog and Bird
dog = Dog()
bird = Bird()

# Using the methods of the Dog and Bird classes
print("Dog:")
print(dog.sound())  # Output: Woof! Woof!
print(dog.move())   # Output: The dog is running!
print("\nBird:")
print(bird.sound())  # Output: Chirp! Chirp!
print(bird.move())   # Output: The bird is flying!
