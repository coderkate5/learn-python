# Example of the magic method called the str Method
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return self.title + " by " + self.author + " (" + str(self.pages) + " pages)."
    

book1 = Book("Python Programming", "John Doe", 325)
book2 = Book("Data Science Basics", "Jane Smith", 429)

print(book1)
print(book2)