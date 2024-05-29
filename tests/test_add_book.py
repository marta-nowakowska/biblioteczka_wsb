import os
from pathlib import Path
from unittest import TestCase
from unittest.mock import Mock, patch

from src.add_book import (
    add_book_by_isbn_from_openlibrary,
    add_book_from_wishlist,
    add_book_manual,
)
from src.utils import load_data, save_data


class TestAddBook(TestCase):

    def setUp(self):
        self.library_file = Path("test_library.json")
        self.wishlist_file = Path("test_wishlist.json")
        self.test_data = {
            "title": "Test Book",
            "author": "Test Author",
            "isbn": "1234567890",
            "status": "unread",
        }
        save_data(self.library_file, [])
        save_data(self.wishlist_file, [])

    def tearDown(self):
        if os.path.exists(self.library_file):
            os.remove(self.library_file)
        if os.path.exists(self.wishlist_file):
            os.remove(self.wishlist_file)

    def test_add_book_manual(self):
        with patch(
            "src.add_book.input",
            side_effect=[
                self.test_data["title"],
                self.test_data["author"],
                self.test_data["isbn"],
                self.test_data["status"],
            ],
        ):
            add_book_manual(self.library_file)
            library = load_data(self.library_file)
            self.assertEqual(len(library), 1)
            self.assertEqual(self.test_data, library[0])

    def test_add_book_manual_no_status(self):
        expected_data = self.test_data.copy()
        self.test_data.pop("status")
        with patch(
            "src.add_book.input",
            side_effect=[
                self.test_data["title"],
                self.test_data["author"],
                self.test_data["isbn"],
            ],
        ):
            add_book_manual(self.library_file, ask_for_satus=False)
            library = load_data(self.library_file)
            self.assertEqual(len(library), 1)
            self.assertEqual(expected_data, library[0])

    def test_add_book_manual_wrong_status(self):
        with patch(
            "src.add_book.input",
            side_effect=[
                self.test_data["title"],
                self.test_data["author"],
                self.test_data["isbn"],
                "wrong_argument",
            ],
        ):
            add_book_manual(self.library_file)
            library = load_data(self.library_file)
            self.assertEqual(len(library), 0)

    def test_add_book_from_wishlist(self):
        save_data(self.wishlist_file, [self.test_data])
        with patch("src.add_book.LIBRARY_FILE", self.library_file):
            with patch("src.add_book.WISHLIST_FILE", self.wishlist_file):
                with patch("src.add_book.input", side_effect=["1"]):
                    add_book_from_wishlist()
                    library = load_data(self.library_file)
                    wishlist = load_data(self.wishlist_file)
                    self.assertEqual(len(library), 1)
                    self.assertEqual(len(wishlist), 0)
                    self.assertEqual(library[0], self.test_data)

    def test_add_book_by_isbn(self):
        with patch("src.add_book.input", side_effect=["1234567890", "unread"]):
            with patch("requests.get") as mocked_get:
                with patch("src.add_book.LIBRARY_FILE", self.library_file):
                    mocked_response = Mock()
                    test_data = self.test_data.copy()
                    test_data["authors"] = []
                    test_data["authors"].append({"name": self.test_data["author"]})

                    mocked_response.json.return_value = {
                        f"ISBN:{test_data['isbn']}": test_data
                    }
                    mocked_get.return_value = mocked_response
                    add_book_by_isbn_from_openlibrary()
                    library = load_data(self.library_file)
                    self.assertEqual(len(library), 1)
                    self.assertEqual(library[0], self.test_data)
