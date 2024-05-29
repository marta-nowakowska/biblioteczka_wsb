from utils import load_data


def display_books(file, filter_by=None, filter_value=None):
    library = load_data(file)
    if filter_by and filter_value:
        library = [book for book in library if book.get(filter_by) == filter_value]

    for idx, book in enumerate(library, start=1):
        print(
            f"{idx}: "
            f"{book['title']} - {book['author']} - "
            f"{book['isbn']} - {book.get('status', 'unread')}"
        )
