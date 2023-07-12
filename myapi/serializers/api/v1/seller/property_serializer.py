# serializers.py
from rest_framework import serializers

from myapi.models import Property


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ("id", "city", "surface", "title")
