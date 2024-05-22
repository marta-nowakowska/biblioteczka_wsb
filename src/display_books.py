from utils import load_data

LIBRARY_FILE = '../data/library.json'

def display_books(filter_by=None, filter_value=None):
    library = load_data(LIBRARY_FILE)
    if filter_by and filter_value:
        library = [book for book in library if book.get(filter_by) == filter_value]

    for book in library:
        print(f"{book['title']} - {book['author']} - {book['isbn']} - {book['status']}")