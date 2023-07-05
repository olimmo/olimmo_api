# serializers.py
from rest_framework import serializers

from .models import Property


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'title', 'city')
