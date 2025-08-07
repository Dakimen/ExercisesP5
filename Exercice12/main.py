"""This file contains exercise 12."""


class Book:
    """Book class.

    Manages core book data.

    Attributes:
    title (string): This book's title.
    author (string): This book's author.
    year (string): This book's publication year.

    This class has no methods.
    """

    def __init__(self, title, author, year):
        """Instantiate book class.

        Args:
        title (string): This book's title.
        author (string): This book's author.
        year (string): This book's publication year.
        """
        self.title = title
        self.author = author
        self.year = year


class Library:
    """Library class.

    This class manages library data.

    Attributes:
    books (list): List containing books available at the library.
    borrow_books (list): List containing books currently borrowed.

    Methods:
    add_book(book): Add a book to the library.
    remove_book(book_title):
    Remove a book from the library using it's title as argument.
    borrow_book(book_title):
    Borrow book from the library using it's title as argument.
    return_book(book_title):
    Return borrowed book from the library using it's title as argument.
    available_books():
    Return a list of titles of books contained in the library.
    borrowed_books():
    Return a list of titles of currently borrowed books.
    """

    def __init__(self):
        """Create a Library instance."""
        self.books = []
        self.borrow_books = []

    def add_book(self, book):
        """Add a book to the library.

        Args:
        book (Book): book to add to the library.
        """
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("book attribute must be a Book instance.")

    def remove_book(self, book_title):
        """Remove a book from the library using it's title as argument."""
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return print("Book removed successfully.")
        raise ValueError(f"Book with title '{book_title}' not found.")

    def borrow_book(self, book_title):
        """Borrow book from the library using it's title as argument."""
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrow_books.append(book)
                return print("Book borrowed successfully.")
        return ValueError(f"Book with title '{book_title}' not found.")

    def return_book(self, book_title):
        """Return a borrowed book to the library.

        Args:
        book_title (string): target book's title.
        """
        for book in self.borrow_books:
            if book.title == book_title:
                self.borrow_books.remove(book)
                self.books.append(book)
                return print("Book returned successfully.")
        return ValueError(
            f"Book with title '{book_title}' not found in borrowed list."
            )

    def available_books(self):
        """Return a list of titles of books contained in the library."""
        print("Books currently available:")
        for book in self.books:
            print(f"\nTitle: {book.title}")
        print("")

    def borrowed_books(self):
        """Return a list of titles of currently borrowed books."""
        print("Borrowed books:")
        for book in self.borrow_books:
            print(f"\nTitle: {book.title}")
        print("")
