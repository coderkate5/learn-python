# Another example of static methods in Python.
# the conversion functions do not need to access any object data. They take a number, perform calculations and return a result.
# Because they are both related to the concept of temperature conversion it makes sense to group them in a class.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return round(fahrenheit, 2)
    

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return round(celsius, 2)
    

# usage, again we are directly calling the methods on the class instead of on objects.
temp_f1 = TemperatureConverter.celsius_to_fahrenheit(8)
temp_f2 = TemperatureConverter.celsius_to_fahrenheit(25)
temp_c1 = TemperatureConverter.fahrenheit_to_celsius(77)
temp_c2 = TemperatureConverter.fahrenheit_to_celsius(101)

print("8 degrees Celsius is ", temp_f1, " Fahrenheit")
print("25 degrees Celsius is ", temp_f2, " Fahrenheit")
print("77 degrees Fahrenheit is ", temp_c1, " Celsius")
print("101 degrees Fahrenheit is ", temp_c2, " Celsius")
