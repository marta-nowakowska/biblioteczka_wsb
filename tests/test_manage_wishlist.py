import unittest
from src.manage_wishlist import manage_wishlist
from src.utils import load_data, save_data
import os


class TestManageWishlist(unittest.TestCase):

    def setUp(self):
        self.wishlist_file = 'test_wishlist.json'
        self.test_data = [
            {"title": "Book 1", "author": "Author 1", "isbn": "1111111111"},
            {"title": "Book 2", "author": "Author 2", "isbn": "2222222222"}
        ]
        save_data(self.wishlist_file, self.test_data)

    def tearDown(self):
        if os.path.exists(self.wishlist_file):
            os.remove(self.wishlist_file)

    def test_add_book_to_wishlist(self):
        with unittest.mock.patch('builtins.input', side_effect=['Test Book', 'Test Author', '1234567890']):
            manage_wishlist(self.wishlist_file)
            wishlist = load_data(self.wishlist_file)
            self.assertEqual(len(wishlist), 3)

    def test_remove_book_from_wishlist(self):
        with unittest.mock.patch('builtins.input', return_value='1111111111'):
            manage_wishlist(self.wishlist_file)
            wishlist = load_data(self.wishlist_file)
            self.assertEqual(len(wishlist), 1)
            self.assertNotIn({"title": "Book 1", "author": "Author 1", "isbn": "1111111111"}, wishlist)


if __name__ == '__main__':
    unittest.main()
