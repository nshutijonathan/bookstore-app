
from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField()
    pic = models.ImageField(upload_to='customers', default='no_picture.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
