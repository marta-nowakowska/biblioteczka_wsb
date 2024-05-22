import requests
from utils import load_data, save_data

LIBRARY_FILE = '../data/library.json'
WISHLIST_FILE = '../data/wishlist.json'


def add_book_manual():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    status = input("Enter book status (reading/read/unread): ")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "status": status
    }
    library = load_data(LIBRARY_FILE)
    library.append(book)
    save_data(LIBRARY_FILE, library)
    print("Book added to library.")


def add_book_from_wishlist():
    wishlist = load_data(WISHLIST_FILE)
    if not wishlist:
        print("Wishlist is empty.")
        return

    for i, book in enumerate(wishlist, 1):
        print(f"{i}. {book['title']} - {book['author']}")

    choice = int(input("Choose the number of the book to add to library: ")) - 1
    book = wishlist.pop(choice)
    save_data(WISHLIST_FILE, wishlist)

    status = input("Enter book status (reading/read/unread): ")
    book["status"] = status

    library = load_data(LIBRARY_FILE)
    library.append(book)
    save_data(LIBRARY_FILE, library)
    print("Book added to library.")


def add_book_by_isbn():
    isbn = input("Enter book ISBN: ")
    response = requests.get(f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data")
    data = response.json()
    if not data:
        print("No book found with the given ISBN.")
        return

    book_data = data[f"ISBN:{isbn}"]
    title = book_data.get("title")
    author = ", ".join([author["name"] for author in book_data.get("authors", [])])

    status = input("Enter book status (reading/read/unread): ")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "status": status
    }
    library = load_data(LIBRARY_FILE)
    if not isinstance(library, list):
        library = []
    library.append(book)
    save_data(LIBRARY_FILE, library)
    print("Book added to library.")