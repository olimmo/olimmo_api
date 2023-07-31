from django.db import models

from django.core.validators import MinLengthValidator

from . import BaseModel

CIVILITIES = (
    ("mr", "Mr"),
    ("mrs", "Mrs"),
    ("unspecified", "Unspecified"),
)


class Seller(BaseModel):
    civility = models.CharField(max_length=12, choices=CIVILITIES)
    email = models.CharField(unique=True, validators=[MinLengthValidator(1)])
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(1)])
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(1)])
    phone = models.CharField(max_length=20, validators=[MinLengthValidator(1)])

    def __str__(self):
        return str(vars(self))
