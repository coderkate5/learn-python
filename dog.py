class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Buddy", 3)
dog1 = Dog("Max", 5)
dog2 = Dog("Luna", 2)
dog3 = Dog("Charlie", 4)

print("My dog's name is " + my_dog.name + ". He is " + str(my_dog.age) + " years old.")
    
print("Dog 1 is named "+ dog1.name + " and is " + str(dog1.age) + " years old.")
print("Dog 2 is named "+ dog2.name + " and is " + str(dog2.age) + " years old.")
print("Dog 3 is named "+ dog3.name + " and is " + str(dog3.age) + " years old.")

