from myapi.models import Photo
from myapi.serializers.api.v1.base_serializer import BaseSerializer


class PhotoSerializer(BaseSerializer):
    class Meta:
        model = Photo
        fields = "__all__"
