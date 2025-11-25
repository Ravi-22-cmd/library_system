# main.py
# Name: YOUR_NAME_HERE
# Date: DATE_HERE
# Assignment: Library Inventory System - Main interactive menu

from library import Library

WELCOME_MSG = """
---------------------------------------------
Welcome to the Library Inventory System
---------------------------------------------
"""

def prompt_add_book(lib: Library):
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    isbn = input("Enter book ISBN: ").strip()
    try:
        book = lib.add_book(title=title, author=author, isbn=isbn)
        print(f"Added: {book}")
    except Exception as e:
        print("Error:", e)

def prompt_register_member(lib: Library):
    name = input("Enter member name: ").strip()
    member_id = input("Enter member ID: ").strip()
    try:
        member = lib.register_member(name=name, member_id=member_id)
        print(f"Registered: {member}")
    except Exception as e:
        print("Error:", e)

def prompt_borrow(lib: Library):
    member_id = input("Member ID: ").strip()
    isbn = input("Book ISBN: ").strip()
    try:
        lib.lend_book(member_id=member_id, isbn=isbn)
        print("Book lent successfully.")
    except Exception as e:
        print("Error:", e)

def prompt_return(lib: Library):
    member_id = input("Member ID: ").strip()
    isbn = input("Book ISBN: ").strip()
    try:
        lib.take_return(member_id=member_id, isbn=isbn)
        print("Book returned successfully.")
    except Exception as e:
        print("Error:", e)

def view_report(lib: Library):
    print("\n--- Library Report ---")
    print(lib.report())
    print("----------------------\n")

def list_books(lib: Library):
    books = lib.list_all_books()
    if not books:
        print("No books in library.")
        return
    for b in books:
        status = "Available" if b.available else "Borrowed"
        print(f"{b.title} | {b.author} | ISBN: {b.isbn} | {status} | borrows: {b.borrow_count}")

def list_members(lib: Library):
    members = lib.list_all_members()
    if not members:
        print("No members registered.")
        return
    for m in members:
        print(f"{m.name} | ID: {m.member_id} | borrowed_books: {m.borrowed_books}")

def main():
    print(WELCOME_MSG)
    lib = Library()  # loads existing data if present
    while True:
        print("Menu:")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Library Report")
        print("6. List all books")
        print("7. List all members")
        print("8. Exit")
        choice = input("Choose an option (1-8): ").strip()
        if choice == "1":
            prompt_add_book(lib)
        elif choice == "2":
            prompt_register_member(lib)
        elif choice == "3":
            prompt_borrow(lib)
        elif choice == "4":
            prompt_return(lib)
        elif choice == "5":
            view_report(lib)
        elif choice == "6":
            list_books(lib)
        elif choice == "7":
            list_members(lib)
        elif choice == "8":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
