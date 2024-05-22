from add_book import add_book_manual, add_book_from_wishlist, add_book_by_isbn
from remove_book import remove_book
from display_books import display_books
from manage_wishlist import manage_wishlist
from add_to_wishlist import add_to_wishlist
from remove_from_wishlist import remove_from_wishlist
from display_wishlist import display_wishlist


def main():
    while True:
        print("\n===== Home Library Menu =====")
        print("1. Add a book manually")
        print("2. Add a book from wishlist")
        print("3. Add a book by ISBN")
        print("4. Display books")
        print("5. Remove a book")
        print("6. Manage wishlist")
        print("7. Add book to wishlist")
        print("8. Remove book from wishlist")
        print("9. Display wishlist")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book_manual()
        elif choice == '2':
            add_book_from_wishlist()
        elif choice == '3':
            add_book_by_isbn()
        elif choice == '4':
            display_books()
        elif choice == '5':
            remove_book()
        elif choice == '6':
            manage_wishlist()
        elif choice == '7':
            add_to_wishlist()
        elif choice == '8':
            remove_from_wishlist()
        elif choice == '9':
            display_wishlist()
        elif choice == '10':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
