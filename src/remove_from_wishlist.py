from utils import load_data, save_data


def remove_from_wishlist(wishlist_file):
    isbn = input("Enter ISBN of the book to remove from wishlist: ")

    wishlist = load_data(wishlist_file)
    updated_wishlist = [book for book in wishlist if book['isbn'] != isbn]
    save_data(wishlist_file, updated_wishlist)
    print("Book removed from wishlist.")
