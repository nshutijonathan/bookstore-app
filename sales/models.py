from django.db import models
from django.shortcuts import reverse
from books.models import Book
# Create your models here.
import datetime


class Sales(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"id: {self.id}, book: {self.book.name}, quantity: {self.quantity}, price: {self.price}"

    # def get_absolute_url(self):
    #     return reverse('sales:records', kwargs={'pk': self.pk})
