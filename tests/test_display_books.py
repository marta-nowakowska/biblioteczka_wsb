import os
import sys
from io import StringIO
from pathlib import Path
from unittest import TestCase

from src.display_books import display_books
from src.utils import save_data


class TestDisplayBooks(TestCase):

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

    def test_display_books(self):
        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        display_books(self.library_file)

        sys.stdout = sys.__stdout__  # Restore stdout
        output = captured_output.getvalue().strip()

        expected_output = (
            "Book 1 - Author 1 - 1111111111 - unread\n"
            "Book 2 - Author 2 - 2222222222 - read"
        )
        self.assertEqual(expected_output, output)

    def test_display_books_with_filter(self):
        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        display_books(self.library_file, filter_by="author", filter_value="Author 1")

        sys.stdout = sys.__stdout__  # Restore stdout
        output = captured_output.getvalue().strip()

        expected_output = "Book 1 - Author 1 - 1111111111 - unread"
        self.assertEqual(expected_output, output)
