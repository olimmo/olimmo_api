# Generated by Django 4.2.3 on 2023-08-23 14:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapi", "0010_alter_externalproperty_elevator_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="externalproperty",
            name="nb_parkings",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
    ]
