from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(LoginRequiredMixin,ListView):
    model = Book
    context_object_name = 'book_list'  # this alternaticve for object_list for frontend works
    template_name = 'books/book_list.html'
    login_url = 'account_login'  # login required permission


class BookDetailView(PermissionRequiredMixin,DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    permission_required = 'books.special_status' # our custom permission added here
