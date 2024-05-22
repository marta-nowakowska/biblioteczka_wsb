import unittest
from src.remove_book import remove_book
from src.utils import load_data, save_data
import os


class TestRemoveBook(unittest.TestCase):

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

    def test_remove_book(self):
        # Set up fake user input for ISBN input
        input_values = iter(['1111111111'])

        def mock_input(prompt):
            return next(input_values)

        # Replace built-in input() function with our mock
        builtins.input = mock_input

        remove_book(self.library_file)
        library = load_data(self.library_file)
        self.assertEqual(len(library), 1)
        self.assertNotIn({"title": "Book 1", "author": "Author 1", "isbn": "1111111111", "status": "unread"}, library)


if __name__ == '__main__':
    unittest.main()
