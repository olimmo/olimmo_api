from django.core.validators import (
    MinLengthValidator,
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models


class Property(models.Model):
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=30, null=True)
    postal_code = models.CharField(max_length=10, null=True)
    surface = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100000),
        ],
    )
    title = models.CharField(
        max_length=60, unique=True, validators=[MinLengthValidator(1)]
    )

    def __str__(self):
        return self.title

    @property
    def full_address(self):
        address_parts = [
            part.strip()
            for part in [self.address, self.city, self.postal_code, self.country]
            if part
        ]
        return " ".join(address_parts)
