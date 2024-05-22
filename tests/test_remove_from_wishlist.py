import unittest
from src.remove_from_wishlist import remove_from_wishlist
from src.utils import load_data, save_data
import os


class TestRemoveFromWishlist(unittest.TestCase):

    def setUp(self):
        self.wishlist_file = 'test_wishlist.json'
        self.test_book = {
            "title": "Test Book",
            "author": "Test Author",
            "isbn": "1234567890"
        }
        save_data(self.wishlist_file, [self.test_book])

    def tearDown(self):
        if os.path.exists(self.wishlist_file):
            os.remove(self.wishlist_file)

    def test_remove_from_wishlist(self):
        # Call the function to remove a book from wishlist
        with unittest.mock.patch('builtins.input', return_value='1234567890'):
            remove_from_wishlist(self.wishlist_file)

        # Load wishlist data
        wishlist = load_data(self.wishlist_file)

        # Assert that the book has been removed from wishlist
        self.assertEqual(len(wishlist), 0)


if __name__ == '__main__':
    unittest.main()
