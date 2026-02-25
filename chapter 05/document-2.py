# More comprehensive example of abstract methods in a real-world scenario using Abstract Base Classes (ABC) in Python
from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, title):
        self.title = title


    @abstractmethod
    def save(self):
        pass


    @abstractmethod
    def load(self):
        pass


    @abstractmethod
    def export(self, format):
        pass


    def display_info(self):
        print(f"Document Title: {self.title}")


class WordDocument(Document):
    def __init__(self, title, content):
        super().__init__(title)
        self.content = content

    def save(self):
        print(f"Saving Word document '{self.title}' to Word format")

    def load(self):
        print(f"Loading Word document '{self.title}' from Word format")

    def export(self, format):
        print(f"Exporting Word document '{self.title}' in {format} format")

   
class SpreadsheetDocument(Document):
    def __init__(self, title, rows, columns):
        super().__init__(title)
        self.rows = rows
        self.columns = columns

    def save(self):
        print(f"Saving Spreadsheet document '{self.title}' with {self.rows} rows and {self.columns} columns to Spreadsheet format")

    def load(self):
        print(f"Loading Spreadsheet document '{self.title}' from Spreadsheet format")

    def export(self, format):
        print(f"Exporting Spreadsheet document '{self.title}' in {format} format")


class PresentationDocument(Document):
    def __init__(self, title, slides):
        super().__init__(title)
        self.slides = slides

    def save(self):
        print(f"Saving Presentation document '{self.title}' with {self.slides} slides to Presentation format")

    def load(self):
        print(f"Loading Presentation document '{self.title}' from Presentation format")

    def export(self, format):
        print(f"Exporting Presentation document '{self.title}' in {format} format")


# Creating instances of the document classes
word_doc = WordDocument("Annual Report", "This is the content...")
spreadsheet_doc = SpreadsheetDocument("Sales Data", 100, 10)
presentation_doc = PresentationDocument("Project Update", 20)

# Working with documents
documents = [word_doc, spreadsheet_doc, presentation_doc]

for doc in documents:
    doc.display_info()
    doc.save()
    doc.load()
    doc.export("PDF")
    print()  # Add a newline for better readability between documents