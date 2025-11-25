#  Library Inventory System – README (Professional & Short)

A clean and concise professional README for your Python-based Library Management System.

---

##  Overview

This project is a **menu-driven Library Inventory System** built using Python OOP. It manages books, members, borrowing/returning, and stores all data in JSON files for persistence.

---

## Project Structure

```
book.py      # Book class
member.py    # Member class
library.py   # Core system logic (books, members, JSON)
main.py      # Interactive menu (run this file)
books.json   # Auto-saved book data
members.json # Auto-saved member data
```

---

## ✨ Features

* Add books & register members
* Borrow and return books safely
* Auto-save & auto-load JSON data
* Shows library statistics and most borrowed books

---

##  How to Run

```
cd library_system
python main.py
```

Use the menu to manage books and members.

---

##  File Relationships

```
main.py → Library
Library → Book + Member
Book/Member → JSON (books.json, members.json)
```

---

##  Common Fixes

* Ensure file names are correct (`book.py`, `library.py`, etc.)
* Delete Python cache if imports fail:

```
rm -r __pycache__
```

---

## 📝 Author

**Your Name Here**
Library Inventory System – Python Assignment

---

Need a **PDF version**, **UML diagram**, or **submission-ready ZIP**? Just tell me! 🚀
