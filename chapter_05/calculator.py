# Method overriding done wrongly
class Calculator:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c
    
calc = Calculator()
print("Calling the add method with two arguments:")
#print(calc.add(5, 10))  # This will raise a TypeError because the first add method is overridden by the second one. Comment out this line to see the correct output of the second add method.
print("Calling the add method with three arguments:")
print(calc.add(5, 10, 15))  # This will work and output 30