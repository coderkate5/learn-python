# Another example of abstraction using Abstract Base Classes (ABC) in Python
# in this example, we define a class that does not implement all abstract methods
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Fish(Animal):
    def move(self):
        return "The fish is swimming!"
# The Fish class does not implement the sound method, so it is still considered an abstract class and cannot be instantiated
    

# Trying to create an instance of the Fish class will raise a TypeError because it has not implemented all abstract methods
my_fish = Fish()  # This will raise a TypeError: Can't instantiate abstract class Fish with abstract methods sound
