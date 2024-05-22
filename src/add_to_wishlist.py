from utils import load_data, save_data


def add_to_wishlist(wishlist_file):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn
    }

    wishlist = load_data(wishlist_file)
    wishlist.append(book)
    save_data(wishlist_file, wishlist)
    print("Book added to wishlist.")
