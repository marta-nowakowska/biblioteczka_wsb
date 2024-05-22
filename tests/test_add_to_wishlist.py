import unittest
from src.add_to_wishlist import add_to_wishlist
from src.utils import load_data, save_data
import os


class TestAddToWishlist(unittest.TestCase):

    def setUp(self):
        self.wishlist_file = 'test_wishlist.json'
        save_data(self.wishlist_file, [])
        self.test_book = {
            "title": "Test Book",
            "author": "Test Author",
            "isbn": "1234567890"
        }

    def tearDown(self):
        if os.path.exists(self.wishlist_file):
            os.remove(self.wishlist_file)

    def test_add_to_wishlist(self):
        # Call the function to add a book to wishlist
        with unittest.mock.patch('builtins.input', side_effect=["Test Book", "Test Author", "1234567890"]):
            add_to_wishlist(self.wishlist_file)

        # Load wishlist data
        wishlist = load_data(self.wishlist_file)

        # Assert that the book has been added to wishlist
        self.assertEqual(len(wishlist), 1)
        self.assertEqual(wishlist[0], self.test_book)


if __name__ == '__main__':
    unittest.main()
