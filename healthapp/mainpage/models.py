from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField(max_length=100)
    water = models.IntegerField(max_length=100)
    alcohol = models.IntegerField(max_length=100)
    caffeine = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name


