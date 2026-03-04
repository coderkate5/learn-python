# Using static methods in python. Static methods do not take self as a parameter. 
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    

    @staticmethod
    def multiply(a, b):
        return a * b
    

    @staticmethod
    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False
        

# You can use static methods directly on the class name. 
# We do not first need to create an object.
result1 = MathOperations.add(18, 22)
result2 = MathOperations.multiply(4, 90)
result3 = MathOperations.is_even(10)
result4 = MathOperations.is_even(75)

print("The sum of 18 and 22 = ", result1)
print("4 times 90 = ", result2)
print("Is 10 an even number? ", result3)
print("Is 75 an even number? ", result4)
