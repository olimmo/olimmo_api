# serializers.py
from rest_framework import serializers

from myapi.models import Property


class LeboncoinPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ("id", "city", "postal_code", "surface", "title")