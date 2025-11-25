# book.py
# Name: YOUR_NAME_HERE
# Date: DATE_HERE
# Assignment: Library Inventory System - Book class

import json

class Book:
    def __init__(self, title: str, author: str, isbn: str, available: bool = True, borrow_count: int = 0):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.borrow_count = borrow_count  # for analytics

    def borrow(self):
        """Mark book as not available and increment borrow count."""
        if not self.available:
            raise ValueError(f"Book '{self.title}' (ISBN {self.isbn}) is already borrowed.")
        self.available = False
        self.borrow_count += 1

    def return_book(self):
        """Mark book as available."""
        if self.available:
            raise ValueError(f"Book '{self.title}' (ISBN {self.isbn}) is not currently borrowed.")
        self.available = True

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available,
            "borrow_count": self.borrow_count
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            title=d.get("title", ""),
            author=d.get("author", ""),
            isbn=d.get("isbn", ""),
            available=d.get("available", True),
            borrow_count=d.get("borrow_count", 0)
        )

    def __repr__(self):
        status = "Available" if self.available else "Borrowed"
        return f"<Book {self.title} by {self.author} | ISBN: {self.isbn} | {status} | borrows: {self.borrow_count}>"
