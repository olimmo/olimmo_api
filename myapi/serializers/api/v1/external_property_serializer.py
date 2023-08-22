from rest_framework import serializers

from myapi.models import ExternalProperty
from myapi.serializers.api.v1 import BaseSerializer
from myapi.serializers.api.v1.photo_serializer import PhotoSerializer


class ExternalPropertySerializer(BaseSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = ExternalProperty
        fields = "__all__"
        include_fields = ["photos"]
