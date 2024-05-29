from display_books import display_books
from utils import load_data, save_data


def remove_book(file):
    display_books(file)
    isbn = input("Enter the ISBN of the book to remove: ")
    library = load_data(file)
    library = [book for book in library if book["isbn"] != isbn]
    save_data(file, library)
    print("Book removed from library.")
