class Book:
    def __init__(self, title, author):
        """Initialize the base Book class."""
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook, inheriting from Book."""
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"{self.title} by {self.author} - EBook ({self.file_size}MB)"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook, inheriting from Book."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author} - Print Book ({self.page_count} pages)"


class Library:
    def __init__(self):
        """Library uses composition to store book objects."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books with their details."""
        for book in self.books:
            print(book)
