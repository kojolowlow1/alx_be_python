class Book:
    """Represents a book with title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """Manages a collection of Book objects."""

    def __init__(self):
        self._books = []  # private list of book objects

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        # If no book found, do nothing

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        # If no book found, do nothing

    def list_available_books(self):
        """Print all books that are not checked out."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
