from django.db import models


# Create your models here.

class Catalogue(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    definition = models.TextField()

    def __str__(self):
        return self.name
