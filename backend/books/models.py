from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publishing_year = models.IntegerField()
