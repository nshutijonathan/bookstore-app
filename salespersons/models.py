from django.db import models

# Create your models here.


class SalesPersons(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    bio = models.TextField()
    pic = models.ImageField(upload_to='sales', default='no_picture.jpg')
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
