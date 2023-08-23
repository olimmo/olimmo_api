from rest_framework import serializers

from myapi.models import UserExternalProperty
from myapi.serializers.api.v1.base_serializer import BaseSerializer
from myapi.serializers.api.v1.external_property_serializer import (
    ExternalPropertySerializer,
)


class UserExternalPropertyRetrieveSerializer(BaseSerializer):
    external_property = ExternalPropertySerializer()

    class Meta:
        model = UserExternalProperty
        fields = "__all__"
        include_fields = ["external_property"]


class UserExternalPropertyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExternalProperty
        fields = ("state",)
