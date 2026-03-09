# Using a class method to create alternative constructors. This is called the factory method pattern.
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        day,month,year = date_string.split('-')
        return cls(int(day), int(month), int(year))
    
    def display(self):
        print(str(self.day) + "-" + str(self.month) + "-" + str(self.year))


date1 = Date(15, 8, 2024)
date1.display()

date2 = Date.from_string("20-12-2024")
date2.display()