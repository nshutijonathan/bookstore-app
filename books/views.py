from django.shortcuts import render
from django.urls import path
from django.views.generic import ListView, DetailView  # to display lists
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book
# Create your views here.


class BookListView(LoginRequiredMixin, ListView):  # class-based view
    model = Book  # specify model
    template_name = 'books/main.html'  # specify template


class BookDetailView(LoginRequiredMixin, DetailView):  # class-based view
    model = Book  # specify model
    template_name = 'books/detail.html'


urlpatterns = [
    path('books/list', BookListView.as_view()),
]
