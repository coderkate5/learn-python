# Example of multilevel inheritance
class LivingBeing:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing.")

    def exist(self):
        print(f"{self.name} exists in the world.")


class Animal(LivingBeing):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def move(self):
        print(f"{self.name} the {self.species} is moving.")

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} is barking.")

# Example usage
dog = Dog("Max", "Canine", "Golden Retriever")
dog.exist()
dog.breathe()  # Output: Buddy is breathing.
dog.move()     # Output: Buddy is moving.
dog.bark()     # Output: Buddy is barking.