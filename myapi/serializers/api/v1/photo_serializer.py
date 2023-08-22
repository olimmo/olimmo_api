from rest_framework import serializers

from myapi.models import Photo
from myapi.serializers.api.v1 import BaseSerializer


class PhotoSerializer(BaseSerializer):    
    class Meta:
        model = Photo
        fields = "__all__"
