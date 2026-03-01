class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"The {self.brand} {self.model} is now going at {self.speed} km/h")

    def brake(self):
        if self.speed > 0:
            self.speed -= 10
            print(f"Slowing down. The {self.brand} {self.model} is now going at {self.speed} km/h")
        else:
            print(f"The {self.brand} {self.model} is already stopped.")
    
    def display_info(self):
        print(f"Car Information:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Current Speed: {self.speed} km/h")

my_car = Car("Lynk & Co", "01", 2025, "Black")
print("Car information")
my_car.display_info()
print()

print("Accelerating the car:")
my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
print()

print("Braking the car:")
my_car.brake()
my_car.brake()

