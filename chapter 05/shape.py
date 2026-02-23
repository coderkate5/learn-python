# Hierarchical inheritance example
class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2
    

class Rectangle(Shape):
    def __init__(self,  width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
        


# Creating objects of the Circle and Rectangle classes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calling the area method on each object
print(f"Area of the circle: {circle.area()}")  # Output: Area of the circle: 78.53975
print(f"Area of the rectangle: {rectangle.area()}")  # Output: Area of 