# Second example of duck typing in Python
class TextDocument:
    def __init__(self, file_name):
        self.file_name = file_name

    def open(self):
        print(f"Opening text document: {self.file_name}")

    def display (self):
        print(f"Displaying plain text content")

class PDFDocument:
    def __init__(self, file_name):
        self.file_name = file_name

    def open(self):
        print(f"Opening PDF document: {self.file_name}")

    def display(self):
        print(f"Displaying PDF in PDF viewer")


class HTMLDocument:
    def __init__(self, file_name):
        self.file_name = file_name

    def open(self):
        print(f"Opening HTML document: {self.file_name}")

    def display(self):
        print(f"Displaying HTML in browser")


# Function that workss with any document
def process_document(document):
    document.open()
    document.display()
    print()

# Creating instances of different document types
text_doc = TextDocument("report.txt")
pdf_doc = PDFDocument("manual.pdf")
html_doc = HTMLDocument("webpage.html")

# Processing each document using the same function
process_document(text_doc)
process_document(pdf_doc)
process_document(html_doc)
