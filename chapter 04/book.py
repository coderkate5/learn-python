# Demonstrating constructor inheritance
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print(f"Book constructor created")

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

class Novel(Book):
    pass
    
class Textbook(Book):
    def __init__(self, title, author, subject, edition):
        super().__init__(title, author)  # Call the parent class constructor
        self.subject = subject
        self.edition = edition
        print(f"Textbook constructor created")

    def display_info(self):
        super().display_info()  # Call the parent class method to display title and author
        print(f"Subject: {self.subject}")


# Example usage
novel = Novel("To Kill a Mockingbird", "Harper Lee")
novel.display_info()  # Output: Title: To Kill a Mockingbird, Author: Harper Lee
print()  # Just for separation of output
print()  # Just for separation of output
textbook = Textbook("Introduction to Algorithms", "Thomas H. Cormen", "Computer Science", "3rd Edition")
textbook.display_info()

