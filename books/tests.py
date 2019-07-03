from django.test import TestCase, Client

from .models import Book

class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title="book1", author="author1", genre="genre1")
        Book.objects.create(title="book2", author="author2", genre="genre2")

    # MODELS
    def test_book_creation(self):
        book1 = Book.objects.get(id=1)
        expected_book1_title = f'{book1.title}'        
        self.assertEquals(expected_book1_title, 'book1')
        book2 = Book.objects.get(id=2)
        expected_book2_title = f'{book2.title}'
        self.assertEquals(expected_book2_title, 'book2')

    def test_book_print_string(self):
        book1 = Book.objects.get(title="book1")
        book2 = Book.objects.get(title="book2")
        self.assertAlmostEqual(book1.__str__(), 'book1 - author1 - genre1')
        self.assertAlmostEqual(book2.__str__(), 'book2 - author2 - genre2')

    # VIEWS
    def test_get_books_route(self):
        c = Client(enforce_csrf_checks=True)
        response = c.get('/books/')
        self.assertEquals(response.status_code, 200)

    def test_get_books_create_route(self):
        c = Client()
        response = c.get('/books/create/')
        self.assertEquals(response.status_code, 200)

    def test_get_books_delete_route(self):
        c = Client()
        response = c.get('/books/delete/')
        self.assertEquals(response.status_code, 200)