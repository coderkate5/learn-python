# Hierarchical inheritance example
class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f"The color of this shape is {self.color}")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius ** 2
        print(f"The area of the circle is {area}")

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(f"The area of the rectangle is {area}")

class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def area(self):
        area = 0.5 * self.base * self.height
        print(f"The area of the triangle is {area}")

# Example usage
circle = Circle("Red", 5)
circle.display_color()  # Output: The color of the shape is Red
circle.area()  # Output: The area of the circle is 78.5

rectangle = Rectangle("Blue", 4, 6)
rectangle.display_color()  # Output: The color of the shape is Blue
rectangle.area()  # Output: The area of the rectangle is 24

triangle = Triangle("Green", 3, 7)
triangle.display_color()  # Output: The color of the shape is Green
triangle.area()  # Output: The area of the triangle is 10.5
