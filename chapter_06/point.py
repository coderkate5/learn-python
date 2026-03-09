# The repr Method. Similar to the str Method but meant to provide a more detailed, unambiguous representation of the object. 
# Typically used for debugging.
# If __str__ is not defined, Python will use __repr__ when you print an object
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point at (" + str(self.x) + ", " + str(self.y) + ")."
    
    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")."
    
point = Point(3,4)
print(point)
print(repr(point))