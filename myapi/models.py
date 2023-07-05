# models.py
from django.db import models


class Property(models.Model):
    title = models.CharField(max_length=60)
    city = models.CharField(max_length=150)

    def __str__(self):
        return self.title
