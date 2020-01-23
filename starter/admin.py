from django.contrib import admin

# this is a relative import since admin and models are in the same directory
from .models import Product
# Register your models here.

admin.site.register(Product)
