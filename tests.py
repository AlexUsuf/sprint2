from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_book_name_true(self, book_name):
        books = BooksCollector()
        books.add_new_book(name=book_name)
        assert_book = list(books.books_rating.keys())
        assert assert_book[0] == book_name

    def test_get_book_rating_default_rating_true(self, book_name):
        books = BooksCollector()
        books.add_new_book(name=book_name)
        assert books.get_book_rating(book_name) == 1

    def test_get_book_rating_set_default_rating_true(self, book_name):
        default_rating = 3
        books = BooksCollector()
        books.add_new_book(name=book_name)
        books.set_book_rating(book_name, default_rating)
        assert books.get_book_rating(book_name) == default_rating

    def test_get_book_specific_rating_set_some_rating_tru(self, book_name):
        default_rating = 3
        books = BooksCollector()
        books.add_new_book(name=book_name)
        books.set_book_rating(book_name, default_rating)
        books.get_books_with_specific_rating(default_rating)
        assert books.get_book_rating(book_name) == default_rating

    def test_get_books_rating_type_dict_true(self, book_name):
        books = BooksCollector()
        books.add_new_book(name=book_name)
        books.get_books_rating()
        assert type(books.get_books_rating()) == dict

    def test_get_books_rating_check_equal_books_true(self, book_name):
        books = BooksCollector()
        books.add_new_book(name=book_name)
        books.add_new_book(name='book2')
        books.get_books_rating()
        assert len(books.get_books_rating()) == 2

    def test_add_book_in_favorites_check_favourite_books_true(self, book_name):
        books = BooksCollector()
        books.add_new_book(name=book_name)
        books.add_book_in_favorites(book_name)
        assert book_name in books.get_list_of_favorites_books()

    def test_delete_book_from_favorites_check_del_favourite_book_true(self, book_name):
        books = BooksCollector()
        books.add_new_book(name=book_name)
        books.add_book_in_favorites(book_name)
        books.delete_book_from_favorites(book_name)
        books_list = books.get_list_of_favorites_books()
        assert book_name not in books_list

    def test_get_list_of_favorites_books_check_favourite_books_true(self, book_name):
        books = BooksCollector()
        books.add_new_book(name=book_name)
        books.add_new_book(name='book_name2')
        books.add_book_in_favorites(book_name)
        assert book_name in books.get_list_of_favorites_books()
