from utils import load_data

def display_wishlist(wishlist_file):
    wishlist = load_data(wishlist_file)
    if not wishlist:
        print("Wishlist is empty.")
    else:
        print("Wishlist:")
        for book in wishlist:
            print(f"{book['title']} - {book['author']} - {book['isbn']}")
