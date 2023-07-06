from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models


class Property(models.Model):
    city = models.CharField(max_length=150)
    surface = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100000),
        ],
    )
    title = models.CharField(max_length=60, unique=True, validators=[MinLengthValidator(1)])

    def __str__(self):
        return self.title
