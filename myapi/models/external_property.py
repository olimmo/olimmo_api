from django.db import models

from django.contrib.contenttypes.fields import GenericRelation

from django.core.validators import (
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
    URLValidator,
)
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField

from . import BaseModel


class ExternalProperty(BaseModel):
    ENERGY_LETTER_CHOICES = [
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E"),
        ("F", "F"),
        ("G", "G"),
    ]
    CURRENCY_CHOICES = [("EUR", "Euro"), ("USD", "US Dollar")]
    PROPERTY_TYPE_CHOICES = [("Appartement", "Appartement"), ("House", "House")]
    SOURCE_CHOICES = [("Leboncoin", "Leboncoin"), ("pap", "PAP")]

    city = models.CharField(validators=[MinLengthValidator(1)])
    currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES, validators=[MinLengthValidator(1)]
    )
    description = models.TextField(validators=[MinLengthValidator(1)])
    elevator = models.BooleanField(default=False, null=True, blank=True)
    energy_rate = models.CharField(
        null=True, blank=True, max_length=1, choices=ENERGY_LETTER_CHOICES
    )
    first_photo_url = models.CharField(
        null=True, blank=True, validators=[URLValidator()], default=""
    )
    floor_number = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )
    gps_latitude = models.CharField(
        validators=[MinLengthValidator(1)], max_length=20, default=""
    )
    gps_longitude = models.CharField(
        validators=[MinLengthValidator(1)], max_length=20, default=""
    )
    greenhouse_gas = models.CharField(
        null=True, blank=True, max_length=1, choices=ENERGY_LETTER_CHOICES
    )
    history = AuditlogHistoryField()
    nb_bedrooms = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )
    nb_floors_building = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )
    nb_parkings = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )
    nb_rooms = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )
    outside_access = models.CharField(null=True, blank=True)
    postal_code = models.CharField(validators=[MinLengthValidator(1)])
    price = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
    )

    property_type = models.CharField(
        choices=PROPERTY_TYPE_CHOICES,
        default="Appartement",
        validators=[MinLengthValidator(1)],
    )

    region = models.CharField(null=True, blank=True)
    seller_phone = models.CharField(null=True, blank=True)
    seller_name = models.CharField(null=True, blank=True)
    seller_email = models.EmailField(null=True, blank=True)
    source = models.CharField(
        validators=[MinLengthValidator(1)], choices=SOURCE_CHOICES, default="Leboncoin"
    )

    source_id = models.CharField(
        validators=[MinLengthValidator(1)], max_length=100, default=""
    )
    surface = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10000),
        ],
    )
    title = models.CharField(validators=[MinLengthValidator(1)])

    url = models.CharField(validators=[MinLengthValidator(1), URLValidator()])

    # Relationships
    photos = GenericRelation("myapi.Photo")

    def __str__(self):
        return str(vars(self))


auditlog.register(ExternalProperty, include_fields=["price"])
