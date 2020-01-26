from django.db import models

# Create your models here.

# we always run makemigrations and migrate whenever we make changes to our models


class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length is required
    # blank is for a field being required ie. when its false
    # null is for the db, whether a field is nullable
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=False)
    featured = models.BooleanField()  # adding a new field when u already migrated
