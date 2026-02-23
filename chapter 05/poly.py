# Short example of polymorphism in Python
class Dog:  
    def sound(self):  
        return "Woof! Woof!"  
    
class Cat:  
    def sound(self):  
        return "Meow! Meow!"  
    
class Cow:  
    def sound(self):  
        return "Moo! Moo!"
    
def make_sound(animal):  
    print(animal.sound())
    
# Creating objects  
my_dog = Dog()  
my_cat = Cat()  
my_cow = Cow()

# Calling the sound method on each object
print(my_dog.sound())  # Output: Woof! Woof!
print(my_cat.sound())  # Output: Meow! Meow!
print(my_cow.sound())  # Output: Moo! Moo!
print()

# Using polymorphism to call the same method on different objects
make_sound(my_dog)  # Output: Woof! Woof!
make_sound(my_cat)  # Output: Meow! Meow!
make_sound(my_cow)  # Output: Moo! Moo!
