from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(blank=False, unique=True, max_length=36)
    description = models.TextField(max_length=250, blank=True)

    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    published = models.DateField()