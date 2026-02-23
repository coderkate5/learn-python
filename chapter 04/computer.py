# using super() to call the parent class method
class Computer:
    def __init__(self, brand, processor):
        self.brand = brand
        self.processor = processor
        print(f"Computer constructer created")

    def display_specs(self):
        print(f"The {self.brand} computer has a {self.processor} processor.")

class Laptop(Computer):
    def __init__(self, brand, processor, battery_life):
        super().__init__(brand, processor)  # Call the parent class constructor
        self.battery_life = battery_life
        print(f"Laptop constructor created")

    def display_specs(self):
        super().display_specs()  # Call the parent class method to display brand and processor
        print(f"It has a battery life of {self.battery_life} hours.")


# Example usage
laptop = Laptop("Dell", "Intel i7", 10)
print()  # Just for separation of output
laptop.display_specs()  # Output: The Dell computer has a Intel i7 processor.

