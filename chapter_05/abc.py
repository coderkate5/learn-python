# Using the ABC module
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


    @abstractmethod
    def start_engine(self):
        pass


    @abstractmethod
    def stop_engine(self):
        pass


    @abstractmethod
    def fuel_type(self):
        pass


    def display_info(self):
        print(f"{self.brand} {self.model}")
        print(f"Fuel type: {self.fuel_type()}")


class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with ignition key")

    def stop_engine(self):
        print("Car engine stopped")

    def fuel_type(self):
        return "Petrol"
    

class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def start_engine(self):
        print("Electric motor started with start-stop button")
    
    def stop_engine(self):
        print("Electric motor engine stopped")
    
    def fuel_type(self):
        return "Electric"
    
    def display_battery_info(self):
        print(f"Battery capacity: {self.battery_capacity} kWh.")


class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started with kick or button")
    
    def stop_engine(self):
        print("Motorcyle engine stopped")
    
    def fuel_type(self):
        return "Petrol"
    

# Create objects
car = Car("Toyota", "Camry")
electric_car = ElectricCar("Polestar", "Model 2", 85)
motorcycle = Motorcycle("Ducatti", "MY26")

# Use methods
print("Regular car: ")
car.display_info()
car.start_engine()
car.stop_engine()
print("\nElectric Car: ")
electric_car.display_info()
electric_car.display_battery_info()
electric_car.start_engine()
electric_car.stop_engine()
print("\nMotorcycle: ")
motorcycle.display_info()
motorcycle.start_engine()
motorcycle.stop_engine()