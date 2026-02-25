# Example of duck typing in Python using a simple Duck class
class Duck:
    def swim(self):
        return "The duck is swimming!"
    
    def fly(self):
        return "The duck is flying!"


class Penguin:
    def swim(self):
        return "The penguin is swimming!"
    
    def fly(self):
        return "The penguin can't fly!"


class Airplane:
    def fly(self):
        return "The airplane is flying!"
    

# Function that takes an object and calls its swim and fly methods
def make_it_swim(duck_like_object):
    print(duck_like_object.swim())
    
def make_it_fly(duck_like_object):
    print(duck_like_object.fly())

# Creating instances of Duck, Penguin, and Airplane
duck = Duck()
penguin = Penguin()
airplane = Airplane()


# Using the make_it_fly function with different objects
print("Using the Duck object:")
make_it_fly(duck)
print("\nUsing the Penguin object:")
make_it_fly(penguin)
print("\nUsing the Airplane object:")
make_it_fly(airplane)


# Using the make_it_swim function with different objects
print("Using the Duck object:")
make_it_swim(duck)
print("\nUsing the Penguin object:")
make_it_swim(penguin)
print("\nUsing the Airplane object:")
make_it_swim(airplane)