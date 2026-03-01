class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, number):    
        self.result += number
    
    def subtract(self, number):
        self.result -= number
    
    def get_result(self):
        return self.result

calc = Calculator()
calc.add(10)
calc.add(5)
calc.subtract(3)
print(f"Result: {calc.get_result()}")

