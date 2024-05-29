from add_book import (
    add_book_by_isbn_from_openlibrary,
    add_book_from_wishlist,
    add_book_manual,
)
from display_books import display_books
from remove_book import remove_book
from utils import LIBRARY_FILE, WISHLIST_FILE


def main():
    while True:
        print("\n===== Home Library Menu =====")
        print("1. Add a book manually")
        print("2. Add a book from wishlist")
        print("3. Add a book by ISBN")
        print("4. Display books")
        print("5. Remove a book")
        print("6. Add book to wishlist")
        print("7. Remove book from wishlist")
        print("8. Display wishlist")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book_manual(LIBRARY_FILE)
        elif choice == "2":
            add_book_from_wishlist()
        elif choice == "3":
            add_book_by_isbn_from_openlibrary()
        elif choice == "4":
            display_books(LIBRARY_FILE)
        elif choice == "5":
            remove_book(LIBRARY_FILE)
        elif choice == "6":
            add_book_manual(WISHLIST_FILE, ask_for_satus=False)
        elif choice == "7":
            remove_book(WISHLIST_FILE)
        elif choice == "8":
            display_books(WISHLIST_FILE)
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
