# library.py
# Name: YOUR_NAME_HERE
# Date: DATE_HERE
# Assignment: Library Inventory System - Library logic and persistence

import json
import os
from book import Book
from member import Member

DEFAULT_BOOKS_FILE = "books.json"
DEFAULT_MEMBERS_FILE = "members.json"

class Library:
    def __init__(self, books_file=DEFAULT_BOOKS_FILE, members_file=DEFAULT_MEMBERS_FILE):
        self.books_file = books_file
        self.members_file = members_file
        # store as dicts for quick lookup: isbn -> Book, member_id -> Member
        self.books = {}
        self.members = {}
        # Try loading existing data
        self.load_data()

    # ---------- Book/member management ----------
    def add_book(self, title: str, author: str, isbn: str):
        if isbn in self.books:
            raise ValueError(f"A book with ISBN {isbn} already exists.")
        book = Book(title=title, author=author, isbn=isbn)
        self.books[isbn] = book
        self.save_data()
        return book

    def register_member(self, name: str, member_id: str):
        if member_id in self.members:
            raise ValueError(f"Member ID {member_id} already registered.")
        member = Member(name=name, member_id=member_id)
        self.members[member_id] = member
        self.save_data()
        return member

    def lend_book(self, member_id: str, isbn: str):
        if member_id not in self.members:
            raise ValueError(f"No member with ID {member_id}.")
        if isbn not in self.books:
            raise ValueError(f"No book with ISBN {isbn}.")
        member = self.members[member_id]
        book = self.books[isbn]
        if not book.available:
            raise ValueError(f"Book '{book.title}' is currently not available.")
        # perform borrow
        book.borrow()
        member.borrow_book(isbn)
        self.save_data()
        return True

    def take_return(self, member_id: str, isbn: str):
        if member_id not in self.members:
            raise ValueError(f"No member with ID {member_id}.")
        if isbn not in self.books:
            raise ValueError(f"No book with ISBN {isbn}.")
        member = self.members[member_id]
        book = self.books[isbn]
        # perform return
        member.return_book(isbn)
        book.return_book()
        self.save_data()
        return True

    # ---------- Persistence ----------
    def save_data(self):
        # Save books
        try:
            with open(self.books_file, "w", encoding="utf-8") as f:
                books_list = [b.to_dict() for b in self.books.values()]
                json.dump(books_list, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving books: {e}")

        # Save members
        try:
            with open(self.members_file, "w", encoding="utf-8") as f:
                members_list = [m.to_dict() for m in self.members.values()]
                json.dump(members_list, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving members: {e}")

    def load_data(self):
        # Load books
        if os.path.exists(self.books_file):
            try:
                with open(self.books_file, "r", encoding="utf-8") as f:
                    books_list = json.load(f)
                    for bd in books_list:
                        book = Book.from_dict(bd)
                        self.books[book.isbn] = book
            except Exception as e:
                print(f"Warning: could not load books file ({self.books_file}): {e}")

        # Load members
        if os.path.exists(self.members_file):
            try:
                with open(self.members_file, "r", encoding="utf-8") as f:
                    members_list = json.load(f)
                    for md in members_list:
                        member = Member.from_dict(md)
                        self.members[member.member_id] = member
            except Exception as e:
                print(f"Warning: could not load members file ({self.members_file}): {e}")

    # ---------- Reporting / Utility ----------
    def list_all_books(self):
        return list(self.books.values())

    def list_all_members(self):
        return list(self.members.values())

    def find_book(self, isbn: str):
        return self.books.get(isbn)

    def find_member(self, member_id: str):
        return self.members.get(member_id)

    # Analytics examples:
    def most_borrowed_book(self):
        if not self.books:
            return None, 0
        # return Book object(s) with highest borrow_count (could be tie)
        max_count = max((b.borrow_count for b in self.books.values()), default=0)
        most = [b for b in self.books.values() if b.borrow_count == max_count]
        return most, max_count        # run from d:\Assignment_3
       

    def total_active_members(self):
        # active = members who currently have at least one borrowed book
        return sum(1 for m in self.members.values() if m.borrowed_books)

    def currently_borrowed_count(self):
        return sum(1 for b in self.books.values() if not b.available)

    def report(self):
        most, count = self.most_borrowed_book()
        report_lines = []
        report_lines.append(f"Total books in library: {len(self.books)}")
        report_lines.append(f"Total members registered: {len(self.members)}")
        report_lines.append(f"Currently borrowed books: {self.currently_borrowed_count()}")
        report_lines.append(f"Active members (have >=1 borrowed book): {self.total_active_members()}")
        if most and count > 0:
            titles = ", ".join(f"'{b.title}'(ISBN:{b.isbn})" for b in most)
            report_lines.append(f"Most borrowed book(s): {titles} — borrowed {count} times")
        else:
            report_lines.append("Most borrowed book(s): None yet")
        return "\n".join(report_lines)
