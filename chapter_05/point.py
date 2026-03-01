# Example of operator overloading in Python using the Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

    def display_info(self):
        print(f"Point({self.x}, {self.y})")

# Creating two Point objects
point1 = Point(2, 3)
point2 = Point(4, 5)

# Displaying the original points
print("Original Points:")
point1.display_info()  # Output: Point(2, 3)
point2.display_info()  # Output: Point(4, 5)

# Adding the two points using the overloaded + operator
result_point = point1 + point2

# Displaying the result of the addition
print("Result of adding point1 and point2:")
result_point.display_info()  # Output: Point(6, 8)

