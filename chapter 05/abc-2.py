# Another example of using the ABC module in a more complex e-commerce system
from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    
    @abstractmethod
    def calculate_final_price(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    def display_product(self):
        print(f"Product: {self.name}")
        print(f"Description: {self.get_description()}")
        print(f"Final Price: ${self.calculate_final_price():.2f}")


class Book(Product):
    def __init__(self, name, base_price, author, pages):
        super().__init__(name, base_price)
        self.author = author
        self.pages = pages

    def calculate_final_price(self):
        return self.base_price * 0.9
    
    def get_description(self):
        return f"A book by {self.author} with {self.pages} pages."
    

class Electronics(Product):
    def __init__(self, name, base_price, warranty_years):
        super().__init__(name, base_price)
        self.warranty_years = warranty_years

    def calculate_final_price(self):
        warranty_cost = self.warranty_years * 20
        return self.base_price + warranty_cost
    
    def get_description(self):
        return f"Electronic item with {self.warranty_years} years warranty."
    

class Clothing(Product):
    def __init__(self, name, base_price, size, material):
        super().__init__(name, base_price)
        self.size = size
        self.material = material

    def calculate_final_price(self):
        return self.base_price * 0.85
    
    def get_description(self):
        return f"Clothing item in Size {self.size} made of {self.material}."
    

# creating objects
book = Book("Pachinko", 44.95, "Min Jin Lee", 496)
laptop = Electronics("Macbook Pro", 2000, 3)
dress = Clothing("Summer dress", 78.99, "M", "Denim")

products = [book, laptop, dress]

for product in products:
    product.display_product()
    print()