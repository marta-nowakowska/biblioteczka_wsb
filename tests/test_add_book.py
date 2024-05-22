import unittest
from src.add_book import add_book_manual, add_book_from_wishlist, add_book_by_isbn
from src.utils import load_data, save_data
import os


class TestAddBook(unittest.TestCase):

    def setUp(self):
        self.library_file = 'test_library.json'
        self.wishlist_file = 'test_wishlist.json'
        self.test_data = {
            "title": "Test Book",
            "author": "Test Author",
            "isbn": "1234567890",
            "status": "unread"
        }
        save_data(self.library_file, [])
        save_data(self.wishlist_file, [])

    def tearDown(self):
        if os.path.exists(self.library_file):
            os.remove(self.library_file)
        if os.path.exists(self.wishlist_file):
            os.remove(self.wishlist_file)

    def test_add_book_manual(self):
        add_book_manual(title=self.test_data['title'], author=self.test_data['author'],
                        isbn=self.test_data['isbn'], status=self.test_data['status'])
        library = load_data(self.library_file)
        self.assertEqual(len(library), 1)
        self.assertEqual(library[0]['title'], self.test_data['title'])

    def test_add_book_from_wishlist(self):
        save_data(self.wishlist_file, [self.test_data])
        add_book_from_wishlist(self.library_file, self.wishlist_file)
        library = load_data(self.library_file)
        wishlist = load_data(self.wishlist_file)
        self.assertEqual(len(library), 1)
        self.assertEqual(len(wishlist), 0)
        self.assertEqual(library[0], self.test_data)

    def test_add_book_by_isbn(self):
        with unittest.mock.patch('src.add_book.input', side_effect=["1234567890", "unread"]):
            with unittest.mock.patch('requests.get') as mocked_get:
                mocked_response = unittest.mock.Mock()
                mocked_response.json.return_value = {
                    f"ISBN:{self.test_data['isbn']}": self.test_data
                }
                mocked_get.return_value = mocked_response
                add_book_by_isbn(self.library_file)
                library = load_data(self.library_file)
                self.assertEqual(len(library), 1)
                self.assertEqual(library[0], self.test_data)


if __name__ == '__main__':
    unittest.main()
