import os
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

from src.remove_book import remove_book
from src.utils import load_data, save_data


class TestRemoveBook(TestCase):

    def setUp(self):
        self.library_file = Path("test_library.json")
        self.test_data = [
            {
                "title": "Book 1",
                "author": "Author 1",
                "isbn": "1111111111",
                "status": "unread",
            },
            {
                "title": "Book 2",
                "author": "Author 2",
                "isbn": "2222222222",
                "status": "read",
            },
        ]
        save_data(self.library_file, self.test_data)

    def tearDown(self):
        if os.path.exists(self.library_file):
            os.remove(self.library_file)

    def test_remove_book(self):
        # Set up fake user input for ISBN input
        with patch("src.remove_book.input", side_effect=["1111111111"]):
            remove_book(self.library_file)
            library = load_data(self.library_file)
            self.assertEqual(len(library), 1)
            self.assertNotIn(
                {
                    "title": "Book 1",
                    "author": "Author 1",
                    "isbn": "1111111111",
                    "status": "unread",
                },
                library,
            )
