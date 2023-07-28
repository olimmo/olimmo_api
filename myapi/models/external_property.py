from django.db import models

from django.core.validators import (
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
    URLValidator,
)


class ExternalProperty(models.Model):
    CURRENCY_CHOICES = [("EUR", "Euro"), ("USD", "US Dollar")]
    SOURCE_CHOICES = [("Leboncoin", "Leboncoin"), ("PAP", "PAP")]

    title = models.CharField(validators=[MinLengthValidator(1)])
    surface = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100000),
        ],
    )
    city = models.CharField(validators=[MinLengthValidator(1)])
    currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES, validators=[MinLengthValidator(1)]
    )
    description = models.TextField(validators=[MinLengthValidator(1)])
    elevator = models.BooleanField(default=False)
    energy_rate = models.CharField(null=True, blank=True, max_length=100)
    first_photo_url = models.CharField(
        validators=[MinLengthValidator(1), URLValidator()], max_length=200, default=""
    )
    floor_number = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100000),
        ],
    )
    gps_latitude = models.CharField(
        validators=[MinLengthValidator(1)], max_length=100, default=""
    )
    gps_longitude = models.CharField(
        validators=[MinLengthValidator(1)], max_length=100, default=""
    )
    greenhouse_gas = models.CharField(null=True)
    has_phone = models.BooleanField(default=False)
    immo_type = models.CharField(null=True)
    kind = models.CharField(null=True)
    nb_floors_building = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100000),
        ],
    )
    nb_parkings = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100000),
        ],
    )
    nb_rooms = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )
    outside_access = models.CharField(null=True)
    phone: models.CharField(null=True)
    postal_code = models.CharField(validators=[MinLengthValidator(1)])
    region = models.CharField(validators=[MinLengthValidator(1)])
    source = models.CharField(validators=[MinLengthValidator(1)])
    source_id = models.CharField(
        unique=True, validators=[MinLengthValidator(1)], max_length=100, default=""
    )
    url = models.CharField(validators=[MinLengthValidator(1), URLValidator()])

    def __str__(self):
        return str(vars(self))
