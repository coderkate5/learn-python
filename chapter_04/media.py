# Media Library System
class MediaItem:
    def __init__(self, title, creator, year):
        self.title = title
        self.creator = creator
        self.year = year
        self.is_borrowed = False

    def display_info(self):
        print(f"Item: {self.title} by {self.creator} ({self.year})")
        print(f"Status: {'Borrowed' if self.is_borrowed else 'Available'}")

    def borrow_item(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")

    def return_item(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have returned '{self.title}'.")
        else:
            print(f"Error: '{self.title}' was not borrowed.")

class Book(MediaItem):
    def __init__(self, title, author, year, pages, isbn):
        super().__init__(title, author, year)
        self.pages = pages
        self.isbn = isbn

    def display_info(self):
        super().display_info()
        print(f"Pages: {self.pages}, ISBN: {self.isbn}")

class Movie(MediaItem):
    def __init__(self, title, director, year, duration, rating):
        super().__init__(title, director, year)
        self.duration = duration
        self.rating = rating

    def display_info(self):
        super().display_info()
        print(f"Duration: {self.duration} minutes Rating: {self.rating}/10")

class Magazine(MediaItem):
    def __init__(self, title, publisher, year, issue_number):
        super().__init__(title, publisher, year)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}.")

# Example usage
book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 180, "978-0743273565")
book.display_info()
print()  # Just for separation of output
book.borrow_item()
print()  # Just for separation of output
book.borrow_item()
print()
print()  

movie = Movie("Inception", "Christopher Nolan", 2010, 148, 8.8)
movie.display_info()
print()  # Just for separation of output

magazine = Magazine("National Geographic", "National Geographic Society", 2021, 5)
magazine.display_info()
