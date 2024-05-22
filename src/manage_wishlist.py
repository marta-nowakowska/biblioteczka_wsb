from utils import load_data, save_data

WISHLIST_FILE = '../data/wishlist.json'


def manage_wishlist():
    action = input("What do you want to do? (add/remove/display): ")
    if action == "add":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")

        book = {
            "title": title,
            "author": author,
            "isbn": isbn
        }
        wishlist = load_data(WISHLIST_FILE)
        wishlist.append(book)
        save_data(WISHLIST_FILE, wishlist)
        print("Book added to wishlist.")
    elif action == "remove":
        display_wishlist()
        isbn = input("Enter the ISBN of the book to remove from wishlist: ")
        wishlist = load_data(WISHLIST_FILE)
        wishlist = [book for book in wishlist if book['isbn'] != isbn]
        save_data(WISHLIST_FILE, wishlist)
        print("Book removed from wishlist.")
    elif action == "display":
        display_wishlist()
    else:
        print("Unknown action.")


def display_wishlist():
    wishlist = load_data(WISHLIST_FILE)
    for book in wishlist:
        print(f"{book['title']} - {book['author']} - {book['isbn']}")