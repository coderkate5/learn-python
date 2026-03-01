# Example of method overriding in a vehicle class hierarchy. The child class (Car) overrides the method of the parent class (Vehicle) to provide a specific implementation.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"The engine of the {self.brand} vehicle is starting with a standard ignition.")
    
    def stop_engine(self):
        print(f"The engine of the {self.brand} vehicle is stopping.")

class ElectricCar(Vehicle):
    def __init__(self, brand, battery_capacity):
        super().__init__(brand)
        self.battery_capacity = battery_capacity

    def start_engine(self):
        print(f"The electric engine of the {self.brand} car is starting silently with battery power.")

    def display_battery_info(self):
        print(f"The {self.brand} car has a battery capacity of {self.battery_capacity} kWh.")

# Example usage
regular_car = Vehicle("Toyota")
regular_car.start_engine()  # Output: The engine of the Toyota vehicle is starting with a standard ignition.
regular_car.stop_engine()   # Output: The engine of the Toyota vehicle is stopping.

print()  # Just for separation of output

electric_car = ElectricCar("Tesla", 100)
electric_car.start_engine()  # Output: The electric engine of the Tesla car is starting silently with battery power.
electric_car.stop_engine()   # Output: The engine of the Tesla vehicle is stopping.
electric_car.display_battery_info()  # Output: The Tesla car has a battery capacity of 100 kWh.
