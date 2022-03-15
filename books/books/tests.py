from django.test import TestCase, Client
from django.urls import reverse

from .models import Book


class BookTests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title='Oka_book',
            author='sharif',
            price='25.00',
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Oka_book')
        self.assertEqual(f'{self.book.author}', 'sharif')
        self.assertEqual(f'{self.book.price}', '25.00')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code,200)
        self.assertNotContains(response,'Oka book')
        self.assertTemplateUsed(response,'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_resonse = self.client.get('/book/1234/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_resonse.status_code, 400)
        self.assertNotContains(response, 'Oka book')
        self.assertTemplateUsed(response, 'books/book_list.html')

