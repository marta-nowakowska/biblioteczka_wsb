from display_books import display_books
from utils import load_data, save_data

LIBRARY_FILE = '../data/library.json'

def remove_book():
    display_books()
    isbn = input("Enter the ISBN of the book to remove: ")
    library = load_data(LIBRARY_FILE)
    library = [book for book in library if book['isbn'] != isbn]
    save_data(LIBRARY_FILE, library)
    print("Book removed from library.")