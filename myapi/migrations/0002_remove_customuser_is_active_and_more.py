# Generated by Django 4.2.3 on 2023-08-14 14:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapi", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="is_staff",
        ),
    ]