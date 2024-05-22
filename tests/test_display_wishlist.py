import unittest
from src.display_wishlist import display_wishlist
from src.utils import load_data, save_data
import os
from io import StringIO
import sys


class TestDisplayWishlist(unittest.TestCase):

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

    def test_display_wishlist(self):
        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        display_wishlist(self.wishlist_file)

        sys.stdout = sys.__stdout__  # Restore stdout
        output = captured_output.getvalue().strip()

        expected_output = "Wishlist:\nBook 1 - Author 1 - 1111111111\nBook 2 - Author 2 - 2222222222"
        self.assertEqual(output, expected_output)

    def test_display_empty_wishlist(self):
        # Save an empty wishlist
        save_data(self.wishlist_file, [])
        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        display_wishlist(self.wishlist_file)

        sys.stdout = sys.__stdout__  # Restore stdout
        output = captured_output.getvalue().strip()

        expected_output = "Wishlist is empty."
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
