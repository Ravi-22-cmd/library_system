# member.py
# Name: YOUR_NAME_HERE
# Date: DATE_HERE
# Assignment: Library Inventory System - Member class

class Member:
    def __init__(self, name: str, member_id: str, borrowed_books=None):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else []  # list of ISBNs

    def borrow_book(self, isbn: str):
        if isbn in self.borrowed_books:
            raise ValueError(f"Member {self.member_id} already has book with ISBN {isbn}.")
        self.borrowed_books.append(isbn)

    def return_book(self, isbn: str):
        if isbn not in self.borrowed_books:
            raise ValueError(f"Member {self.member_id} does not have book with ISBN {isbn}.")
        self.borrowed_books.remove(isbn)

    def list_books(self):
        return list(self.borrowed_books)

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            name=d.get("name", ""),
            member_id=d.get("member_id", ""),
            borrowed_books=d.get("borrowed_books", [])
        )

    def __repr__(self):
        return f"<Member {self.name} | ID: {self.member_id} | borrowed: {len(self.borrowed_books)}>"
