from django.db import models

# Create your models here.

class Product(models.Model):
    title       = models.TextField(null=False, max_length=100)
    description = models.TextField(default='enter something')
    price       = models.TextField()
