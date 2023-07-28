from django.db import models

from .external_property import ExternalProperty

from django.core.validators import (
    MinLengthValidator,
    MaxValueValidator,
    MinValueValidator,
    URLValidator,
)


class Photo(models.Model):
    position = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000),
        ],
    )

    url = models.CharField(validators=[MinLengthValidator(1), URLValidator()])

    # RELATIONSHIPS
    external_property = models.ForeignKey(
        ExternalProperty,
        on_delete=models.CASCADE,
        related_name="external_properties",
        null=True,
    )

    def __str__(self):
        return str(vars(self))
