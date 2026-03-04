# Example of using static methods in Python.
class Product:
    discount_rate = 0.1

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        discount = self.price * Product.discount_rate
        return self.price - discount
    
    @classmethod
    def change_discount_rate(cls, new_rate):
        cls.discount_rate = new_rate
        print("Discount rate changed to ", new_rate)
        print()

    def display_info(self):
        print("Product: ", self.name)
        print("Original price: ", self.price)
        print("Discounted price: ", self.get_discounted_price())
        print()


# usage examples
product1 = Product("Laptop", 2250)
product2 = Product("Phone", 1449)
product1.display_info()
product2.display_info()

Product.change_discount_rate(0.2)
product1.display_info()
product2.display_info()