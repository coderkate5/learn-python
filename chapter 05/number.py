# More comprehensive example of operator overloading in Python
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        return ComplexNumber(new_real, new_imaginary)

    def __sub__(self, other):
        new_real = self.real - other.real
        new_imaginary = self.imaginary - other.imaginary
        return ComplexNumber(new_real, new_imaginary)

    def __mul__(self, other):
        new_real = self.real * other.real - self.imaginary * other.imaginary
        new_imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(new_real, new_imaginary)

    def __str__(self):
        # This method is used to define how the object should be represented as a string
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"
        

# Creating two ComplexNumber objects
num1 = ComplexNumber(3, 2)
num2 = ComplexNumber(1, 4)

# Using overloaded operators to perform arithmetic operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

# Displaying the results
print(f"num1: {num1}")  # Output: num1: 3 + 2i
print(f"num2: {num2}")  # Output: num2: 1 + 4i
print(f"Sum: {sum_result}")  # Output: Sum: 4 + 6i
print(f"Difference: {difference_result}")  # Output: Difference: 2 - 2i
print(f"Product: {product_result}")  # Output: Product: -5 + 14i


