# Advanced OOP Concepts in Python: Composition
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print("Engine started with "+ str(self.horsepower) + " horsepower.")


class Wheel:
    def __init__(self, size):
        self.size = size

    def rotate(self):
        print("Wheel of size " + str(self.size) + " inches is rotating.")


class Car:
    # The Car class doesn't inherit from Engine or Wheel. Instead it contains instances of these classes. The car "has an" Engine and "has" Wheels. This is composition.
    # Inheritance would be wrong here because a car is not a type of Engine or a type of Wheel.
    def __init__(self, engine_hp, wheel_size):
        self.engine = Engine(engine_hp)
        self.wheels = [Wheel(wheel_size) for i in range(4)]

    def drive(self):
        self.engine.start()
        for wheel in self.wheels:
            wheel.rotate()
        print("Car is now driving.")


#create object
car = Car(200, 22)
car.drive()
