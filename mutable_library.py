class Library:
    """Represents a library."""
    
    def __init__(self, books=None):
        """Initialise the books."""
        if books:
            self.books = books
        else:
            self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)


london = Library(["The surrender experiment"])
london.add_book("The Clean Coder")
london.add_book("War and Peace")

print(london.books)


new_york = Library()
new_york.add_book("The power of now")

print(new_york.books)

