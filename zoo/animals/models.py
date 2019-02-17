from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    is_domesticated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

