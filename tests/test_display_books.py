import unittest
from src.display_books import display_books
from src.utils import load_data, save_data
import os

class TestDisplayBooks(unittest.TestCase):

    def setUp(self):
        self.library_file = 'test_library.json'
        self.test_data = [
            {"title": "Book 1", "author": "Author 1", "isbn": "1111111111", "status": "unread"},
            {"title": "Book 2", "author": "Author 2", "isbn": "2222222222", "status": "read"}
        ]
        save_data(self.library_file, self.test_data)

    def tearDown(self):
        if os.path.exists(self.library_file):
            os.remove(self.library_file)

    def test_display_books(self):
        # Redirect stdout to capture print output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        display_books(self.library_file)

        sys.stdout = sys.__stdout__  # Restore stdout
        output = captured_output.getvalue().strip()

        expected_output = "Book 1 - Author 1 - 1111111111 - unread\nBook 2 - Author 2 - 2222222222 - read"
        self.assertEqual(output, expected_output)

    def test_display_books_with_filter(self):
        # Redirect stdout to capture print output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        # Mock user input for filtering by author
        with unittest.mock.patch('builtins.input', side_effect=['yes', 'author', 'Author 1']):
            display_books(self.library_file)

        sys.stdout = sys.__stdout__  # Restore stdout
        output = captured_output.getvalue().strip()

        expected_output = "Book 1 - Author 1 - 1111111111 - unread"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
