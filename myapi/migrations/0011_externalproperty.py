# Generated by Django 4.2.3 on 2023-07-28 14:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapi", "0010_alter_seller_first_name_alter_seller_last_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExternalProperty",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        validators=[django.core.validators.MinLengthValidator(1)]
                    ),
                ),
                (
                    "surface",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100000),
                        ],
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        validators=[django.core.validators.MinLengthValidator(1)]
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        validators=[django.core.validators.MinLengthValidator(1)]
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        validators=[django.core.validators.MinLengthValidator(1)]
                    ),
                ),
                ("elevator", models.BooleanField(default=False)),
                (
                    "floor_number",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100000),
                        ],
                    ),
                ),
                ("greenhouse_gas", models.CharField(null=True)),
                ("has_phone", models.BooleanField(default=False)),
                ("immo_type", models.CharField(null=True)),
                ("kind", models.CharField(null=True)),
                (
                    "nb_floors_building",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100000),
                        ],
                    ),
                ),
                (
                    "nb_parkings",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100000),
                        ],
                    ),
                ),
                (
                    "nb_rooms",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        validators=[django.core.validators.MinLengthValidator(1)]
                    ),
                ),
                (
                    "region",
                    models.CharField(
                        validators=[django.core.validators.MinLengthValidator(1)]
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        validators=[django.core.validators.MinLengthValidator(1)]
                    ),
                ),
                (
                    "url",
                    models.CharField(
                        validators=[django.core.validators.MinLengthValidator(1)]
                    ),
                ),
            ],
        ),
    ]
