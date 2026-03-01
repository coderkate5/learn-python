class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
       
    def calculate_area(self):
        area = self.length * self.width
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter
    
    def display_info(self):
        print(f"Rectangle with length {self.length} and width {self.width}")
        print(f"Area: {self.calculate_area()}")
        print(f"Perimeter: {self.calculate_perimeter()}")   


rect1 = Rectangle(10, 5)
rect1.display_info()

print()

rect2 = Rectangle(7, 3)
rect2.display_info()

print()
