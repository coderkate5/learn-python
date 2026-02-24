# add money amounts together, compare them, and display them nicely.
class Money:
    def __init__(self, amount):
        self.amount = amount
      
    def __add__(self, other):
        return Money(self.amount + other.amount)
    
    def __sub__(self, other):
        return Money(self.amount - other.amount)
    
    def __eq__(self, other):
        return self.amount == other.amount
    
    def __lt__(self, other):
        return self.amount < other.amount
    
    def __gt__(self, other):
        return self.amount > other.amount

    def __str__(self):
        return f"${self.amount:.2f}"
    
# Creating Money objects
price1 = Money(50.75)
price2 = Money(30.25)
price3 = Money(50.75)

# Using overloaded operators to perform operations
total_price = price1 + price2
total_price2 = price1 + price2 + price3
price_difference = price1 - price2

# Displaying the results
print(f"Price 1: {price1}")  # Output: Price 1: $50.75
print(f"Price 2: {price2}")  # Output: Price 2: $30.25
print(f"Price 3: {price3}")  # Output: Price 3: $50.75
print(f"Total Price (price1 + price2): {total_price}")  # Output: Total Price: $81.00
print(f"Total Price (price1 + price2 + price3): {total_price2}")  # Output: Total Price: $131.75
print(f"Price Difference (price1 - price2): {price_difference}")  # Output: Price Difference: $20.50
print(f"Is Price 1 equal to Price 3? {price1 == price3}")  # Output: Is Price 1 equal to Price 3? True
print(f"Is Price 1 less than Price 2? {price1 < price2}")  # Output: Is Price 1 less than Price 2? False
print(f"Is Price 1 greater than Price 2? {price1 > price2}")  # Output: Is Price 1 greater than Price 2? True