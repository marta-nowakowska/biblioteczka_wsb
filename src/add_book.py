from enum import Enum

import requests

from display_books import display_books
from utils import LIBRARY_FILE, WISHLIST_FILE, load_data, save_data


class BookStatus(Enum):
    READING = "reading"
    READ = "read"
    UNREAD = "unread"


def add_book(title, author, isbn, file, status=None):
    """Dodaje książkę do pliku (w zależności od ścieżki)."""
    book = {"title": title, "author": author, "isbn": isbn, "status": status}
    library = load_data(file)
    library.append(book)
    save_data(file, library)
    print(f"Book added to library. {book}")


def add_book_manual(file, ask_for_satus=True):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    status = "unread"

    if ask_for_satus:
        try:
            status = input("Enter book status (reading/read/unread): ").strip().lower()
            BookStatus(status)
        except ValueError:
            print(
                "Invalid status! "
                "Please enter one of the following: reading, read, unread."
            )
            return

    add_book(title, author, isbn, file, status=status)


def add_book_from_wishlist():
    """Wczytuje whishlistę, usuwa z niej wybraną książkę i dodaje do biblioteczki."""
    wishlist = load_data(WISHLIST_FILE)
    if not wishlist:
        print("Wishlist is empty.")
        return

    display_books(WISHLIST_FILE)

    choice = int(input("Choose the number of the book to add to library: ")) - 1
    book = wishlist.pop(choice)
    save_data(WISHLIST_FILE, wishlist)

    add_book(
        book["title"], book["author"], book["isbn"], LIBRARY_FILE, status=book["status"]
    )


def add_book_by_isbn_from_openlibrary():
    isbn = input("Enter book ISBN: ")
    response = requests.get(
        f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    )
    data = response.json()
    if not data:
        print("No book found with the given ISBN.")
        return

    book_data = data[f"ISBN:{isbn}"]
    title = book_data.get("title")

    authors = book_data.get("authors", [])
    author = "N/A"
    if len(authors) == 1:
        author = authors[0]["name"]
    if len(authors) > 1:
        author = ", ".join([author["name"] for author in authors])

    status = input("Enter book status (reading/read/unread): ")

    add_book(title, author, isbn, LIBRARY_FILE, status=status)
