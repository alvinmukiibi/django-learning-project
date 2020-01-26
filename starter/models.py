from django.db import models

# Create your models here.

# we always run makemigrations and migrate whenever we make changes to our models


class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length is required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField()
