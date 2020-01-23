from django.db import models

# Create your models here.

# we always run makemigrations and migrate whenever we make changes to our models


class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='this is awesome')
