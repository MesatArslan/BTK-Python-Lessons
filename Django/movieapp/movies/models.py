from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    movies_name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=100)
    homepage = models.BooleanField(default=False)
