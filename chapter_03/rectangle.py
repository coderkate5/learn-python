#demonstrating the use of property decorators to create a read only attribute
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property   # The @property decorator allows us to define a method that can be accessed like an attribute. In this case, we are defining a getter for the width attribute.
    def width(self):
        return self.__width
    
    @width.setter # The @width.setter decorator allows us to define a setter for the width attribute, which allows us to set the value of width while also performing validation to ensure that it is positive.
    def width(self, width):
        if width > 0:
            self.__width = width
        else:
            print("Width must be positive.")

    @property # The @property decorator is also used to define a getter for the height attribute, allowing us to access it like an attribute while keeping it private.
    def height(self):
        return self.__height
    
    @height.setter # The @height.setter decorator allows us to define a setter for the height attribute, which allows us to set the value of height while also performing validation to ensure that it is positive.
    def height(self, height):
        if height > 0:
            self.__height = height
        else:
            print("Height must be positive.")

    @property # The @property decorator is used to define a read-only attribute for the area of the rectangle. This allows us to calculate the area based on the current width and height without allowing it to be set directly.
    def area(self):
        return self.__width * self.__height


rect1 = Rectangle(5, 10)
print(f"Width: {rect1.width}")
print(f"Height: {rect1.height}")
print(f"Area: {rect1.area}")
rect1.width = 7
rect1.height = 12
print(f"Updated Width: {rect1.width}")
print(f"Updated Height: {rect1.height}")    
print(f"Updated Area: {rect1.area}")
rect1.width = -3  # Attempt to set an invalid width, which should be rejected
print(f"Width after invalid assignment: {rect1.width}")