# Arithmetic Magic Methods demonstration
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append({"item":item, "price":price})

    def __add__(self, other):
        new_cart = ShoppingCart()
        new_cart.items = self.items + other.items
        return new_cart
    
    def get_total(self):
        total = 0
        for item in self.items:
            total = total + item["price"]
        return total
        
    def __str__(self):
        result = "Shopping cart with " + str(len(self.items)) + " items:\n"
        for item in self.items:
            result = result + item["item"] + ": €" + str(item["price"]) + "\n"
        result = result + "Total €" + str(self.get_total())
        return result
        

cart1 = ShoppingCart()
cart1.add_item("Apple", 1.5)
cart1.add_item("Orange", 1.75)

cart2 = ShoppingCart()
cart2.add_item("Banana", 0.75)
cart2.add_item("Grape", 3.5)

combined_cart = cart1 + cart2 # here we are using the + operator and the class then defaults to the __add__ method because it is defined.
print(combined_cart)
