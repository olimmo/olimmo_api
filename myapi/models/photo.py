from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

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

    # Relationships
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    def __str__(self):
        return str(vars(self))
