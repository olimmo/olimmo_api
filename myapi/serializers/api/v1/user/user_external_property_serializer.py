from rest_framework import serializers
from myapi.models import UserExternalProperty
from myapi.serializers.api.v1.external_property_serializer import (
    ExternalPropertySerializer,
)


class UserExternalPropertyRetrieveSerializer(serializers.ModelSerializer):
    external_property = ExternalPropertySerializer()

    class Meta:
        model = UserExternalProperty
        fields = "__all__"


class UserExternalPropertyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExternalProperty
        fields = ("state",)
