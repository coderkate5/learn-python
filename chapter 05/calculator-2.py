# Method overloading the correct way using default parameters
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c    

    
calc = Calculator()
print("Calling the add method with two arguments:")
print(calc.add(5, 10))  # This will work and output 15
print("Calling the add method with three arguments:")
print(calc.add(5, 10, 15))  # This will work and output 30