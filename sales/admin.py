from django.contrib import admin
from .models import Sales
# Register your models here.


class SalesAdmin(admin.ModelAdmin):
    list_display = ('book', 'quantity', 'price', 'date_created', 'updated_at')


admin.site.register(Sales, SalesAdmin)
