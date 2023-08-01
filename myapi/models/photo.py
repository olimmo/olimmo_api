from django.db import models

from .external_property import ExternalProperty

from django.core.validators import (
    MinLengthValidator,
    MaxValueValidator,
    MinValueValidator,
    URLValidator,
)

from . import BaseModel


class Photo(BaseModel):
    position = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1000),
        ],
    )

    url = models.CharField(validators=[MinLengthValidator(1), URLValidator()])

    # RELATIONSHIPS
    external_property = models.ForeignKey(
        ExternalProperty,
        on_delete=models.CASCADE,
        related_name="photos",
        null=True,
    )

    def __str__(self):
        return str(vars(self))
